# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from ..commons.variable_value import VariableValue
from .exception_v_2 import ExceptionV2


class TestCaseNonHiddenGrade(pydantic.BaseModel):
    passed: bool
    actual_result: typing.Optional[VariableValue] = pydantic.Field(alias="actualResult", default=None)
    exception: typing.Optional[ExceptionV2] = None
    stdout: str

    class Partial(typing_extensions.TypedDict):
        passed: typing_extensions.NotRequired[bool]
        actual_result: typing_extensions.NotRequired[typing.Optional[VariableValue]]
        exception: typing_extensions.NotRequired[typing.Optional[ExceptionV2]]
        stdout: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseNonHiddenGrade.Validators.root()
            def validate(values: TestCaseNonHiddenGrade.Partial) -> TestCaseNonHiddenGrade.Partial:
                ...

            @TestCaseNonHiddenGrade.Validators.field("passed")
            def validate_passed(passed: bool, values: TestCaseNonHiddenGrade.Partial) -> bool:
                ...

            @TestCaseNonHiddenGrade.Validators.field("actual_result")
            def validate_actual_result(actual_result: typing.Optional[VariableValue], values: TestCaseNonHiddenGrade.Partial) -> typing.Optional[VariableValue]:
                ...

            @TestCaseNonHiddenGrade.Validators.field("exception")
            def validate_exception(exception: typing.Optional[ExceptionV2], values: TestCaseNonHiddenGrade.Partial) -> typing.Optional[ExceptionV2]:
                ...

            @TestCaseNonHiddenGrade.Validators.field("stdout")
            def validate_stdout(stdout: str, values: TestCaseNonHiddenGrade.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators._RootValidator]] = []
        _passed_pre_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.PrePassedValidator]] = []
        _passed_post_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.PassedValidator]] = []
        _actual_result_pre_validators: typing.ClassVar[
            typing.List[TestCaseNonHiddenGrade.Validators.PreActualResultValidator]
        ] = []
        _actual_result_post_validators: typing.ClassVar[
            typing.List[TestCaseNonHiddenGrade.Validators.ActualResultValidator]
        ] = []
        _exception_pre_validators: typing.ClassVar[
            typing.List[TestCaseNonHiddenGrade.Validators.PreExceptionValidator]
        ] = []
        _exception_post_validators: typing.ClassVar[
            typing.List[TestCaseNonHiddenGrade.Validators.ExceptionValidator]
        ] = []
        _stdout_pre_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.PreStdoutValidator]] = []
        _stdout_post_validators: typing.ClassVar[typing.List[TestCaseNonHiddenGrade.Validators.StdoutValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators._RootValidator], TestCaseNonHiddenGrade.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators._PreRootValidator], TestCaseNonHiddenGrade.Validators._PreRootValidator
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.PrePassedValidator], TestCaseNonHiddenGrade.Validators.PrePassedValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["passed"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.PassedValidator], TestCaseNonHiddenGrade.Validators.PassedValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_result"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.PreActualResultValidator],
            TestCaseNonHiddenGrade.Validators.PreActualResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["actual_result"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.ActualResultValidator],
            TestCaseNonHiddenGrade.Validators.ActualResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.PreExceptionValidator],
            TestCaseNonHiddenGrade.Validators.PreExceptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["exception"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.ExceptionValidator], TestCaseNonHiddenGrade.Validators.ExceptionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.PreStdoutValidator], TestCaseNonHiddenGrade.Validators.PreStdoutValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TestCaseNonHiddenGrade.Validators.StdoutValidator], TestCaseNonHiddenGrade.Validators.StdoutValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "passed":
                    if pre:
                        cls._passed_pre_validators.append(validator)
                    else:
                        cls._passed_post_validators.append(validator)
                if field_name == "actual_result":
                    if pre:
                        cls._actual_result_pre_validators.append(validator)
                    else:
                        cls._actual_result_post_validators.append(validator)
                if field_name == "exception":
                    if pre:
                        cls._exception_pre_validators.append(validator)
                    else:
                        cls._exception_post_validators.append(validator)
                if field_name == "stdout":
                    if pre:
                        cls._stdout_pre_validators.append(validator)
                    else:
                        cls._stdout_post_validators.append(validator)
                return validator

            return decorator

        class PrePassedValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseNonHiddenGrade.Partial) -> typing.Any:
                ...

        class PassedValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: TestCaseNonHiddenGrade.Partial) -> bool:
                ...

        class PreActualResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseNonHiddenGrade.Partial) -> typing.Any:
                ...

        class ActualResultValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[VariableValue], __values: TestCaseNonHiddenGrade.Partial
            ) -> typing.Optional[VariableValue]:
                ...

        class PreExceptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseNonHiddenGrade.Partial) -> typing.Any:
                ...

        class ExceptionValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[ExceptionV2], __values: TestCaseNonHiddenGrade.Partial
            ) -> typing.Optional[ExceptionV2]:
                ...

        class PreStdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseNonHiddenGrade.Partial) -> typing.Any:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: TestCaseNonHiddenGrade.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseNonHiddenGrade.Partial) -> TestCaseNonHiddenGrade.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_test_case_non_hidden_grade(
        cls, values: TestCaseNonHiddenGrade.Partial
    ) -> TestCaseNonHiddenGrade.Partial:
        for validator in TestCaseNonHiddenGrade.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_test_case_non_hidden_grade(
        cls, values: TestCaseNonHiddenGrade.Partial
    ) -> TestCaseNonHiddenGrade.Partial:
        for validator in TestCaseNonHiddenGrade.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("passed", pre=True)
    def _pre_validate_passed(cls, v: bool, values: TestCaseNonHiddenGrade.Partial) -> bool:
        for validator in TestCaseNonHiddenGrade.Validators._passed_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("passed", pre=False)
    def _post_validate_passed(cls, v: bool, values: TestCaseNonHiddenGrade.Partial) -> bool:
        for validator in TestCaseNonHiddenGrade.Validators._passed_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result", pre=True)
    def _pre_validate_actual_result(
        cls, v: typing.Optional[VariableValue], values: TestCaseNonHiddenGrade.Partial
    ) -> typing.Optional[VariableValue]:
        for validator in TestCaseNonHiddenGrade.Validators._actual_result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result", pre=False)
    def _post_validate_actual_result(
        cls, v: typing.Optional[VariableValue], values: TestCaseNonHiddenGrade.Partial
    ) -> typing.Optional[VariableValue]:
        for validator in TestCaseNonHiddenGrade.Validators._actual_result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception", pre=True)
    def _pre_validate_exception(
        cls, v: typing.Optional[ExceptionV2], values: TestCaseNonHiddenGrade.Partial
    ) -> typing.Optional[ExceptionV2]:
        for validator in TestCaseNonHiddenGrade.Validators._exception_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("exception", pre=False)
    def _post_validate_exception(
        cls, v: typing.Optional[ExceptionV2], values: TestCaseNonHiddenGrade.Partial
    ) -> typing.Optional[ExceptionV2]:
        for validator in TestCaseNonHiddenGrade.Validators._exception_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=True)
    def _pre_validate_stdout(cls, v: str, values: TestCaseNonHiddenGrade.Partial) -> str:
        for validator in TestCaseNonHiddenGrade.Validators._stdout_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=False)
    def _post_validate_stdout(cls, v: str, values: TestCaseNonHiddenGrade.Partial) -> str:
        for validator in TestCaseNonHiddenGrade.Validators._stdout_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
