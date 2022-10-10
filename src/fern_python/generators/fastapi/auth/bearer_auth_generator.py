from fern_python.codegen import AST

from ..external_dependencies import FastAPI
from .abstract_auth_generator import AbstractAuthGenerator


class BearerAuthGenerator(AbstractAuthGenerator):
    def get_dependency(self) -> AST.Expression:
        return AST.Expression(
            AST.FunctionInvocation(
                function_definition=FastAPI.Depends,
                args=[AST.Expression(self._context.core_utilities.HTTPBearer())],
            )
        )

    def get_parsed_auth_type(self) -> AST.TypeHint:
        return AST.TypeHint(type=self._context.core_utilities.BearerToken())
