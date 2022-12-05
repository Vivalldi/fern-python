# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class WorkspaceTracedUpdate(pydantic.BaseModel):
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    class Partial(typing_extensions.TypedDict):
        trace_responses_size: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceTracedUpdate.Validators.root
            def validate(values: WorkspaceTracedUpdate.Partial) -> WorkspaceTracedUpdate.Partial:
                ...

            @WorkspaceTracedUpdate.Validators.field("trace_responses_size")
            def validate_trace_responses_size(trace_responses_size: int, values: WorkspaceTracedUpdate.Partial) -> int:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[WorkspaceTracedUpdate.Partial], WorkspaceTracedUpdate.Partial]]
        ] = []
        _trace_responses_size_validators: typing.ClassVar[
            typing.List[WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[WorkspaceTracedUpdate.Partial], WorkspaceTracedUpdate.Partial]
        ) -> typing.Callable[[WorkspaceTracedUpdate.Partial], WorkspaceTracedUpdate.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses_size"]
        ) -> typing.Callable[
            [WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator],
            WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "trace_responses_size":
                    cls._trace_responses_size_validators.append(validator)
                return validator

            return decorator

        class TraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: WorkspaceTracedUpdate.Partial) -> int:
                ...

    @pydantic.root_validator
    def _validate(cls, values: WorkspaceTracedUpdate.Partial) -> WorkspaceTracedUpdate.Partial:
        for validator in WorkspaceTracedUpdate.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("trace_responses_size")
    def _validate_trace_responses_size(cls, v: int, values: WorkspaceTracedUpdate.Partial) -> int:
        for validator in WorkspaceTracedUpdate.Validators._trace_responses_size_validators:
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
