# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.binary_tree_node_value import BinaryTreeNodeValue
from ...commons.types.binary_tree_value import BinaryTreeValue
from ...commons.types.doubly_linked_list_node_value import DoublyLinkedListNodeValue
from ...commons.types.doubly_linked_list_value import DoublyLinkedListValue
from ...commons.types.node_id import NodeId
from ...commons.types.singly_linked_list_node_value import SinglyLinkedListNodeValue
from ...commons.types.singly_linked_list_value import SinglyLinkedListValue
from .actual_result import ActualResult
from .compile_error import CompileError
from .error_info import ErrorInfo
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2
from .internal_error import InternalError
from .running_submission_state import RunningSubmissionState
from .runtime_error import RuntimeError
from .submission_status_for_test_case import SubmissionStatusForTestCase
from .test_case_grade import TestCaseGrade
from .test_case_hidden_grade import TestCaseHiddenGrade
from .test_case_non_hidden_grade import TestCaseNonHiddenGrade
from .test_case_result import TestCaseResult
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_test_case import TracedTestCase


class TestSubmissionStatus_Stopped(pydantic.BaseModel):
    type: typing_extensions.Literal["stopped"]

    class Config:
        frozen = True
        smart_union = True


class TestSubmissionStatus_Errored(pydantic.BaseModel):
    type: typing_extensions.Literal["errored"]
    value: ErrorInfo

    class Config:
        frozen = True
        smart_union = True


class TestSubmissionStatus_Running(pydantic.BaseModel):
    type: typing_extensions.Literal["running"]
    value: RunningSubmissionState

    class Config:
        frozen = True
        smart_union = True


class TestSubmissionStatus_TestCaseIdToState(pydantic.BaseModel):
    type: typing_extensions.Literal["testCaseIdToState"]
    value: typing.Dict[str, SubmissionStatusForTestCase]

    class Config:
        frozen = True
        smart_union = True


TestSubmissionStatus = typing.Union[
    TestSubmissionStatus_Stopped,
    TestSubmissionStatus_Errored,
    TestSubmissionStatus_Running,
    TestSubmissionStatus_TestCaseIdToState,
]
from ...commons.types.key_value_pair import KeyValuePair  # noqa: E402
from ...commons.types.map_value import MapValue  # noqa: E402
from ...commons.types.variable_value import VariableValue  # noqa: E402
