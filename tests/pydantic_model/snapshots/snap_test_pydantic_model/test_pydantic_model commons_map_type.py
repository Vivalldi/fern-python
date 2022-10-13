# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class MapType(pydantic.BaseModel):
    key_type: VariableType = pydantic.Field(alias="keyType")
    value_type: VariableType = pydantic.Field(alias="valueType")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @MapType.Validators.field("key_type")
            def validate_key_type(v: VariableType, values: MapType.Partial) -> VariableType:
                ...

            @MapType.Validators.field("value_type")
            def validate_value_type(v: VariableType, values: MapType.Partial) -> VariableType:
                ...
        """

        _key_type_validators: typing.ClassVar[typing.List[MapType.Validators.KeyTypeValidator]] = []
        _value_type_validators: typing.ClassVar[typing.List[MapType.Validators.ValueTypeValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key_type"]
        ) -> typing.Callable[[MapType.Validators.KeyTypeValidator], MapType.Validators.KeyTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"]
        ) -> typing.Callable[[MapType.Validators.ValueTypeValidator], MapType.Validators.ValueTypeValidator]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "key_type":
                    cls._key_type_validators.append(validator)
                if field_name == "value_type":
                    cls._value_type_validators.append(validator)
                return validator

            return decorator

        class KeyTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: MapType.Partial) -> VariableType:
                ...

        class ValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: VariableType, *, values: MapType.Partial) -> VariableType:
                ...

    @pydantic.validator("key_type")
    def _validate_key_type(cls, v: VariableType, values: MapType.Partial) -> VariableType:
        for validator in MapType.Validators._key_type_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("value_type")
    def _validate_value_type(cls, v: VariableType, values: MapType.Partial) -> VariableType:
        for validator in MapType.Validators._value_type_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        key_type: typing_extensions.NotRequired[VariableType]
        value_type: typing_extensions.NotRequired[VariableType]

    class Config:
        frozen = True
        allow_population_by_field_name = True


from .variable_type import VariableType  # noqa: E402

MapType.update_forward_refs()
