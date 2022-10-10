from functools import cached_property
from typing import List

import fern.ir.pydantic as ir_types

from fern_python.codegen import AST

from ..context import FastApiGeneratorContext
from ..external_dependencies import FastAPI
from .endpoint_parameters import (
    AuthEndpointParameter,
    EndpointParameter,
    PathEndpointParameter,
    QueryEndpointParameter,
    RequestEndpointParameter,
)


class EndpointGenerator:
    _INIT_ENDPOINT_ROUTER_ARG = "router"

    def __init__(self, *, endpoint: ir_types.services.HttpEndpoint, context: FastApiGeneratorContext):
        self._endpoint = endpoint
        self._context = context

        self._parameters: List[EndpointParameter] = []
        if endpoint.request.type_v_2 is not None:
            self._parameters.append(
                RequestEndpointParameter(
                    context=context,
                    request_type=endpoint.request.type_v_2,
                )
            )
        for path_parameter in endpoint.path_parameters:
            self._parameters.append(PathEndpointParameter(context=context, path_parameter=path_parameter))
        for query_parameter in endpoint.query_parameters:
            self._parameters.append(QueryEndpointParameter(context=context, query_parameter=query_parameter))
        if endpoint.auth:
            self._parameters.append(AuthEndpointParameter(context=context))

    def add_abstract_method_to_class(self, class_declaration: AST.ClassDeclaration) -> None:
        class_declaration.add_abstract_method(
            name=self._get_method_name(),
            signature=AST.FunctionSignature(
                named_parameters=[parameter.to_function_parameter() for parameter in self._parameters],
                return_type=self._return_type,
            ),
        )

    @cached_property
    def _return_type(self) -> AST.TypeHint:
        response_type = self._endpoint.response.type_v_2
        if response_type is None:
            return AST.TypeHint.none()
        return self._context.pydantic_generator_context.get_type_hint_for_type_reference(response_type)

    @cached_property
    def _endpoint_path(self) -> str:
        path = self._endpoint.path.head
        for i, part in enumerate(self._endpoint.path.parts):
            path_parameter = self._endpoint.path_parameters[i]
            path += "{" + PathEndpointParameter.get_variable_name_of_path_parameter(path_parameter) + "}"
            path += part.tail
        return path

    def add_init_method_to_class(self, class_declaration: AST.ClassDeclaration) -> None:
        class_declaration.add_method(
            decorator=AST.ClassMethodDecorator.CLASS_METHOD,
            declaration=AST.FunctionDeclaration(
                name=self._get_init_method_name(),
                signature=AST.FunctionSignature(
                    parameters=[
                        AST.FunctionParameter(
                            name=EndpointGenerator._INIT_ENDPOINT_ROUTER_ARG,
                            type_hint=AST.TypeHint(type=FastAPI.APIRouter.REFERENCE),
                        )
                    ],
                    return_type=AST.TypeHint.none(),
                ),
                body=AST.CodeWriter(self._write_init_body),
            ),
        )

    def _write_init_body(self, writer: AST.NodeWriter, reference_resolver: AST.ReferenceResolver) -> None:
        self._write_update_endpoint_signature(writer=writer, reference_resolver=reference_resolver)
        writer.write(f"cls.{self._get_method_name()} = ")
        writer.write(f"{EndpointGenerator._INIT_ENDPOINT_ROUTER_ARG}.")
        writer.write(convert_http_method_to_fastapi_method_name(self._endpoint.method))
        writer.write_line("(  # type: ignore")
        with writer.indent():
            writer.write_line(f'path="{self._endpoint_path}",')
            if self._endpoint.response.type_v_2 is not None:
                writer.write("response_model=")
                writer.write_node(self._return_type)
                writer.write_line(",")
        writer.write(f")(cls.{self._get_method_name()})")

    def _write_update_endpoint_signature(
        self, writer: AST.NodeWriter, reference_resolver: AST.ReferenceResolver
    ) -> None:
        ENDPOINT_FUNCTION_VARIABLE_NAME = "endpoint_function"
        writer.write(f"{ENDPOINT_FUNCTION_VARIABLE_NAME} = ")
        writer.write_node(
            AST.FunctionInvocation(
                function_definition=AST.Reference(
                    qualified_name_excluding_import=("signature",),
                    import_=AST.ReferenceImport(module=AST.Module.built_in("inspect")),
                )
            )
        )
        writer.write_line()

        NEW_PARAMETERS_VARIABLE_NAME = "new_parameters"
        writer.write(f"{NEW_PARAMETERS_VARIABLE_NAME}: ")
        writer.write_node(
            AST.TypeHint.list(
                AST.TypeHint(
                    type=AST.ClassReference(
                        qualified_name_excluding_import=("Parameter",),
                        import_=AST.ReferenceImport(module=AST.Module.built_in("inspect")),
                    )
                )
            )
        )
        writer.write_line(" = []")

        INDEX_VARIABLE_NAME = "index"
        PARAMETER_NAME_VARIABLE_NAME = "parameter_name"
        PARAMETER_VALUE_VARIABLE_NAME = "parameter"
        writer.write_line(
            f"for {INDEX_VARIABLE_NAME}, ({PARAMETER_NAME_VARIABLE_NAME}, {PARAMETER_VALUE_VARIABLE_NAME}) "
            + f"in enumerate({ENDPOINT_FUNCTION_VARIABLE_NAME}.parameters.items()):"
        )

        with writer.indent():
            writer.write_line(f"if {INDEX_VARIABLE_NAME} == 0:")
            with writer.indent():
                writer.write(
                    f"{NEW_PARAMETERS_VARIABLE_NAME}.append(" + f"{PARAMETER_VALUE_VARIABLE_NAME}.replace(default="
                )
                writer.write_node(node=FastAPI.Depends(dependency=AST.Expression("cls")))
                writer.write_line("))")
            for i, parameter in enumerate(self._parameters):
                writer.write_line(f'elif {PARAMETER_NAME_VARIABLE_NAME} == "{parameter.get_name()}":')
                with writer.indent():
                    writer.write(
                        f"{NEW_PARAMETERS_VARIABLE_NAME}.append(" + f"{PARAMETER_VALUE_VARIABLE_NAME}.replace(default="
                    )
                    writer.write_node(parameter.get_default())
                    writer.write_line("))")
            writer.write_line("else:")
            with writer.indent():
                writer.write_line(f"{NEW_PARAMETERS_VARIABLE_NAME}.append({PARAMETER_VALUE_VARIABLE_NAME})")

        writer.write_line(
            'setattr(cls, "__signature__", '
            + f"{ENDPOINT_FUNCTION_VARIABLE_NAME}.replace(parameters={NEW_PARAMETERS_VARIABLE_NAME}))"
        )

    def invoke_init_method(self, *, reference_to_fastapi_router: AST.Expression) -> AST.FunctionInvocation:
        return AST.FunctionInvocation(
            function_definition=AST.Reference(
                qualified_name_excluding_import=("cls", self._get_init_method_name()),
            ),
            kwargs=[(EndpointGenerator._INIT_ENDPOINT_ROUTER_ARG, reference_to_fastapi_router)],
        )

    def _get_method_name(self) -> str:
        return self._endpoint.name.camel_case

    def _get_init_method_name(self) -> str:
        return f"__init_{self._get_method_name()}"


def convert_http_method_to_fastapi_method_name(http_method: ir_types.services.HttpMethod) -> str:
    return http_method.visit(
        get=lambda: "get",
        post=lambda: "post",
        put=lambda: "put",
        patch=lambda: "patch",
        delete=lambda: "delete",
    )
