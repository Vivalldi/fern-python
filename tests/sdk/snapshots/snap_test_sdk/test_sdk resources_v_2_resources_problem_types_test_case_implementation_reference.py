# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.list_type import ListType
from .....commons.types.map_type import MapType
from .....commons.types.variable_type import VariableType
from .test_case_implementation import TestCaseImplementation
from .test_case_template_id import TestCaseTemplateId


class TestCaseImplementationReference_TemplateId(pydantic.BaseModel):
    type: typing_extensions.Literal["templateId"] = "templateId"
    value: TestCaseTemplateId

    class Config:
        frozen = True


class TestCaseImplementationReference_Implementation(TestCaseImplementation):
    type: typing_extensions.Literal["implementation"] = "implementation"

    class Config:
        frozen = True


TestCaseImplementationReference = typing_extensions.Annotated[
    typing.Union[TestCaseImplementationReference_TemplateId, TestCaseImplementationReference_Implementation],
    pydantic.Field(discriminator="type"),
]
TestCaseImplementationReference_Implementation.update_forward_refs(
    ListType=ListType, MapType=MapType, VariableType=VariableType
)
