# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..submission.test_case_result_with_stdout import TestCaseResultWithStdout
from ..submission.trace_response import TraceResponse


class StoreTracedTestCaseRequest(pydantic.BaseModel):
    result: TestCaseResultWithStdout
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    class Partial(typing_extensions.TypedDict):
        result: typing_extensions.NotRequired[TestCaseResultWithStdout]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponse]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoreTracedTestCaseRequest.Validators.root()
            def validate(values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
                ...

            @StoreTracedTestCaseRequest.Validators.field("result")
            def validate_result(result: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial) -> TestCaseResultWithStdout:
                ...

            @StoreTracedTestCaseRequest.Validators.field("trace_responses")
            def validate_trace_responses(trace_responses: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial) -> typing.List[TraceResponse]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StoreTracedTestCaseRequest.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StoreTracedTestCaseRequest.Validators._RootValidator]] = []
        _result_pre_validators: typing.ClassVar[typing.List[StoreTracedTestCaseRequest.Validators.ResultValidator]] = []
        _result_post_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.ResultValidator]
        ] = []
        _trace_responses_pre_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.TraceResponsesValidator]
        ] = []
        _trace_responses_post_validators: typing.ClassVar[
            typing.List[StoreTracedTestCaseRequest.Validators.TraceResponsesValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators._RootValidator], StoreTracedTestCaseRequest.Validators._RootValidator
        ]:
            def decorator(
                validator: StoreTracedTestCaseRequest.Validators._RootValidator,
            ) -> StoreTracedTestCaseRequest.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["result"], *, pre: bool = False
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.ResultValidator],
            StoreTracedTestCaseRequest.Validators.ResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"], *, pre: bool = False
        ) -> typing.Callable[
            [StoreTracedTestCaseRequest.Validators.TraceResponsesValidator],
            StoreTracedTestCaseRequest.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "result":
                    if pre:
                        cls._result_pre_validators.append(validator)
                    else:
                        cls._result_post_validators.append(validator)
                if field_name == "trace_responses":
                    if pre:
                        cls._trace_responses_pre_validators.append(validator)
                    else:
                        cls._trace_responses_post_validators.append(validator)
                return validator

            return decorator

        class ResultValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseResultWithStdout, __values: StoreTracedTestCaseRequest.Partial
            ) -> TestCaseResultWithStdout:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TraceResponse], __values: StoreTracedTestCaseRequest.Partial
            ) -> typing.List[TraceResponse]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
        for validator in StoreTracedTestCaseRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StoreTracedTestCaseRequest.Partial) -> StoreTracedTestCaseRequest.Partial:
        for validator in StoreTracedTestCaseRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("result", pre=True)
    def _pre_validate_result(
        cls, v: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial
    ) -> TestCaseResultWithStdout:
        for validator in StoreTracedTestCaseRequest.Validators._result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("result", pre=False)
    def _post_validate_result(
        cls, v: TestCaseResultWithStdout, values: StoreTracedTestCaseRequest.Partial
    ) -> TestCaseResultWithStdout:
        for validator in StoreTracedTestCaseRequest.Validators._result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=True)
    def _pre_validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedTestCaseRequest.Validators._trace_responses_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=False)
    def _post_validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedTestCaseRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedTestCaseRequest.Validators._trace_responses_post_validators:
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
