# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_grade import TestCaseGrade
from .test_case_result_with_stdout import TestCaseResultWithStdout
from .traced_test_case import TracedTestCase


class SubmissionStatusForTestCase_Graded(TestCaseResultWithStdout):
    type: typing_extensions.Literal["graded"]

    class Config:
        allow_population_by_field_name = True


class SubmissionStatusForTestCase_GradedV2(pydantic.BaseModel):
    type: typing_extensions.Literal["gradedV2"]
    value: TestCaseGrade


class SubmissionStatusForTestCase_Traced(TracedTestCase):
    type: typing_extensions.Literal["traced"]

    class Config:
        allow_population_by_field_name = True


SubmissionStatusForTestCase = typing.Union[
    SubmissionStatusForTestCase_Graded, SubmissionStatusForTestCase_GradedV2, SubmissionStatusForTestCase_Traced
]
