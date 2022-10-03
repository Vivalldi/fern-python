import typing

from ...commons.with_docs import WithDocs
from ...errors.declared_error_name import DeclaredErrorName


class ResponseError(WithDocs):
    error: DeclaredErrorName

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
