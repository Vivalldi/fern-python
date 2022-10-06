from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .compile_error import CompileError
from .internal_error import InternalError
from .runtime_error import RuntimeError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def compile_error(self, value: CompileError) -> ErrorInfo:
        return ErrorInfo(__root__=_ErrorInfo.CompileError(**dict(value), type="compileError"))

    def runtime_error(self, value: RuntimeError) -> ErrorInfo:
        return ErrorInfo(__root__=_ErrorInfo.RuntimeError(**dict(value), type="runtimeError"))

    def internal_error(self, value: InternalError) -> ErrorInfo:
        return ErrorInfo(__root__=_ErrorInfo.InternalError(**dict(value), type="internalError"))


class ErrorInfo(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError]:
        return self.__root__

    def visit(
        self,
        compile_error: typing.Callable[[CompileError], T_Result],
        runtime_error: typing.Callable[[RuntimeError], T_Result],
        internal_error: typing.Callable[[InternalError], T_Result],
    ) -> T_Result:
        if self.__root__.type == "compileError":
            return compile_error(self.__root__)
        if self.__root__.type == "runtimeError":
            return runtime_error(self.__root__)
        if self.__root__.type == "internalError":
            return internal_error(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_ErrorInfo.CompileError, _ErrorInfo.RuntimeError, _ErrorInfo.InternalError],
        pydantic.Field(discriminator="type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True


class _ErrorInfo:
    class CompileError(CompileError):
        type: typing_extensions.Literal["compileError"]

        class Config:
            frozen = True

    class RuntimeError(RuntimeError):
        type: typing_extensions.Literal["runtimeError"]

        class Config:
            frozen = True

    class InternalError(InternalError):
        type: typing_extensions.Literal["internalError"]

        class Config:
            frozen = True


ErrorInfo.update_forward_refs()
