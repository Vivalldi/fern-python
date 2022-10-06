from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .binary_tree_value import BinaryTreeValue
from .doubly_linked_list_value import DoublyLinkedListValue
from .singly_linked_list_value import SinglyLinkedListValue

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def integer_value(self, value: int) -> VariableValue:
        return VariableValue(__root__=_VariableValue.IntegerValue(type="integerValue", value=value))

    def boolean_value(self, value: bool) -> VariableValue:
        return VariableValue(__root__=_VariableValue.BooleanValue(type="booleanValue", value=value))

    def double_value(self, value: float) -> VariableValue:
        return VariableValue(__root__=_VariableValue.DoubleValue(type="doubleValue", value=value))

    def string_value(self, value: str) -> VariableValue:
        return VariableValue(__root__=_VariableValue.StringValue(type="stringValue", value=value))

    def char_value(self, value: str) -> VariableValue:
        return VariableValue(__root__=_VariableValue.CharValue(type="charValue", value=value))

    def map_value(self, value: MapValue) -> VariableValue:
        return VariableValue(__root__=_VariableValue.MapValue(**dict(value), type="mapValue"))

    def list_value(self, value: typing.List[VariableValue]) -> VariableValue:
        return VariableValue(__root__=_VariableValue.ListValue(type="listValue", value=value))

    def binary_tree_value(self, value: BinaryTreeValue) -> VariableValue:
        return VariableValue(__root__=_VariableValue.BinaryTreeValue(**dict(value), type="binaryTreeValue"))

    def singly_linked_list_value(self, value: SinglyLinkedListValue) -> VariableValue:
        return VariableValue(__root__=_VariableValue.SinglyLinkedListValue(**dict(value), type="singlyLinkedListValue"))

    def doubly_linked_list_value(self, value: DoublyLinkedListValue) -> VariableValue:
        return VariableValue(__root__=_VariableValue.DoublyLinkedListValue(**dict(value), type="doublyLinkedListValue"))

    def null_value(self) -> VariableValue:
        return VariableValue(__root__=_VariableValue.NullValue(type="nullValue"))


class VariableValue(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _VariableValue.IntegerValue,
        _VariableValue.BooleanValue,
        _VariableValue.DoubleValue,
        _VariableValue.StringValue,
        _VariableValue.CharValue,
        _VariableValue.MapValue,
        _VariableValue.ListValue,
        _VariableValue.BinaryTreeValue,
        _VariableValue.SinglyLinkedListValue,
        _VariableValue.DoublyLinkedListValue,
        _VariableValue.NullValue,
    ]:
        return self.__root__

    def visit(
        self,
        integer_value: typing.Callable[[int], T_Result],
        boolean_value: typing.Callable[[bool], T_Result],
        double_value: typing.Callable[[float], T_Result],
        string_value: typing.Callable[[str], T_Result],
        char_value: typing.Callable[[str], T_Result],
        map_value: typing.Callable[[MapValue], T_Result],
        list_value: typing.Callable[[typing.List[VariableValue]], T_Result],
        binary_tree_value: typing.Callable[[BinaryTreeValue], T_Result],
        singly_linked_list_value: typing.Callable[[SinglyLinkedListValue], T_Result],
        doubly_linked_list_value: typing.Callable[[DoublyLinkedListValue], T_Result],
        null_value: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.__root__.type == "integerValue":
            return integer_value(self.__root__.integer_value)
        if self.__root__.type == "booleanValue":
            return boolean_value(self.__root__.boolean_value)
        if self.__root__.type == "doubleValue":
            return double_value(self.__root__.double_value)
        if self.__root__.type == "stringValue":
            return string_value(self.__root__.string_value)
        if self.__root__.type == "charValue":
            return char_value(self.__root__.char_value)
        if self.__root__.type == "mapValue":
            return map_value(self.__root__)
        if self.__root__.type == "listValue":
            return list_value(self.__root__.list_value)
        if self.__root__.type == "binaryTreeValue":
            return binary_tree_value(self.__root__)
        if self.__root__.type == "singlyLinkedListValue":
            return singly_linked_list_value(self.__root__)
        if self.__root__.type == "doublyLinkedListValue":
            return doubly_linked_list_value(self.__root__)
        if self.__root__.type == "nullValue":
            return null_value()

    __root__: typing_extensions.Annotated[
        typing.Union[
            _VariableValue.IntegerValue,
            _VariableValue.BooleanValue,
            _VariableValue.DoubleValue,
            _VariableValue.StringValue,
            _VariableValue.CharValue,
            _VariableValue.MapValue,
            _VariableValue.ListValue,
            _VariableValue.BinaryTreeValue,
            _VariableValue.SinglyLinkedListValue,
            _VariableValue.DoublyLinkedListValue,
            _VariableValue.NullValue,
        ],
        pydantic.Field(discriminator="type"),
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[
                _VariableValue.IntegerValue,
                _VariableValue.BooleanValue,
                _VariableValue.DoubleValue,
                _VariableValue.StringValue,
                _VariableValue.CharValue,
                _VariableValue.MapValue,
                _VariableValue.ListValue,
                _VariableValue.BinaryTreeValue,
                _VariableValue.SinglyLinkedListValue,
                _VariableValue.DoublyLinkedListValue,
                _VariableValue.NullValue,
            ],
            values.get("__root__"),
        )
        for validator in VariableValue.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _VariableValue.IntegerValue,
                            _VariableValue.BooleanValue,
                            _VariableValue.DoubleValue,
                            _VariableValue.StringValue,
                            _VariableValue.CharValue,
                            _VariableValue.MapValue,
                            _VariableValue.ListValue,
                            _VariableValue.BinaryTreeValue,
                            _VariableValue.SinglyLinkedListValue,
                            _VariableValue.DoublyLinkedListValue,
                            _VariableValue.NullValue,
                        ]
                    ],
                    typing.Union[
                        _VariableValue.IntegerValue,
                        _VariableValue.BooleanValue,
                        _VariableValue.DoubleValue,
                        _VariableValue.StringValue,
                        _VariableValue.CharValue,
                        _VariableValue.MapValue,
                        _VariableValue.ListValue,
                        _VariableValue.BinaryTreeValue,
                        _VariableValue.SinglyLinkedListValue,
                        _VariableValue.DoublyLinkedListValue,
                        _VariableValue.NullValue,
                    ],
                ]
            ]
        ] = []

        @classmethod
        def add_validator(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _VariableValue.IntegerValue,
                        _VariableValue.BooleanValue,
                        _VariableValue.DoubleValue,
                        _VariableValue.StringValue,
                        _VariableValue.CharValue,
                        _VariableValue.MapValue,
                        _VariableValue.ListValue,
                        _VariableValue.BinaryTreeValue,
                        _VariableValue.SinglyLinkedListValue,
                        _VariableValue.DoublyLinkedListValue,
                        _VariableValue.NullValue,
                    ]
                ],
                typing.Union[
                    _VariableValue.IntegerValue,
                    _VariableValue.BooleanValue,
                    _VariableValue.DoubleValue,
                    _VariableValue.StringValue,
                    _VariableValue.CharValue,
                    _VariableValue.MapValue,
                    _VariableValue.ListValue,
                    _VariableValue.BinaryTreeValue,
                    _VariableValue.SinglyLinkedListValue,
                    _VariableValue.DoublyLinkedListValue,
                    _VariableValue.NullValue,
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True


from .map_value import MapValue  # noqa: E402


class _VariableValue:
    class IntegerValue(pydantic.BaseModel):
        type: typing_extensions.Literal["integerValue"]
        value: int

        class Config:
            frozen = True

    class BooleanValue(pydantic.BaseModel):
        type: typing_extensions.Literal["booleanValue"]
        value: bool

        class Config:
            frozen = True

    class DoubleValue(pydantic.BaseModel):
        type: typing_extensions.Literal["doubleValue"]
        value: float

        class Config:
            frozen = True

    class StringValue(pydantic.BaseModel):
        type: typing_extensions.Literal["stringValue"]
        value: str

        class Config:
            frozen = True

    class CharValue(pydantic.BaseModel):
        type: typing_extensions.Literal["charValue"]
        value: str

        class Config:
            frozen = True

    class MapValue(MapValue):
        type: typing_extensions.Literal["mapValue"]

        class Config:
            frozen = True

    class ListValue(pydantic.BaseModel):
        type: typing_extensions.Literal["listValue"]
        value: typing.List[VariableValue]

        class Config:
            frozen = True

    class BinaryTreeValue(BinaryTreeValue):
        type: typing_extensions.Literal["binaryTreeValue"]

        class Config:
            frozen = True

    class SinglyLinkedListValue(SinglyLinkedListValue):
        type: typing_extensions.Literal["singlyLinkedListValue"]

        class Config:
            frozen = True

    class DoublyLinkedListValue(DoublyLinkedListValue):
        type: typing_extensions.Literal["doublyLinkedListValue"]

        class Config:
            frozen = True

    class NullValue(pydantic.BaseModel):
        type: typing_extensions.Literal["nullValue"]

        class Config:
            frozen = True


VariableValue.update_forward_refs()
