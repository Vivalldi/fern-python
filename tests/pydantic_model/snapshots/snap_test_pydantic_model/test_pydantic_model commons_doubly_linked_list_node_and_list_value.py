import typing

import pydantic
import typing_extensions

from .doubly_linked_list_value import DoublyLinkedListValue
from .node_id import NodeId


class DoublyLinkedListNodeAndListValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: DoublyLinkedListValue = pydantic.Field(alias="fullList")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("node_id")
    def _validate_node_id(cls, node_id: NodeId) -> NodeId:
        for validator in DoublyLinkedListNodeAndListValue.Validators._node_id_validators:
            node_id = validator(node_id)
        return node_id

    @pydantic.validator("full_list")
    def _validate_full_list(cls, full_list: DoublyLinkedListValue) -> DoublyLinkedListValue:
        for validator in DoublyLinkedListNodeAndListValue.Validators._full_list_validators:
            full_list = validator(full_list)
        return full_list

    class Validators:
        _node_id_validators: typing.ClassVar[typing.List[typing.Callable[[NodeId], NodeId]]] = []
        _full_list_validators: typing.ClassVar[
            typing.List[typing.Callable[[DoublyLinkedListValue], DoublyLinkedListValue]]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[[typing.Callable[[NodeId], NodeId]], typing.Callable[[NodeId], NodeId]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"]
        ) -> typing.Callable[
            [typing.Callable[[DoublyLinkedListValue], DoublyLinkedListValue]],
            typing.Callable[[DoublyLinkedListValue], DoublyLinkedListValue],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    cls._node_id_validators.append(validator)
                elif field_name == "full_list":
                    cls._full_list_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on DoublyLinkedListNodeAndListValue: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
        allow_population_by_field_name = True
