import typing
from dataclasses import dataclass
from typing import List, Optional

import fern.ir.resources as ir_types

from fern_python.codegen import AST, SourceFile
from fern_python.codegen.ast.nodes.code_writer.code_writer import CodeWriterFunction
from fern_python.external_dependencies import httpx

from ..context.sdk_generator_context import SdkGeneratorContext


@dataclass
class ConstructorParameter:
    constructor_parameter_name: str
    type_hint: AST.TypeHint
    private_member_name: str
    getter_method: typing.Optional[AST.FunctionDeclaration] = None
    header_key: typing.Optional[str] = None
    header_prefix: typing.Optional[str] = None
    is_basic: bool = False


@dataclass
class ConstructorInfo:
    constructor_parameters: List[ConstructorParameter]


class ClientWrapperGenerator:
    AUTHORIZATION_HEADER = "AUTHORIZATION"
    BEARER_AUTH_PREFIX = "Bearer"

    BASE_CLIENT_WRAPPER_CLASS_NAME = "BaseClientWrapper"
    SYNC_CLIENT_WRAPPER_CLASS_NAME = "SyncClientWrapper"
    ASYNC_CLIENT_WRAPPER_CLASS_NAME = "AsyncClientWrapper"

    GET_HEADERS_METHOD_NAME = "get_headers"

    HTTPX_CLIENT_MEMBER_NAME = "httpx_client"

    TOKEN_CONSTRUCTOR_PARAMETER_NAME = "token"
    TOKEN_MEMBER_NAME = "_token"

    STRING_OR_SUPPLIER_TYPE_HINT = AST.TypeHint.callable(
        [AST.TypeHint.str_()], AST.TypeHint.callable(parameters=[], return_type=AST.TypeHint.str_())
    )

    def __init__(
        self,
        *,
        context: SdkGeneratorContext,
    ):
        self._context = context

    def generate(self, source_file: SourceFile) -> None:
        constructor_info = self._get_constructor_info()
        source_file.add_class_declaration(
            declaration=self._create_base_client_wrapper_class_declaration(constructor_info=constructor_info),
            should_export=True,
        )
        source_file.add_class_declaration(
            declaration=self._create_sync_client_wrapper_class_declaration(constructor_info=constructor_info),
            should_export=True,
        )
        source_file.add_class_declaration(
            declaration=self._create_async_client_wrapper_class_declaration(constructor_info=constructor_info),
            should_export=True,
        )

    def _create_base_client_wrapper_class_declaration(
        self, *, constructor_info: ConstructorInfo
    ) -> AST.ClassDeclaration:
        named_parameters = self._get_named_parameters(constructor_parameters=constructor_info.constructor_parameters)

        class_declaration = AST.ClassDeclaration(
            name=ClientWrapperGenerator.BASE_CLIENT_WRAPPER_CLASS_NAME,
            constructor=AST.ClassConstructor(
                signature=AST.FunctionSignature(
                    named_parameters=named_parameters,
                ),
                body=AST.CodeWriter(
                    self._get_write_constructor_body(constructor_parameters=constructor_info.constructor_parameters)
                ),
            ),
        )

        for constructor_param in constructor_info.constructor_parameters:
            if constructor_param.getter_method is not None:
                class_declaration.add_method(constructor_param.getter_method)

        class_declaration.add_method(
            AST.FunctionDeclaration(
                name=ClientWrapperGenerator.GET_HEADERS_METHOD_NAME,
                signature=AST.FunctionSignature(
                    return_type=AST.TypeHint.dict(AST.TypeHint.str_(), AST.TypeHint.str_())
                ),
                body=AST.CodeWriter(
                    self._get_write_constructor_body(constructor_parameters=constructor_info.constructor_parameters)
                ),
            )
        )

        return class_declaration

    def _create_sync_client_wrapper_class_declaration(
        self, *, constructor_info: ConstructorInfo
    ) -> AST.ClassDeclaration:
        named_parameters = self._get_named_parameters(constructor_parameters=constructor_info.constructor_parameters)

        named_parameters.append(
            AST.NamedFunctionParameter(
                name=ClientWrapperGenerator.HTTPX_CLIENT_MEMBER_NAME,
                type_hint=AST.TypeHint(httpx.HttpX.CLIENT),
            )
        )

        class_declaration = AST.ClassDeclaration(
            name=ClientWrapperGenerator.SYNC_CLIENT_WRAPPER_CLASS_NAME,
            extends=[AST.ClassReference((ClientWrapperGenerator.BASE_CLIENT_WRAPPER_CLASS_NAME,))],
            constructor=AST.ClassConstructor(
                signature=AST.FunctionSignature(
                    named_parameters=named_parameters,
                ),
                body=AST.CodeWriter(
                    self._get_write_derived_client_wrapper_constructor_body(
                        constructor_parameters=constructor_info.constructor_parameters
                    )
                ),
            ),
        )

        return class_declaration

    def _create_async_client_wrapper_class_declaration(
        self, *, constructor_info: ConstructorInfo
    ) -> AST.ClassDeclaration:
        named_parameters = self._get_named_parameters(constructor_parameters=constructor_info.constructor_parameters)

        named_parameters.append(
            AST.NamedFunctionParameter(
                name=ClientWrapperGenerator.HTTPX_CLIENT_MEMBER_NAME,
                type_hint=AST.TypeHint(httpx.HttpX.ASYNC_CLIENT),
            )
        )

        class_declaration = AST.ClassDeclaration(
            name=ClientWrapperGenerator.ASYNC_CLIENT_WRAPPER_CLASS_NAME,
            extends=[AST.ClassReference((ClientWrapperGenerator.BASE_CLIENT_WRAPPER_CLASS_NAME,))],
            constructor=AST.ClassConstructor(
                signature=AST.FunctionSignature(
                    named_parameters=named_parameters,
                ),
                body=AST.CodeWriter(
                    self._get_write_derived_client_wrapper_constructor_body(
                        constructor_parameters=constructor_info.constructor_parameters
                    )
                ),
            ),
        )

        return class_declaration

    def _get_write_derived_client_wrapper_constructor_body(
        self, *, constructor_parameters: List[ConstructorParameter]
    ) -> CodeWriterFunction:
        def _write_derived_client_wrapper_constructor_body(writer: AST.NodeWriter) -> None:
            writer.write_line(
                f"super().__init__({', '.join([param.constructor_parameter_name for param in constructor_parameters])})"
            )
            writer.write_line(
                f"self.{ClientWrapperGenerator.HTTPX_CLIENT_MEMBER_NAME} = {ClientWrapperGenerator.HTTPX_CLIENT_MEMBER_NAME}"
            )

        return _write_derived_client_wrapper_constructor_body

    def _get_named_parameters(
        self, *, constructor_parameters: List[ConstructorParameter]
    ) -> typing.List[AST.NamedFunctionParameter]:
        return [
            AST.NamedFunctionParameter(
                name=param.constructor_parameter_name,
                type_hint=param.type_hint,
            )
            for param in constructor_parameters
        ]

    def _get_write_get_headers_body(self, *, constructor_parameters: List[ConstructorParameter]) -> CodeWriterFunction:
        def _write_get_headers_body(writer: AST.NodeWriter) -> None:
            writer.write_line("return {")
            basic_auth_scheme = self._get_basic_auth_scheme()
            if basic_auth_scheme is not None:
                writer.write(f'"{ClientWrapperGenerator.AUTHORIZATION_HEADER}": ')
                writer.write_node(
                    AST.ClassInstantiation(
                        class_=httpx.HttpX.BASIC_AUTH,
                        args=[
                            AST.Expression(f"self.{self._get_username_getter_name(basic_auth_scheme)}()"),
                            AST.Expression(f"self.{self._get_password_getter_name(basic_auth_scheme)}()"),
                        ],
                    )
                )
                writer.write("._auth_header,")
                writer.write_newline_if_last_line_not()
            for param in constructor_parameters:
                if param.is_basic:
                    continue
                if param.header_key is not None:
                    if param.getter_method is not None:
                        writer.write_line(
                            f"\"{param.header_key}\": {param.header_prefix if param.header_prefix is not None else ''} self.{param.getter_method.name}(),"
                        )
                    elif param.private_member_name is not None:
                        writer.write_line(
                            f"\"{param.header_key}\": {param.header_prefix if param.header_prefix is not None else ''} self.{param.private_member_name},"
                        )
            writer.write_line("}")

        return _write_get_headers_body

    def _get_write_constructor_body(self, *, constructor_parameters: List[ConstructorParameter]) -> CodeWriterFunction:
        def _write_constructor_body(writer: AST.NodeWriter) -> None:
            for param in constructor_parameters:
                if param.private_member_name is not None:
                    writer.write_line(f"self.{param.private_member_name} = {param.constructor_parameter_name}")

        return _write_constructor_body

    def _get_constructor_info(self) -> ConstructorInfo:
        parameters: List[ConstructorParameter] = []

        # TODO(dsinghvi): Support suppliers for global headers
        for header in self._context.ir.headers:
            parameters.append(
                ConstructorParameter(
                    constructor_parameter_name=self._get_header_constructor_parameter_name(header),
                    private_member_name=self._get_header_private_member_name(header),
                    type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                        header.value_type
                    ),
                    header_key=header.name.wire_value,
                )
            )

        # TODO(dsinghvi): Support suppliers for header auth schemes
        for header_auth_scheme in self._get_header_auth_schemes():
            parameters.append(
                ConstructorParameter(
                    constructor_parameter_name=self._get_auth_scheme_header_private_member_name(header_auth_scheme),
                    private_member_name=self._get_auth_scheme_header_private_member_name(header_auth_scheme),
                    type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                        header_auth_scheme.value_type
                    ),
                    header_key=header_auth_scheme.name.wire_value,
                    header_prefix=header_auth_scheme.prefix,
                )
            )

        if self._has_bearer_auth():
            parameters.append(
                ConstructorParameter(
                    constructor_parameter_name=ClientWrapperGenerator.TOKEN_CONSTRUCTOR_PARAMETER_NAME,
                    private_member_name=ClientWrapperGenerator.TOKEN_MEMBER_NAME,
                    type_hint=ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT
                    if self._context.ir.sdk_config.is_auth_mandatory
                    else AST.TypeHint.optional(ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT),
                    getter_method=AST.FunctionDeclaration(
                        name=f"_get_{ClientWrapperGenerator.TOKEN_CONSTRUCTOR_PARAMETER_NAME}",
                        signature=AST.FunctionSignature(
                            parameters=[],
                            return_type=AST.TypeHint.str_(),
                        ),
                        body=AST.CodeWriter(self._get_getter_body_writer(ClientWrapperGenerator.TOKEN_MEMBER_NAME)),
                    ),
                    header_key=ClientWrapperGenerator.AUTHORIZATION_HEADER,
                    header_prefix=ClientWrapperGenerator.BEARER_AUTH_PREFIX,
                )
            )

        basic_auth_scheme = self._get_basic_auth_scheme()
        if basic_auth_scheme is not None:
            username_constructor_parameter = ConstructorParameter(
                constructor_parameter_name=self._get_username_constructor_parameter_name(basic_auth_scheme),
                private_member_name=self._get_username_member_name(basic_auth_scheme),
                type_hint=ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT
                if self._context.ir.sdk_config.is_auth_mandatory
                else AST.TypeHint.optional(ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT),
                getter_method=AST.FunctionDeclaration(
                    name=self._get_username_getter_name(basic_auth_scheme),
                    signature=AST.FunctionSignature(
                        parameters=[],
                        return_type=AST.TypeHint.str_(),
                    ),
                    body=AST.CodeWriter(
                        self._get_getter_body_writer(self._get_username_member_name(basic_auth_scheme))
                    ),
                ),
                is_basic=True,
            )
            password_constructor_parameter = ConstructorParameter(
                constructor_parameter_name=self._get_password_constructor_parameter_name(basic_auth_scheme),
                private_member_name=self._get_password_member_name(basic_auth_scheme),
                type_hint=ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT
                if self._context.ir.sdk_config.is_auth_mandatory
                else AST.TypeHint.optional(ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT),
                getter_method=AST.FunctionDeclaration(
                    name=self._get_password_getter_name(basic_auth_scheme),
                    signature=AST.FunctionSignature(
                        parameters=[],
                        return_type=AST.TypeHint.str_(),
                    ),
                    body=AST.CodeWriter(
                        self._get_getter_body_writer(self._get_password_member_name(basic_auth_scheme))
                    ),
                ),
                is_basic=True,
            )
            parameters.extend(
                [
                    username_constructor_parameter,
                    password_constructor_parameter,
                ]
            )

        return ConstructorInfo(constructor_parameters=parameters)

    def _get_getter_body_writer(self, member_name: str) -> AST.CodeWriterFunction:
        def _write_getter_body(writer: AST.NodeWriter) -> None:
            writer.write_line(f"if isinstance(self.{member_name}, str):")
            with writer.indent():
                writer.write_line(f"return self.{member_name}")
            writer.write_line("else:")
            with writer.indent():
                writer.write_line(f"return self.{member_name}()")

        return _write_getter_body

    def _has_bearer_auth(self) -> bool:
        for scheme in self._context.ir.auth.schemes:
            if scheme.get_as_union().type == "bearer":
                return True
        return False

    def _has_basic_auth(self) -> bool:
        return self._get_basic_auth_scheme() is not None

    def _get_basic_auth_scheme(self) -> Optional[ir_types.BasicAuthScheme]:
        for scheme in self._context.ir.auth.schemes:
            scheme_as_union = scheme.get_as_union()
            if scheme_as_union.type == "basic":
                return scheme_as_union
        return None

    def _get_username_constructor_parameter_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return basic_auth_scheme.username.snake_case.safe_name

    def _get_username_getter_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return f"_get_{basic_auth_scheme.username.snake_case.unsafe_name}"

    def _get_username_member_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return f"_{basic_auth_scheme.username.snake_case.unsafe_name}"

    def _get_password_constructor_parameter_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return basic_auth_scheme.password.snake_case.safe_name

    def _get_password_getter_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return f"_get_{basic_auth_scheme.password.snake_case.unsafe_name}"

    def _get_password_member_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return f"_{basic_auth_scheme.password.snake_case.unsafe_name}"

    def _get_header_auth_schemes(self) -> List[ir_types.HeaderAuthScheme]:
        header_auth_schemes: List[ir_types.HeaderAuthScheme] = []
        for scheme in self._context.ir.auth.schemes:
            scheme_member = scheme.get_as_union()
            if scheme_member.type == "header":
                header_auth_schemes.append(scheme_member)
        return header_auth_schemes

    def _get_header_parameter_name(self, header: ir_types.HttpHeader) -> str:
        return header.name.name.snake_case.unsafe_name

    def _get_header_private_member_name(self, header: ir_types.HttpHeader) -> str:
        return "_" + header.name.name.snake_case.unsafe_name

    def _get_header_constructor_parameter_name(self, header: ir_types.HttpHeader) -> str:
        return header.name.name.snake_case.unsafe_name

    def _get_auth_scheme_header_constructor_parameter_name(self, header: ir_types.HeaderAuthScheme) -> str:
        return header.name.name.snake_case.unsafe_name

    def _get_auth_scheme_header_private_member_name(self, header: ir_types.HeaderAuthScheme) -> str:
        return header.name.name.snake_case.unsafe_name
