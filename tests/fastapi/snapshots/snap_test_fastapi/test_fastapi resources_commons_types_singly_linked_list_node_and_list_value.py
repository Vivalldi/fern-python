# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .node_id import NodeId
from .singly_linked_list_value import SinglyLinkedListValue


class SinglyLinkedListNodeAndListValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    full_list: SinglyLinkedListValue = pydantic.Field(alias="fullList")

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        full_list: typing_extensions.NotRequired[SinglyLinkedListValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SinglyLinkedListNodeAndListValue.Validators.root()
            def validate(values: SinglyLinkedListNodeAndListValue.Partial) -> SinglyLinkedListNodeAndListValue.Partial:
                ...

            @SinglyLinkedListNodeAndListValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
                ...

            @SinglyLinkedListNodeAndListValue.Validators.field("full_list")
            def validate_full_list(full_list: SinglyLinkedListValue, values: SinglyLinkedListNodeAndListValue.Partial) -> SinglyLinkedListValue:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[typing.List[SinglyLinkedListNodeAndListValue.Validators._RootValidator]] = []
        _node_id_pre_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators.PreNodeIdValidator]
        ] = []
        _node_id_post_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators.NodeIdValidator]
        ] = []
        _full_list_pre_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators.PreFullListValidator]
        ] = []
        _full_list_post_validators: typing.ClassVar[
            typing.List[SinglyLinkedListNodeAndListValue.Validators.FullListValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators._RootValidator],
            SinglyLinkedListNodeAndListValue.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators._PreRootValidator],
            SinglyLinkedListNodeAndListValue.Validators._PreRootValidator,
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
            [SinglyLinkedListNodeAndListValue.Validators.PreNodeIdValidator],
            SinglyLinkedListNodeAndListValue.Validators.PreNodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["node_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators.NodeIdValidator],
            SinglyLinkedListNodeAndListValue.Validators.NodeIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators.PreFullListValidator],
            SinglyLinkedListNodeAndListValue.Validators.PreFullListValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["full_list"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SinglyLinkedListNodeAndListValue.Validators.FullListValidator],
            SinglyLinkedListNodeAndListValue.Validators.FullListValidator,
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
                if field_name == "full_list":
                    if pre:
                        cls._full_list_pre_validators.append(validator)
                    else:
                        cls._full_list_post_validators.append(validator)
                return validator

            return decorator

        class PreNodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SinglyLinkedListNodeAndListValue.Partial) -> typing.Any:
                ...

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: NodeId, __values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
                ...

        class PreFullListValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SinglyLinkedListNodeAndListValue.Partial) -> typing.Any:
                ...

        class FullListValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: SinglyLinkedListValue, __values: SinglyLinkedListNodeAndListValue.Partial
            ) -> SinglyLinkedListValue:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: SinglyLinkedListNodeAndListValue.Partial
            ) -> SinglyLinkedListNodeAndListValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _presingly_linked_list_node_and_list_value_validate(
        cls, values: SinglyLinkedListNodeAndListValue.Partial
    ) -> SinglyLinkedListNodeAndListValue.Partial:
        for validator in SinglyLinkedListNodeAndListValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postsingly_linked_list_node_and_list_value_validate(
        cls, values: SinglyLinkedListNodeAndListValue.Partial
    ) -> SinglyLinkedListNodeAndListValue.Partial:
        for validator in SinglyLinkedListNodeAndListValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id", pre=True)
    def _pre_validate_node_id(cls, v: NodeId, values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
        for validator in SinglyLinkedListNodeAndListValue.Validators._node_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("node_id", pre=False)
    def _post_validate_node_id(cls, v: NodeId, values: SinglyLinkedListNodeAndListValue.Partial) -> NodeId:
        for validator in SinglyLinkedListNodeAndListValue.Validators._node_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_list", pre=True)
    def _pre_validate_full_list(
        cls, v: SinglyLinkedListValue, values: SinglyLinkedListNodeAndListValue.Partial
    ) -> SinglyLinkedListValue:
        for validator in SinglyLinkedListNodeAndListValue.Validators._full_list_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("full_list", pre=False)
    def _post_validate_full_list(
        cls, v: SinglyLinkedListValue, values: SinglyLinkedListNodeAndListValue.Partial
    ) -> SinglyLinkedListValue:
        for validator in SinglyLinkedListNodeAndListValue.Validators._full_list_post_validators:
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
