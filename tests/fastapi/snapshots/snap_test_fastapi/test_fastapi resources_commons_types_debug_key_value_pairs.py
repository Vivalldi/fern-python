# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class DebugKeyValuePairs(pydantic.BaseModel):
    key: DebugVariableValue
    value: DebugVariableValue

    class Partial(typing_extensions.TypedDict):
        key: typing_extensions.NotRequired[DebugVariableValue]
        value: typing_extensions.NotRequired[DebugVariableValue]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DebugKeyValuePairs.Validators.root()
            def validate(values: DebugKeyValuePairs.Partial) -> DebugKeyValuePairs.Partial:
                ...

            @DebugKeyValuePairs.Validators.field("key")
            def validate_key(key: DebugVariableValue, values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
                ...

            @DebugKeyValuePairs.Validators.field("value")
            def validate_value(value: DebugVariableValue, values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[DebugKeyValuePairs.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[DebugKeyValuePairs.Validators._RootValidator]] = []
        _key_pre_validators: typing.ClassVar[typing.List[DebugKeyValuePairs.Validators.PreKeyValidator]] = []
        _key_post_validators: typing.ClassVar[typing.List[DebugKeyValuePairs.Validators.KeyValidator]] = []
        _value_pre_validators: typing.ClassVar[typing.List[DebugKeyValuePairs.Validators.PreValueValidator]] = []
        _value_post_validators: typing.ClassVar[typing.List[DebugKeyValuePairs.Validators.ValueValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [DebugKeyValuePairs.Validators._RootValidator], DebugKeyValuePairs.Validators._RootValidator
        ]:
            def decorator(
                validator: DebugKeyValuePairs.Validators._RootValidator,
            ) -> DebugKeyValuePairs.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DebugKeyValuePairs.Validators.PreKeyValidator], DebugKeyValuePairs.Validators.PreKeyValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["key"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[DebugKeyValuePairs.Validators.KeyValidator], DebugKeyValuePairs.Validators.KeyValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DebugKeyValuePairs.Validators.PreValueValidator], DebugKeyValuePairs.Validators.PreValueValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DebugKeyValuePairs.Validators.ValueValidator], DebugKeyValuePairs.Validators.ValueValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "key":
                    if pre:
                        cls._key_pre_validators.append(validator)
                    else:
                        cls._key_post_validators.append(validator)
                if field_name == "value":
                    if pre:
                        cls._value_pre_validators.append(validator)
                    else:
                        cls._value_post_validators.append(validator)
                return validator

            return decorator

        class PreKeyValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DebugKeyValuePairs.Partial) -> typing.Any:
                ...

        class KeyValidator(typing_extensions.Protocol):
            def __call__(self, __v: DebugVariableValue, __values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
                ...

        class PreValueValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DebugKeyValuePairs.Partial) -> typing.Any:
                ...

        class ValueValidator(typing_extensions.Protocol):
            def __call__(self, __v: DebugVariableValue, __values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: DebugKeyValuePairs.Partial) -> DebugKeyValuePairs.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: DebugKeyValuePairs.Partial) -> DebugKeyValuePairs.Partial:
        for validator in DebugKeyValuePairs.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: DebugKeyValuePairs.Partial) -> DebugKeyValuePairs.Partial:
        for validator in DebugKeyValuePairs.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("key", pre=True)
    def _pre_validate_key(cls, v: DebugVariableValue, values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
        for validator in DebugKeyValuePairs.Validators._key_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("key", pre=False)
    def _post_validate_key(cls, v: DebugVariableValue, values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
        for validator in DebugKeyValuePairs.Validators._key_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value", pre=True)
    def _pre_validate_value(cls, v: DebugVariableValue, values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
        for validator in DebugKeyValuePairs.Validators._value_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value", pre=False)
    def _post_validate_value(cls, v: DebugVariableValue, values: DebugKeyValuePairs.Partial) -> DebugVariableValue:
        for validator in DebugKeyValuePairs.Validators._value_post_validators:
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
        extra = pydantic.Extra.forbid


from .debug_variable_value import DebugVariableValue  # noqa: E402

DebugKeyValuePairs.update_forward_refs()
