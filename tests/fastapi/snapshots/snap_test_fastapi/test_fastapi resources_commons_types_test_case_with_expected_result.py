# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case import TestCase
from .variable_value import VariableValue


class TestCaseWithExpectedResult(pydantic.BaseModel):
    test_case: TestCase = pydantic.Field(alias="testCase")
    expected_result: VariableValue = pydantic.Field(alias="expectedResult")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseWithExpectedResult.Validators.field("test_case")
            def validate_test_case(v: TestCase, values: TestCaseWithExpectedResult.Partial) -> TestCase:
                ...

            @TestCaseWithExpectedResult.Validators.field("expected_result")
            def validate_expected_result(v: VariableValue, values: TestCaseWithExpectedResult.Partial) -> VariableValue:
                ...
        """

        _test_case_validators: typing.ClassVar[
            typing.List[TestCaseWithExpectedResult.Validators.TestCaseValidator]
        ] = []
        _expected_result_validators: typing.ClassVar[
            typing.List[TestCaseWithExpectedResult.Validators.ExpectedResultValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case"]
        ) -> typing.Callable[
            [TestCaseWithExpectedResult.Validators.TestCaseValidator],
            TestCaseWithExpectedResult.Validators.TestCaseValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expected_result"]
        ) -> typing.Callable[
            [TestCaseWithExpectedResult.Validators.ExpectedResultValidator],
            TestCaseWithExpectedResult.Validators.ExpectedResultValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "test_case":
                    cls._test_case_validators.append(validator)
                if field_name == "expected_result":
                    cls._expected_result_validators.append(validator)
                return validator

            return decorator

        class TestCaseValidator(typing_extensions.Protocol):
            def __call__(self, v: TestCase, *, values: TestCaseWithExpectedResult.Partial) -> TestCase:
                ...

        class ExpectedResultValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableValue, *, values: TestCaseWithExpectedResult.Partial) -> VariableValue:
                ...

    @pydantic.validator("test_case")
    def _validate_test_case(cls, v: TestCase, values: TestCaseWithExpectedResult.Partial) -> TestCase:
        for validator in TestCaseWithExpectedResult.Validators._test_case_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("expected_result")
    def _validate_expected_result(cls, v: VariableValue, values: TestCaseWithExpectedResult.Partial) -> VariableValue:
        for validator in TestCaseWithExpectedResult.Validators._expected_result_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        test_case: typing_extensions.NotRequired[TestCase]
        expected_result: typing_extensions.NotRequired[VariableValue]

    class Config:
        frozen = True
        allow_population_by_field_name = True
