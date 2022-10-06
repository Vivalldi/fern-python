import typing

import pydantic
import typing_extensions

from .trace_response import TraceResponse


class TraceResponsesPage(pydantic.BaseModel):
    offset: typing.Optional[int]
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    @pydantic.validator("offset")
    def _validate_offset(cls, offset: typing.Optional[int]) -> typing.Optional[int]:
        for validator in TraceResponsesPage.Validators._offset:
            offset = validator(offset)
        return offset

    @pydantic.validator("trace_responses")
    def _validate_trace_responses(cls, trace_responses: typing.List[TraceResponse]) -> typing.List[TraceResponse]:
        for validator in TraceResponsesPage.Validators._trace_responses:
            trace_responses = validator(trace_responses)
        return trace_responses

    class Validators:
        _offset: typing.ClassVar[typing.Optional[int]] = []
        _trace_responses: typing.ClassVar[typing.List[TraceResponse]] = []

        @typing.overload
        @classmethod
        def field(offset: typing_extensions.Literal["offset"]) -> typing.Optional[int]:
            ...

        @typing.overload
        @classmethod
        def field(trace_responses: typing_extensions.Literal["trace_responses"]) -> typing.List[TraceResponse]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "offset":
                    cls._offset.append(validator)  # type: ignore
                elif field_name == "trace_responses":
                    cls._trace_responses.append(validator)  # type: ignore
                else:
                    raise RuntimeError("Field does not exist on TraceResponsesPage: " + field_name)

                return validator

            return validator  # type: ignore

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
