# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class TestCaseHiddenGrade(pydantic.BaseModel):
    passed: bool

    class Partial(typing_extensions.TypedDict):
        passed: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseHiddenGrade.Validators.root
            def validate(values: TestCaseHiddenGrade.Partial) -> TestCaseHiddenGrade.Partial:
                ...

            @TestCaseHiddenGrade.Validators.field("passed")
            def validate_passed(passed: bool, values: TestCaseHiddenGrade.Partial) -> bool:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestCaseHiddenGrade.Partial], TestCaseHiddenGrade.Partial]]
        ] = []
        _passed_validators: typing.ClassVar[typing.List[TestCaseHiddenGrade.Validators.PassedValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestCaseHiddenGrade.Partial], TestCaseHiddenGrade.Partial]
        ) -> typing.Callable[[TestCaseHiddenGrade.Partial], TestCaseHiddenGrade.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"]
        ) -> typing.Callable[
            [TestCaseHiddenGrade.Validators.PassedValidator], TestCaseHiddenGrade.Validators.PassedValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "passed":
                    cls._passed_validators.append(validator)
                return validator

            return decorator

        class PassedValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: TestCaseHiddenGrade.Partial) -> bool:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestCaseHiddenGrade.Partial) -> TestCaseHiddenGrade.Partial:
        for validator in TestCaseHiddenGrade.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("passed")
    def _validate_passed(cls, v: bool, values: TestCaseHiddenGrade.Partial) -> bool:
        for validator in TestCaseHiddenGrade.Validators._passed_validators:
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
