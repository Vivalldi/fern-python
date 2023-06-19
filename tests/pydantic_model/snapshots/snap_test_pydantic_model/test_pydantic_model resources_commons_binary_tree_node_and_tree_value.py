# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
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

            @BinaryTreeNodeAndTreeValue.Validators.root()
            def validate(values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeNodeAndTreeValue.Partial:
                ...

            @BinaryTreeNodeAndTreeValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
                ...

            @BinaryTreeNodeAndTreeValue.Validators.field("full_tree")
            def validate_full_tree(full_tree: BinaryTreeValue, values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeValue:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[BinaryTreeNodeAndTreeValue.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[BinaryTreeNodeAndTreeValue.Validators._RootValidator]] = []
        _node_id_pre_validators: typing.ClassVar[
            typing.List[BinaryTreeNodeAndTreeValue.Validators.PreNodeIdValidator]
        ] = []
        _node_id_post_validators: typing.ClassVar[
            typing.List[BinaryTreeNodeAndTreeValue.Validators.NodeIdValidator]
        ] = []
        _full_tree_pre_validators: typing.ClassVar[
            typing.List[BinaryTreeNodeAndTreeValue.Validators.PreFullTreeValidator]
        ] = []
        _full_tree_post_validators: typing.ClassVar[
            typing.List[BinaryTreeNodeAndTreeValue.Validators.FullTreeValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators._RootValidator], BinaryTreeNodeAndTreeValue.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators._PreRootValidator],
            BinaryTreeNodeAndTreeValue.Validators._PreRootValidator,
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators.PreNodeIdValidator],
            BinaryTreeNodeAndTreeValue.Validators.PreNodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators.NodeIdValidator],
            BinaryTreeNodeAndTreeValue.Validators.NodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_tree"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators.PreFullTreeValidator],
            BinaryTreeNodeAndTreeValue.Validators.PreFullTreeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_tree"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [BinaryTreeNodeAndTreeValue.Validators.FullTreeValidator],
            BinaryTreeNodeAndTreeValue.Validators.FullTreeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    if pre:
                        cls._node_id_pre_validators.append(validator)
                    else:
                        cls._node_id_post_validators.append(validator)
                if field_name == "full_tree":
                    if pre:
                        cls._full_tree_pre_validators.append(validator)
                    else:
                        cls._full_tree_post_validators.append(validator)
                return validator

            return decorator

        class PreNodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BinaryTreeNodeAndTreeValue.Partial) -> typing.Any:
                ...

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: NodeId, __values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
                ...

        class PreFullTreeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: BinaryTreeNodeAndTreeValue.Partial) -> typing.Any:
                ...

        class FullTreeValidator(typing_extensions.Protocol):
            def __call__(self, __v: BinaryTreeValue, __values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeValue:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeNodeAndTreeValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _prebinary_tree_node_and_tree_value_validate(
        cls, values: BinaryTreeNodeAndTreeValue.Partial
    ) -> BinaryTreeNodeAndTreeValue.Partial:
        for validator in BinaryTreeNodeAndTreeValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postbinary_tree_node_and_tree_value_validate(
        cls, values: BinaryTreeNodeAndTreeValue.Partial
    ) -> BinaryTreeNodeAndTreeValue.Partial:
        for validator in BinaryTreeNodeAndTreeValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id", pre=True)
    def _pre_validate_node_id(cls, v: NodeId, values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
        for validator in BinaryTreeNodeAndTreeValue.Validators._node_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("node_id", pre=False)
    def _post_validate_node_id(cls, v: NodeId, values: BinaryTreeNodeAndTreeValue.Partial) -> NodeId:
        for validator in BinaryTreeNodeAndTreeValue.Validators._node_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_tree", pre=True)
    def _pre_validate_full_tree(cls, v: BinaryTreeValue, values: BinaryTreeNodeAndTreeValue.Partial) -> BinaryTreeValue:
        for validator in BinaryTreeNodeAndTreeValue.Validators._full_tree_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_tree", pre=False)
    def _post_validate_full_tree(
        cls, v: BinaryTreeValue, values: BinaryTreeNodeAndTreeValue.Partial
    ) -> BinaryTreeValue:
        for validator in BinaryTreeNodeAndTreeValue.Validators._full_tree_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
