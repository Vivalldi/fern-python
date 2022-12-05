# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .binary_tree_value import BinaryTreeValue
from .node_id import NodeId


class BinaryTreeNodeAndTreeValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_tree: BinaryTreeValue = pydantic.Field(alias="fullTree")

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        full_tree: typing_extensions.NotRequired[BinaryTreeValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @BinaryTreeNodeAndTreeValue.Validators.root
            def validate(values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeNodeAndTreeValue.Partial:
                ...

            @BinaryTreeNodeAndTreeValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
                ...

            @BinaryTreeNodeAndTreeValue.Validators.field("full_tree")
            def validate_full_tree(full_tree: BinaryTreeValue, values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeValue:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[BinaryTreeNodeAndTreeValue.Partial], BinaryTreeNodeAndTreeValue.Partial]]
        ] = []
        _node_id_validators: typing.ClassVar[typing.List[BinaryTreeNodeAndTreeValue.Validators.NodeIdValidator]] = []
        _full_tree_validators: typing.ClassVar[
            typing.List[BinaryTreeNodeAndTreeValue.Validators.FullTreeValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[BinaryTreeNodeAndTreeValue.Partial], BinaryTreeNodeAndTreeValue.Partial]
        ) -> typing.Callable[[BinaryTreeNodeAndTreeValue.Partial], BinaryTreeNodeAndTreeValue.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"]
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators.NodeIdValidator],
            BinaryTreeNodeAndTreeValue.Validators.NodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_tree"]
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators.FullTreeValidator],
            BinaryTreeNodeAndTreeValue.Validators.FullTreeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    cls._node_id_validators.append(validator)
                if field_name == "full_tree":
                    cls._full_tree_validators.append(validator)
                return validator

            return decorator

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: NodeId, __values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
                ...

        class FullTreeValidator(typing_extensions.Protocol):
            def __call__(self, __v: BinaryTreeValue, __values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeValue:
                ...

    @pydantic.root_validator
    def _validate(cls, values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeNodeAndTreeValue.Partial:
        for validator in BinaryTreeNodeAndTreeValue.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id")
    def _validate_node_id(cls, v: NodeId, values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
        for validator in BinaryTreeNodeAndTreeValue.Validators._node_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_tree")
    def _validate_full_tree(cls, v: BinaryTreeValue, values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeValue:
        for validator in BinaryTreeNodeAndTreeValue.Validators._full_tree_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
