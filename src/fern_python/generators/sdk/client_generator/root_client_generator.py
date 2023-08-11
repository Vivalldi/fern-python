import typing
from dataclasses import dataclass
from typing import List, Optional

import fern.ir.resources as ir_types

from fern_python.codegen import AST, SourceFile
from fern_python.codegen.ast.nodes.code_writer.code_writer import CodeWriterFunction
from fern_python.external_dependencies import HttpX
from fern_python.generators.sdk.client_generator.endpoint_response_code_writer import (
    EndpointResponseCodeWriter,
)
from fern_python.generators.sdk.core_utilities.client_wrapper_generator import (
    ClientWrapperGenerator,
)

from ..context.sdk_generator_context import SdkGeneratorContext
from ..environment_generators import (
    MultipleBaseUrlsEnvironmentGenerator,
    SingleBaseUrlEnvironmentGenerator,
)
from .constants import DEFAULT_BODY_PARAMETER_VALUE
from .endpoint_function_generator import EndpointFunctionGenerator


@dataclass
class RootClientConstructorParameter:
    constructor_parameter_name: str
    type_hint: AST.TypeHint
    private_member_name: typing.Optional[str] = None
    initializer: Optional[AST.Expression] = None
    exclude_from_wrapper_construction: Optional[bool] = False


class RootClientGenerator:
    ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME = "environment"
    ENVIRONMENT_MEMBER_NAME = "_environment"

    BASE_URL_CONSTRUCTOR_PARAMETER_NAME = "base_url"
    BASE_URL_MEMBER_NAME = "_base_url"

    RESPONSE_VARIABLE = EndpointResponseCodeWriter.RESPONSE_VARIABLE
    RESPONSE_JSON_VARIABLE = EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE

    def __init__(
        self,
        *,
        context: SdkGeneratorContext,
        package: ir_types.Package,
        class_name: str,
        async_class_name: str,
    ):
        self._context = context
        self._package = package
        self._class_name = class_name
        self._async_class_name = async_class_name
        self._is_default_body_parameter_used = False

        client_wrapper_generator = ClientWrapperGenerator(context=self._context)
        self._client_wrapper_constructor_params = (
            client_wrapper_generator._get_constructor_info().constructor_parameters
        )

        self._timeout_constructor_parameter_name = self._get_timeout_constructor_parameter_name(
            [param.constructor_parameter_name for param in self._client_wrapper_constructor_params]
        )

    def generate(self, source_file: SourceFile) -> None:
        class_declaration = self._create_class_declaration(is_async=False)
        if self._is_default_body_parameter_used:
            source_file.add_arbitrary_code(AST.CodeWriter(self._write_default_param))
        source_file.add_class_declaration(
            declaration=class_declaration,
            should_export=False,
        )
        source_file.add_class_declaration(
            declaration=self._create_class_declaration(is_async=True),
            should_export=False,
        )

    def _create_class_declaration(self, *, is_async: bool) -> AST.ClassDeclaration:
        constructor_parameters = self._get_constructor_parameters(is_async=is_async)

        named_parameters = [
            AST.NamedFunctionParameter(
                name=param.constructor_parameter_name,
                type_hint=param.type_hint,
                initializer=param.initializer,
            )
            for param in constructor_parameters
        ]

        class_declaration = AST.ClassDeclaration(
            name=self._async_class_name if is_async else self._class_name,
            constructor=AST.ClassConstructor(
                signature=AST.FunctionSignature(
                    named_parameters=named_parameters,
                ),
                body=AST.CodeWriter(self._get_write_constructor_body(is_async=is_async)),
            ),
        )

        if self._package.service is not None:
            service = self._context.ir.services[self._package.service]
            for endpoint in service.endpoints:
                endpoint_function_generator = EndpointFunctionGenerator(
                    context=self._context,
                    service=service,
                    endpoint=endpoint,
                    is_async=is_async,
                    client_wrapper_member_name=self._get_client_wrapper_member_name(),
                )
                generated_endpoint_function = endpoint_function_generator.generate()
                class_declaration.add_method(generated_endpoint_function.function)
                if (
                    not self._is_default_body_parameter_used
                    and generated_endpoint_function.is_default_body_parameter_used
                ):
                    self._is_default_body_parameter_used = True

        return class_declaration

    def _get_constructor_parameters(self, *, is_async: bool) -> List[RootClientConstructorParameter]:
        parameters: List[RootClientConstructorParameter] = []

        environments_config = self._context.ir.environments
        # If no environments, client should only provide base_url argument
        if environments_config is None: 
            parameters.append(
                RootClientConstructorParameter(
                    constructor_parameter_name=RootClientGenerator.BASE_URL_CONSTRUCTOR_PARAMETER_NAME,
                    type_hint=AST.TypeHint.str_(),
                    private_member_name=None,
                    initializer=None,
                )
            )
        # If single url environment present, client should provide both base_url and environment arguments
        elif environments_config.environments.get_as_union().type == "singleBaseUrl":
            parameters.append(
                RootClientConstructorParameter(
                    constructor_parameter_name=RootClientGenerator.BASE_URL_CONSTRUCTOR_PARAMETER_NAME,
                    type_hint=AST.TypeHint.optional(AST.TypeHint.str_()),
                    private_member_name=None,
                    initializer=AST.Expression("None"),
                    exclude_from_wrapper_construction=True
                ))
            parameters.append(RootClientConstructorParameter(
                    constructor_parameter_name=RootClientGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME,
                    type_hint=AST.TypeHint(self._context.get_reference_to_environments_class())
                    if environments_config.default_environment is None
                    else AST.TypeHint.optional(AST.TypeHint(self._context.get_reference_to_environments_class())),
                    private_member_name=None,
                    initializer=AST.Expression(
                        environments_config.environments.visit(
                            single_base_url=lambda single_base_url_environments: SingleBaseUrlEnvironmentGenerator(
                                context=self._context, environments=single_base_url_environments
                            ).get_reference_to_default_environment(),
                            multiple_base_urls=lambda multiple_base_urls_environments: MultipleBaseUrlsEnvironmentGenerator(
                                context=self._context, environments=multiple_base_urls_environments
                            ).get_reference_to_default_environment(),
                        )
                    )
                    if environments_config.default_environment is not None
                    else None,
                    exclude_from_wrapper_construction=True
                ),
            )
        # If mutli url environment present, client should provide only environment argument
        elif environments_config.environments.get_as_union().type == "multipleBaseUrls":
            parameters.append(RootClientConstructorParameter(
                    constructor_parameter_name=RootClientGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME,
                    type_hint=AST.TypeHint(self._context.get_reference_to_environments_class())
                    if environments_config.default_environment is None
                    else AST.TypeHint.optional(AST.TypeHint(self._context.get_reference_to_environments_class())),
                    private_member_name=None,
                    initializer=AST.Expression(
                        environments_config.environments.visit(
                            single_base_url=lambda single_base_url_environments: SingleBaseUrlEnvironmentGenerator(
                                context=self._context, environments=single_base_url_environments
                            ).get_reference_to_default_environment(),
                            multiple_base_urls=lambda multiple_base_urls_environments: MultipleBaseUrlsEnvironmentGenerator(
                                context=self._context, environments=multiple_base_urls_environments
                            ).get_reference_to_default_environment(),
                        )
                    )
                    if environments_config.default_environment is not None
                    else None,
                ),
            )

        client_wrapper_generator = ClientWrapperGenerator(context=self._context)
        for param in client_wrapper_generator._get_constructor_info().constructor_parameters:
            parameters.append(
                RootClientConstructorParameter(
                    constructor_parameter_name=param.constructor_parameter_name,
                    type_hint=param.type_hint,
                )
            )

        parameters.append(
            RootClientConstructorParameter(
                constructor_parameter_name=self._timeout_constructor_parameter_name,
                type_hint=AST.TypeHint.optional(AST.TypeHint.float_()),
                initializer=AST.Expression(f"{self._context.custom_config.timeout_in_seconds}")
                if isinstance(self._context.custom_config.timeout_in_seconds, int)
                else AST.Expression(AST.TypeHint.none()),
            )
        )
        return parameters

    def _environment_is_enum(self) -> bool:
        return self._context.ir.environments is not None

    def _get_write_constructor_body(self, *, is_async: bool) -> CodeWriterFunction:
        def _write_constructor_body(writer: AST.NodeWriter) -> None:
            client_wrapper_generator = ClientWrapperGenerator(context=self._context)
            client_wrapper_constructor_kwargs = []

            environments_config = self._context.ir.environments
            # If no environments, client should only provide base_url argument
            if environments_config is None: 
                client_wrapper_constructor_kwargs.append(
                    (
                        ClientWrapperGenerator.BASE_URL_PARAMETER_NAME,
                        AST.Expression(RootClientGenerator.BASE_URL_CONSTRUCTOR_PARAMETER_NAME),
                    )
                )
            elif environments_config.environments.get_as_union().type == "singleBaseUrl":
                writer.write_line(f"if {RootClientGenerator.BASE_URL_CONSTRUCTOR_PARAMETER_NAME} is None and {RootClientGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME} is None:")
                with writer.indent(): 
                    writer.write_line('raise new Exception("Please pass in either base_url or environment to construct the client")')
                client_wrapper_constructor_kwargs.append(
                    (
                        ClientWrapperGenerator.BASE_URL_PARAMETER_NAME,
                        AST.Expression(f"{RootClientGenerator.BASE_URL_CONSTRUCTOR_PARAMETER_NAME} if {RootClientGenerator.BASE_URL_CONSTRUCTOR_PARAMETER_NAME} is not None else {RootClientGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME}.value"),
                    )
                )
            elif environments_config.environments.get_as_union().type == "multipleBaseUrls":
                client_wrapper_constructor_kwargs.append(
                    (
                        ClientWrapperGenerator.ENVIRONMENT_PARAMETER_NAME,
                        AST.Expression(RootClientGenerator.ENVIRONMENT_CONSTRUCTOR_PARAMETER_NAME),
                    )
                )
            
            for wrapper_param in client_wrapper_generator._get_constructor_info().constructor_parameters:
                client_wrapper_constructor_kwargs.append(
                    (
                        wrapper_param.constructor_parameter_name,
                        AST.Expression(wrapper_param.constructor_parameter_name),
                    )
                )
            client_wrapper_constructor_kwargs.append(
                (
                    ClientWrapperGenerator.HTTPX_CLIENT_MEMBER_NAME,
                    AST.Expression(
                        AST.ClassInstantiation(
                            HttpX.ASYNC_CLIENT if is_async else HttpX.CLIENT,
                            kwargs=[
                                (
                                    "timeout",
                                    AST.Expression(f"{self._timeout_constructor_parameter_name}"),
                                )
                            ],
                        )
                    ),
                )
            )
            for param in self._get_constructor_parameters(is_async=is_async):
                if param.private_member_name is not None:
                    writer.write_line(f"self.{param.private_member_name} = {param.constructor_parameter_name}")
            writer.write(f"self.{self._get_client_wrapper_member_name()} = ")
            writer.write_node(
                AST.ClassInstantiation(
                    self._context.core_utilities.get_reference_to_client_wrapper(is_async=is_async),
                    kwargs=client_wrapper_constructor_kwargs,
                )
            )
            writer.write_newline_if_last_line_not()
            for subpackage_id in self._package.subpackages:
                subpackage = self._context.ir.subpackages[subpackage_id]
                if subpackage.has_endpoints_in_tree:
                    writer.write_node(AST.Expression(f"self.{subpackage.name.snake_case.safe_name} = "))
                    client_wrapper_constructor_kwargs = [
                        (param.constructor_parameter_name, AST.Expression(f"self.{param.constructor_parameter_name}"))
                        for param in self._get_constructor_parameters(is_async=is_async)
                    ]
                    client_wrapper_constructor_kwargs.append(
                        (
                            "client_wrapper",
                            AST.Expression(f"self.{self._get_client_wrapper_member_name()}"),
                        ),
                    )
                    writer.write_node(
                        AST.ClassInstantiation(
                            class_=self._context.get_reference_to_async_subpackage_service(subpackage_id)
                            if is_async
                            else self._context.get_reference_to_subpackage_service(subpackage_id),
                            kwargs=[
                                (
                                    "client_wrapper",
                                    AST.Expression(f"self.{self._get_client_wrapper_member_name()}"),
                                ),
                            ],
                        )
                    )
                    writer.write_line()

        return _write_constructor_body

    def _write_default_param(self, writer: AST.NodeWriter) -> None:
        writer.write_line("# this is used as the default value for optional parameters")
        writer.write(f"{DEFAULT_BODY_PARAMETER_VALUE} = ")
        writer.write_node(AST.TypeHint.cast(AST.TypeHint.any(), AST.Expression("...")))
        writer.write_newline_if_last_line_not()

    def _get_client_wrapper_constructor_parameter_name(self, params: typing.List[RootClientConstructorParameter]) -> str:
        for param in params:
            if param.constructor_parameter_name == "client_wrapper":
                return "_client_wrapper"
        return "client_wrapper"

    def _get_client_wrapper_member_name(self) -> str:
        return "_client_wrapper"

    def _get_timeout_constructor_parameter_name(self, params: typing.List[str]) -> str:
        for param in params:
            if param == "timeout":
                return "_timeout"
        return "timeout"
