# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .compile_error import CompileError
from .error_info import ErrorInfo
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .internal_error import InternalError
from .running_submission_state import RunningSubmissionState
from .runtime_error import RuntimeError
from .workspace_run_details import WorkspaceRunDetails


class WorkspaceSubmissionStatus_Stopped(pydantic.BaseModel):
    type: typing_extensions.Literal["stopped"]


class WorkspaceSubmissionStatus_Errored(pydantic.BaseModel):
    type: typing_extensions.Literal["errored"]
    value: ErrorInfo


class WorkspaceSubmissionStatus_Running(pydantic.BaseModel):
    type: typing_extensions.Literal["running"]
    value: RunningSubmissionState


class WorkspaceSubmissionStatus_Ran(WorkspaceRunDetails):
    type: typing_extensions.Literal["ran"]

    class Config:
        allow_population_by_field_name = True


class WorkspaceSubmissionStatus_Traced(WorkspaceRunDetails):
    type: typing_extensions.Literal["traced"]

    class Config:
        allow_population_by_field_name = True


WorkspaceSubmissionStatus = typing.Union[
    WorkspaceSubmissionStatus_Stopped,
    WorkspaceSubmissionStatus_Errored,
    WorkspaceSubmissionStatus_Running,
    WorkspaceSubmissionStatus_Ran,
    WorkspaceSubmissionStatus_Traced,
]
