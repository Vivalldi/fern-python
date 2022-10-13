# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..submission.trace_response import TraceResponse
from ..submission.workspace_run_details import WorkspaceRunDetails


class StoreTracedWorkspaceRequest(pydantic.BaseModel):
    workspace_run_details: WorkspaceRunDetails = pydantic.Field(alias="workspaceRunDetails")
    trace_responses: typing.List[TraceResponse] = pydantic.Field(alias="traceResponses")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoreTracedWorkspaceRequest.Validators.field("workspace_run_details")
            def validate_workspace_run_details(v: WorkspaceRunDetails, values: StoreTracedWorkspaceRequest.Partial) -> WorkspaceRunDetails:
                ...

            @StoreTracedWorkspaceRequest.Validators.field("trace_responses")
            def validate_trace_responses(v: typing.List[TraceResponse], values: StoreTracedWorkspaceRequest.Partial) -> typing.List[TraceResponse]:
                ...
        """

        _workspace_run_details_validators: typing.ClassVar[
            typing.List[StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator]
        ] = []
        _trace_responses_validators: typing.ClassVar[
            typing.List[StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["workspace_run_details"]
        ) -> typing.Callable[
            [StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator],
            StoreTracedWorkspaceRequest.Validators.WorkspaceRunDetailsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"]
        ) -> typing.Callable[
            [StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator],
            StoreTracedWorkspaceRequest.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "workspace_run_details":
                    cls._workspace_run_details_validators.append(validator)
                if field_name == "trace_responses":
                    cls._trace_responses_validators.append(validator)
                return validator

            return decorator

        class WorkspaceRunDetailsValidator(typing_extensions.Protocol):
            def __call__(
                self, v: WorkspaceRunDetails, *, values: StoreTracedWorkspaceRequest.Partial
            ) -> WorkspaceRunDetails:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.List[TraceResponse], *, values: StoreTracedWorkspaceRequest.Partial
            ) -> typing.List[TraceResponse]:
                ...

    @pydantic.validator("workspace_run_details")
    def _validate_workspace_run_details(
        cls, v: WorkspaceRunDetails, values: StoreTracedWorkspaceRequest.Partial
    ) -> WorkspaceRunDetails:
        for validator in StoreTracedWorkspaceRequest.Validators._workspace_run_details_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("trace_responses")
    def _validate_trace_responses(
        cls, v: typing.List[TraceResponse], values: StoreTracedWorkspaceRequest.Partial
    ) -> typing.List[TraceResponse]:
        for validator in StoreTracedWorkspaceRequest.Validators._trace_responses_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        workspace_run_details: typing_extensions.NotRequired[WorkspaceRunDetails]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponse]]

    class Config:
        frozen = True
        allow_population_by_field_name = True
