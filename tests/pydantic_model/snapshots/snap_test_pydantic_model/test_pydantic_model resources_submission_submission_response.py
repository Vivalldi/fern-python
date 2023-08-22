# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.binary_tree_node_value import BinaryTreeNodeValue
from ..commons.binary_tree_value import BinaryTreeValue
from ..commons.doubly_linked_list_node_value import DoublyLinkedListNodeValue
from ..commons.doubly_linked_list_value import DoublyLinkedListValue
from ..commons.language import Language
from ..commons.node_id import NodeId
from ..commons.problem_id import ProblemId
from ..commons.singly_linked_list_node_value import SinglyLinkedListNodeValue
from ..commons.singly_linked_list_value import SinglyLinkedListValue
from ..v_2.resources.problem.test_case_id import TestCaseId
from .actual_result import ActualResult
from .building_executor_response import BuildingExecutorResponse
from .code_execution_update import CodeExecutionUpdate
from .compile_error import CompileError
from .custom_test_cases_unsupported import CustomTestCasesUnsupported
from .error_info import ErrorInfo
from .errored_response import ErroredResponse
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .execution_session_status import ExecutionSessionStatus
from .finished_response import FinishedResponse
from .graded_response import GradedResponse
from .graded_response_v_2 import GradedResponseV2
from .initialize_problem_request import InitializeProblemRequest
from .internal_error import InternalError
from .invalid_request_cause import InvalidRequestCause
from .invalid_request_response import InvalidRequestResponse
from .lightweight_stackframe_information import LightweightStackframeInformation
from .recorded_response_notification import RecordedResponseNotification
from .recording_response_notification import RecordingResponseNotification
from .running_response import RunningResponse
from .running_submission_state import RunningSubmissionState
from .runtime_error import RuntimeError
from .stop_request import StopRequest
from .stopped_response import StoppedResponse
from .submission_file_info import SubmissionFileInfo
from .submission_id import SubmissionId
from .submission_id_not_found import SubmissionIdNotFound
from .submission_request import SubmissionRequest
from .submit_request_v_2 import SubmitRequestV2
from .terminated_response import TerminatedResponse
from .test_case_grade import TestCaseGrade
from .test_case_hidden_grade import TestCaseHiddenGrade
from .test_case_non_hidden_grade import TestCaseNonHiddenGrade
from .test_case_result import TestCaseResult
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_file import TracedFile
from .unexpected_language_error import UnexpectedLanguageError
from .workspace_ran_response import WorkspaceRanResponse
from .workspace_run_details import WorkspaceRunDetails
from .workspace_submit_request import WorkspaceSubmitRequest


class SubmissionResponse_ServerInitialized(pydantic.BaseModel):
    type: typing_extensions.Literal["serverInitialized"]


class SubmissionResponse_ProblemInitialized(pydantic.BaseModel):
    type: typing_extensions.Literal["problemInitialized"]
    value: ProblemId


class SubmissionResponse_WorkspaceInitialized(pydantic.BaseModel):
    type: typing_extensions.Literal["workspaceInitialized"]


class SubmissionResponse_ServerErrored(ExceptionInfo):
    type: typing_extensions.Literal["serverErrored"]

    class Config:
        allow_population_by_field_name = True


class SubmissionResponse_CodeExecutionUpdate(pydantic.BaseModel):
    type: typing_extensions.Literal["codeExecutionUpdate"]
    value: CodeExecutionUpdate


class SubmissionResponse_Terminated(TerminatedResponse):
    type: typing_extensions.Literal["terminated"]

    class Config:
        allow_population_by_field_name = True


SubmissionResponse = typing.Union[
    SubmissionResponse_ServerInitialized,
    SubmissionResponse_ProblemInitialized,
    SubmissionResponse_WorkspaceInitialized,
    SubmissionResponse_ServerErrored,
    SubmissionResponse_CodeExecutionUpdate,
    SubmissionResponse_Terminated,
]
from ..commons.key_value_pair import KeyValuePair  # noqa: E402
from ..commons.map_value import MapValue  # noqa: E402
from ..commons.variable_value import VariableValue  # noqa: E402
