# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def list(self, value: typing.List[FieldValue]) -> ContainerValue:
        return ContainerValue(__root__=_ContainerValue.List(type="list", value=value))

    def optional(self, value: typing.Optional[FieldValue]) -> ContainerValue:
        return ContainerValue(__root__=_ContainerValue.Optional(type="optional", value=value))


class ContainerValue(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_ContainerValue.List, _ContainerValue.Optional]:
        return self.__root__

    def visit(
        self,
        list: typing.Callable[[typing.List[FieldValue]], T_Result],
        optional: typing.Callable[[typing.Optional[FieldValue]], T_Result],
    ) -> T_Result:
        if self.__root__.type == "list":
            return list(self.__root__.value)
        if self.__root__.type == "optional":
            return optional(self.__root__.value)

    __root__: typing_extensions.Annotated[
        typing.Union[_ContainerValue.List, _ContainerValue.Optional], pydantic.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}


from .field_value import FieldValue  # noqa: E402


class _ContainerValue:
    class List(pydantic.BaseModel):
        type: typing_extensions.Literal["list"]
        value: typing.List[FieldValue]

        class Config:
            frozen = True
            smart_union = True

    class Optional(pydantic.BaseModel):
        type: typing_extensions.Literal["optional"]
        value: typing.Optional[FieldValue]

        class Config:
            frozen = True
            smart_union = True


_ContainerValue.List.update_forward_refs(ContainerValue=ContainerValue, FieldValue=FieldValue)
_ContainerValue.Optional.update_forward_refs(ContainerValue=ContainerValue, FieldValue=FieldValue)
ContainerValue.update_forward_refs()
