# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.variable_value import VariableValue
from .actual_result import ActualResult


class TestCaseResult(pydantic.BaseModel):
    expected_result: VariableValue = pydantic.Field(alias="expectedResult")
    actual_result: ActualResult = pydantic.Field(alias="actualResult")
    passed: bool

    class Partial(typing_extensions.TypedDict):
        expected_result: typing_extensions.NotRequired[VariableValue]
        actual_result: typing_extensions.NotRequired[ActualResult]
        passed: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseResult.Validators.root
            def validate(values: TestCaseResult.Partial) -> TestCaseResult.Partial:
                ...

            @TestCaseResult.Validators.field("expected_result")
            def validate_expected_result(expected_result: VariableValue, values: TestCaseResult.Partial) -> VariableValue:
                ...

            @TestCaseResult.Validators.field("actual_result")
            def validate_actual_result(actual_result: ActualResult, values: TestCaseResult.Partial) -> ActualResult:
                ...

            @TestCaseResult.Validators.field("passed")
            def validate_passed(passed: bool, values: TestCaseResult.Partial) -> bool:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[TestCaseResult.Partial], TestCaseResult.Partial]]
        ] = []
        _expected_result_validators: typing.ClassVar[
            typing.List[TestCaseResult.Validators.ExpectedResultValidator]
        ] = []
        _actual_result_validators: typing.ClassVar[typing.List[TestCaseResult.Validators.ActualResultValidator]] = []
        _passed_validators: typing.ClassVar[typing.List[TestCaseResult.Validators.PassedValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[TestCaseResult.Partial], TestCaseResult.Partial]
        ) -> typing.Callable[[TestCaseResult.Partial], TestCaseResult.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_result"]
        ) -> typing.Callable[
            [TestCaseResult.Validators.ExpectedResultValidator], TestCaseResult.Validators.ExpectedResultValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_result"]
        ) -> typing.Callable[
            [TestCaseResult.Validators.ActualResultValidator], TestCaseResult.Validators.ActualResultValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"]
        ) -> typing.Callable[[TestCaseResult.Validators.PassedValidator], TestCaseResult.Validators.PassedValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_result":
                    cls._expected_result_validators.append(validator)
                if field_name == "actual_result":
                    cls._actual_result_validators.append(validator)
                if field_name == "passed":
                    cls._passed_validators.append(validator)
                return validator

            return decorator

        class ExpectedResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableValue, __values: TestCaseResult.Partial) -> VariableValue:
                ...

        class ActualResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: ActualResult, __values: TestCaseResult.Partial) -> ActualResult:
                ...

        class PassedValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: TestCaseResult.Partial) -> bool:
                ...

    @pydantic.root_validator
    def _validate(cls, values: TestCaseResult.Partial) -> TestCaseResult.Partial:
        for validator in TestCaseResult.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_result")
    def _validate_expected_result(cls, v: VariableValue, values: TestCaseResult.Partial) -> VariableValue:
        for validator in TestCaseResult.Validators._expected_result_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result")
    def _validate_actual_result(cls, v: ActualResult, values: TestCaseResult.Partial) -> ActualResult:
        for validator in TestCaseResult.Validators._actual_result_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("passed")
    def _validate_passed(cls, v: bool, values: TestCaseResult.Partial) -> bool:
        for validator in TestCaseResult.Validators._passed_validators:
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
        extra = pydantic.Extra.forbid
