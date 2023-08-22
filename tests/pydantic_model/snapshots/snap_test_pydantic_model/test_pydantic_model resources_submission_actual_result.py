# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.binary_tree_node_value import BinaryTreeNodeValue
from ..commons.binary_tree_value import BinaryTreeValue
from ..commons.doubly_linked_list_node_value import DoublyLinkedListNodeValue
from ..commons.doubly_linked_list_value import DoublyLinkedListValue
from ..commons.node_id import NodeId
from ..commons.singly_linked_list_node_value import SinglyLinkedListNodeValue
from ..commons.singly_linked_list_value import SinglyLinkedListValue
from .exception_info import ExceptionInfo
from .exception_v_2 import ExceptionV2


class ActualResult_Value(pydantic.BaseModel):
    type: typing_extensions.Literal["value"]
    value: VariableValue


class ActualResult_Exception(ExceptionInfo):
    type: typing_extensions.Literal["exception"]

    class Config:
        allow_population_by_field_name = True


class ActualResult_ExceptionV2(pydantic.BaseModel):
    type: typing_extensions.Literal["exceptionV2"]
    value: ExceptionV2


ActualResult = typing.Union[ActualResult_Value, ActualResult_Exception, ActualResult_ExceptionV2]
from ..commons.key_value_pair import KeyValuePair  # noqa: E402
from ..commons.map_value import MapValue  # noqa: E402
from ..commons.variable_value import VariableValue  # noqa: E402
