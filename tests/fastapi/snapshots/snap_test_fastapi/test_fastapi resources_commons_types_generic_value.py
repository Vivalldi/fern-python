# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class GenericValue(pydantic.BaseModel):
    stringified_type: typing.Optional[str] = pydantic.Field(alias="stringifiedType")
    stringified_value: str = pydantic.Field(alias="stringifiedValue")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GenericValue.Validators.field("stringified_type")
            def validate_stringified_type(v: typing.Optional[str], values: GenericValue.Partial) -> typing.Optional[str]:
                ...

            @GenericValue.Validators.field("stringified_value")
            def validate_stringified_value(v: str, values: GenericValue.Partial) -> str:
                ...
        """

        _stringified_type_validators: typing.ClassVar[
            typing.List[GenericValue.Validators.StringifiedTypeValidator]
        ] = []
        _stringified_value_validators: typing.ClassVar[
            typing.List[GenericValue.Validators.StringifiedValueValidator]
        ] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stringified_type"]
        ) -> typing.Callable[
            [GenericValue.Validators.StringifiedTypeValidator], GenericValue.Validators.StringifiedTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stringified_value"]
        ) -> typing.Callable[
            [GenericValue.Validators.StringifiedValueValidator], GenericValue.Validators.StringifiedValueValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "stringified_type":
                    cls._stringified_type_validators.append(validator)
                if field_name == "stringified_value":
                    cls._stringified_value_validators.append(validator)
                return validator

            return decorator

        class StringifiedTypeValidator(typing_extensions.Protocol):
            def __call__(self, v: typing.Optional[str], *, values: GenericValue.Partial) -> typing.Optional[str]:
                ...

        class StringifiedValueValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: GenericValue.Partial) -> str:
                ...

    @pydantic.validator("stringified_type")
    def _validate_stringified_type(cls, v: typing.Optional[str], values: GenericValue.Partial) -> typing.Optional[str]:
        for validator in GenericValue.Validators._stringified_type_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("stringified_value")
    def _validate_stringified_value(cls, v: str, values: GenericValue.Partial) -> str:
        for validator in GenericValue.Validators._stringified_value_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        stringified_type: typing_extensions.NotRequired[typing.Optional[str]]
        stringified_value: typing_extensions.NotRequired[str]

    class Config:
        frozen = True
        allow_population_by_field_name = True
