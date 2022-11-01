# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class UpdateProblemResponse(pydantic.BaseModel):
    problem_version: int = pydantic.Field(alias="problemVersion")

    class Partial(typing_extensions.TypedDict):
        problem_version: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @UpdateProblemResponse.Validators.root
            def validate(values: UpdateProblemResponse.Partial) -> UpdateProblemResponse.Partial:
                ...

            @UpdateProblemResponse.Validators.field("problem_version")
            def validate_problem_version(problem_version: int, values: UpdateProblemResponse.Partial) -> int:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[UpdateProblemResponse.Partial], UpdateProblemResponse.Partial]]
        ] = []
        _problem_version_validators: typing.ClassVar[
            typing.List[UpdateProblemResponse.Validators.ProblemVersionValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[UpdateProblemResponse.Partial], UpdateProblemResponse.Partial]
        ) -> typing.Callable[[UpdateProblemResponse.Partial], UpdateProblemResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"]
        ) -> typing.Callable[
            [UpdateProblemResponse.Validators.ProblemVersionValidator],
            UpdateProblemResponse.Validators.ProblemVersionValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_version":
                    cls._problem_version_validators.append(validator)
                return validator

            return decorator

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: UpdateProblemResponse.Partial) -> int:
                ...

    @pydantic.root_validator
    def _validate(cls, values: UpdateProblemResponse.Partial) -> UpdateProblemResponse.Partial:
        for validator in UpdateProblemResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_version")
    def _validate_problem_version(cls, v: int, values: UpdateProblemResponse.Partial) -> int:
        for validator in UpdateProblemResponse.Validators._problem_version_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
