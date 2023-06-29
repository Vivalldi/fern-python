import typing
import fern.ir.resources as ir_types
from typing import Optional, List

from dataclasses import dataclass
from fern_python.codegen import AST, SourceFile
from ..context.sdk_generator_context import SdkGeneratorContext


@dataclass
class ConstructorParameter:
    constructor_parameter_name: str
    type_hint: AST.TypeHint
    private_member_name: str

@dataclass
class ConstructorInfo:
    constructor_parameters: List[ConstructorParameter] 
    getter_methods: List[AST.FunctionDeclaration]

class ClientWrapperGenerator:
    BASE_CLIENT_WRAPPER_CLASS_NAME = "BaseClientWrapper"
    SYNC_CLIENT_WRAPPER_CLASS_NAME = "SyncClientWrapper"
    ASYNC_CLIENT_WRAPPER_CLASS_NAME = "AsyncClientWrapper"

    GET_HEADERS_METHOD_NAME = "get_headers"
    
    HTTPX_CLIENT_MEMBER_NAME = "httpx_client"

    TOKEN_CONSTRUCTOR_PARAMETER_NAME = "token"
    TOKEN_MEMBER_NAME = "_token"

    STRING_OR_SUPPLIER_TYPE_HINT = AST.TypeHint.callable(
        [AST.TypeHint.str_()],
        AST.TypeHint.callable(parameters=[], return_type=AST.TypeHint.str_())
    )

    def __init__(
        self,
        *,
        context: SdkGeneratorContext,
    ):
        self._context = context

    def generate(self, source_file: SourceFile) -> None:
        class_declaration = self._create_class_declaration(is_async=False)
        # source_file.add_class_declaration(
        #     declaration=class_declaration,
        #     should_export=False,
        # )
        # source_file.add_class_declaration(
        #     declaration=self._create_class_declaration(is_async=True),
        #     should_export=False,
        # )
        pass
    
    def _create_base_client_wrapper_class_declaration() -> None:
        self._get_constructor_parameters()
        pass

    def _create_sync_client_wrapper_class_declaration() -> None:
        pass

    def _create_async_client_wrapper_class_declaration() -> None:
        pass

    def _get_constructor_parameters(self) -> ConstructorInfo:
        parameters: List[ConstructorParameter] = []
        getter_methods: List[AST.FunctionDeclaration] = []

        # TODO(dsinghvi): Support suppliers for global headers
        for header in self._context.ir.headers:
            parameters.append(
                ConstructorParameter(
                    constructor_parameter_name=self._get_header_constructor_parameter_name(header),
                    private_member_name=self._get_header_private_member_name(header),
                    type_hint=self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                        header.value_type
                    ),
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
                )
            )
            getter_methods.append(AST.FunctionDeclaration(
                name=f"_get_{ClientWrapperGenerator.TOKEN_CONSTRUCTOR_PARAMETER_NAME}",
                signature=AST.FunctionSignature(
                    parameters=[],
                    return_type=AST.TypeHint.str_(),
                ),
                body=AST.CodeWriter(self._get_getter_body_writer(ClientWrapperGenerator.TOKEN_MEMBER_NAME)),
            ))

        basic_auth_scheme = self._get_basic_auth_scheme()
        if basic_auth_scheme is not None:
            username_constructor_parameter = ConstructorParameter(
                constructor_parameter_name=self._get_username_constructor_parameter_name(basic_auth_scheme),
                private_member_name=self._get_username_member_name(basic_auth_scheme),
                type_hint=ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT
                if self._context.ir.sdk_config.is_auth_mandatory
                else AST.TypeHint.optional(ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT),
            )
            password_constructor_parameter = ConstructorParameter(
                constructor_parameter_name=self._get_password_constructor_parameter_name(basic_auth_scheme),
                private_member_name=self._get_password_member_name(basic_auth_scheme),
                type_hint=ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT
                if self._context.ir.sdk_config.is_auth_mandatory
                else AST.TypeHint.optional(ClientWrapperGenerator.STRING_OR_SUPPLIER_TYPE_HINT),
            )
            parameters.extend(
                [
                    username_constructor_parameter,
                    password_constructor_parameter,
                ]
            )
            getter_methods.append(AST.FunctionDeclaration(
                name=f"_get_{username_constructor_parameter.private_member_name}",
                signature=AST.FunctionSignature(
                    parameters=[],
                    return_type=AST.TypeHint.str_(),
                ),
                body=AST.CodeWriter(self._get_getter_body_writer(username_constructor_parameter.private_member_name)),
            ))
            getter_methods.append(AST.FunctionDeclaration(
                name=f"_get_{password_constructor_parameter.private_member_name}",
                signature=AST.FunctionSignature(
                    parameters=[],
                    return_type=AST.TypeHint.str_(),
                ),
                body=AST.CodeWriter(self._get_getter_body_writer(password_constructor_parameter.private_member_name)),
            ))

        return ConstructorInfo(constructor_parameters=parameters, getter_methods=getter_methods)
    
    def _get_getter_body_writer(self, member_name: str) -> AST.CodeWriterFunction: 
        def _write_getter_body(writer: AST.NodeWriter) -> None:
            writer.write_line(f"if isinstance(self.{member_name}, str):")
            with writer.indent():
                writer.write_line(f"return self.{member_name}")
            writer.write_line(f"else:")
            with writer.indent():
                writer.write_line(f"return self.{member_name}()")
        
        return _write_getter_body


    def _has_bearer_auth(self) -> bool:
        for scheme in self._context.ir.auth.schemes:
            if scheme.get_as_union().type == "bearer":
                return True
        return False

    def _get_basic_auth_scheme(self) -> Optional[ir_types.BasicAuthScheme]:
        for scheme in self._context.ir.auth.schemes:
            scheme_as_union = scheme.get_as_union()
            if scheme_as_union.type == "basic":
                return scheme_as_union
        return None
    
    def _get_username_constructor_parameter_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return basic_auth_scheme.username.snake_case.unsafe_name

    def _get_username_member_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return f"_{self._get_username_constructor_parameter_name(basic_auth_scheme)}"

    def _get_password_constructor_parameter_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return basic_auth_scheme.password.snake_case.unsafe_name

    def _get_password_member_name(self, basic_auth_scheme: ir_types.BasicAuthScheme) -> str:
        return f"_{self._get_password_constructor_parameter_name(basic_auth_scheme)}"

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
