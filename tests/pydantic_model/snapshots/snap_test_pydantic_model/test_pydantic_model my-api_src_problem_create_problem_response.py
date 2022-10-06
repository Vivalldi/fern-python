from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.problem_id import ProblemId
from .create_problem_error import CreateProblemError

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def success(self, value: ProblemId) -> CreateProblemResponse:
        return CreateProblemResponse(__root__=_CreateProblemResponse.Success(type="success", value=value))

    def error(self, value: CreateProblemError) -> CreateProblemResponse:
        return CreateProblemResponse(__root__=_CreateProblemResponse.Error(type="error", value=value))


class CreateProblemResponse(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]:
        return self.__root__

    def visit(
        self, success: typing.Callable[[ProblemId], T_Result], error: typing.Callable[[CreateProblemError], T_Result]
    ) -> T_Result:
        if self.__root__.type == "success":
            return success(self.__root__.success)
        if self.__root__.type == "error":
            return error(self.__root__.error)

    __root__: typing_extensions.Annotated[
        typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error], pydantic.Field(discriminator="type")
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error], values.get("__root__")
        )
        for validator in CreateProblemResponse.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]],
                    typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error],
                ]
            ]
        ] = []

        @classmethod
        def add_validator(
            cls,
            validator: typing.Callable[
                [typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error]],
                typing.Union[_CreateProblemResponse.Success, _CreateProblemResponse.Error],
            ],
        ) -> None:
            cls._validators.append(validator)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True


class _CreateProblemResponse:
    class Success(pydantic.BaseModel):
        type: typing_extensions.Literal["success"]
        value: ProblemId

        class Config:
            frozen = True

    class Error(pydantic.BaseModel):
        type: typing_extensions.Literal["error"]
        value: CreateProblemError

        class Config:
            frozen = True


CreateProblemResponse.update_forward_refs()
