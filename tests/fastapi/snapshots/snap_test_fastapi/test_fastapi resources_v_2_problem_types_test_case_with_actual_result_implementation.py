# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .assert_correctness_check import AssertCorrectnessCheck
from .non_void_function_definition import NonVoidFunctionDefinition


class TestCaseWithActualResultImplementation(pydantic.BaseModel):
    get_actual_result: NonVoidFunctionDefinition = pydantic.Field(alias="getActualResult")
    assert_correctness_check: AssertCorrectnessCheck = pydantic.Field(alias="assertCorrectnessCheck")

    class Partial(typing_extensions.TypedDict):
        get_actual_result: typing_extensions.NotRequired[NonVoidFunctionDefinition]
        assert_correctness_check: typing_extensions.NotRequired[AssertCorrectnessCheck]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseWithActualResultImplementation.Validators.root
            def validate(values: TestCaseWithActualResultImplementation.Partial) -> TestCaseWithActualResultImplementation.Partial:
                ...

            @TestCaseWithActualResultImplementation.Validators.field("get_actual_result")
            def validate_get_actual_result(get_actual_result: NonVoidFunctionDefinition, values: TestCaseWithActualResultImplementation.Partial) -> NonVoidFunctionDefinition:
                ...

            @TestCaseWithActualResultImplementation.Validators.field("assert_correctness_check")
            def validate_assert_correctness_check(assert_correctness_check: AssertCorrectnessCheck, values: TestCaseWithActualResultImplementation.Partial) -> AssertCorrectnessCheck:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [TestCaseWithActualResultImplementation.Partial], TestCaseWithActualResultImplementation.Partial
                ]
            ]
        ] = []
        _get_actual_result_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators.GetActualResultValidator]
        ] = []
        _assert_correctness_check_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators.AssertCorrectnessCheckValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [TestCaseWithActualResultImplementation.Partial], TestCaseWithActualResultImplementation.Partial
            ],
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Partial], TestCaseWithActualResultImplementation.Partial
        ]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["get_actual_result"]
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators.GetActualResultValidator],
            TestCaseWithActualResultImplementation.Validators.GetActualResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["assert_correctness_check"]
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators.AssertCorrectnessCheckValidator],
            TestCaseWithActualResultImplementation.Validators.AssertCorrectnessCheckValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "get_actual_result":
                    cls._get_actual_result_validators.append(validator)
                if field_name == "assert_correctness_check":
                    cls._assert_correctness_check_validators.append(validator)
                return validator

            return decorator

        class GetActualResultValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: NonVoidFunctionDefinition, __values: TestCaseWithActualResultImplementation.Partial
            ) -> NonVoidFunctionDefinition:
                ...

        class AssertCorrectnessCheckValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: AssertCorrectnessCheck, __values: TestCaseWithActualResultImplementation.Partial
            ) -> AssertCorrectnessCheck:
                ...

    @pydantic.root_validator
    def _validate(
        cls, values: TestCaseWithActualResultImplementation.Partial
    ) -> TestCaseWithActualResultImplementation.Partial:
        for validator in TestCaseWithActualResultImplementation.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("get_actual_result")
    def _validate_get_actual_result(
        cls, v: NonVoidFunctionDefinition, values: TestCaseWithActualResultImplementation.Partial
    ) -> NonVoidFunctionDefinition:
        for validator in TestCaseWithActualResultImplementation.Validators._get_actual_result_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("assert_correctness_check")
    def _validate_assert_correctness_check(
        cls, v: AssertCorrectnessCheck, values: TestCaseWithActualResultImplementation.Partial
    ) -> AssertCorrectnessCheck:
        for validator in TestCaseWithActualResultImplementation.Validators._assert_correctness_check_validators:
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
