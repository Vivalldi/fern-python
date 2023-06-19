# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...commons.types.variable_type import VariableType


class VariableTypeAndName(pydantic.BaseModel):
    variable_type: VariableType = pydantic.Field(alias="variableType")
    name: str

    class Partial(typing_extensions.TypedDict):
        variable_type: typing_extensions.NotRequired[VariableType]
        name: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VariableTypeAndName.Validators.root()
            def validate(values: VariableTypeAndName.Partial) -> VariableTypeAndName.Partial:
                ...

            @VariableTypeAndName.Validators.field("variable_type")
            def validate_variable_type(variable_type: VariableType, values: VariableTypeAndName.Partial) -> VariableType:
                ...

            @VariableTypeAndName.Validators.field("name")
            def validate_name(name: str, values: VariableTypeAndName.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[VariableTypeAndName.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[VariableTypeAndName.Validators._RootValidator]] = []
        _variable_type_pre_validators: typing.ClassVar[
            typing.List[VariableTypeAndName.Validators.PreVariableTypeValidator]
        ] = []
        _variable_type_post_validators: typing.ClassVar[
            typing.List[VariableTypeAndName.Validators.VariableTypeValidator]
        ] = []
        _name_pre_validators: typing.ClassVar[typing.List[VariableTypeAndName.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[VariableTypeAndName.Validators.NameValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [VariableTypeAndName.Validators._RootValidator], VariableTypeAndName.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VariableTypeAndName.Validators._PreRootValidator], VariableTypeAndName.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["variable_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VariableTypeAndName.Validators.PreVariableTypeValidator],
            VariableTypeAndName.Validators.PreVariableTypeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["variable_type"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [VariableTypeAndName.Validators.VariableTypeValidator], VariableTypeAndName.Validators.VariableTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VariableTypeAndName.Validators.PreNameValidator], VariableTypeAndName.Validators.PreNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [VariableTypeAndName.Validators.NameValidator], VariableTypeAndName.Validators.NameValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "variable_type":
                    if pre:
                        cls._variable_type_pre_validators.append(validator)
                    else:
                        cls._variable_type_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                return validator

            return decorator

        class PreVariableTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: VariableTypeAndName.Partial) -> typing.Any:
                ...

        class VariableTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: VariableTypeAndName.Partial) -> VariableType:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: VariableTypeAndName.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: VariableTypeAndName.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: VariableTypeAndName.Partial) -> VariableTypeAndName.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _prevariable_type_and_name_validate(cls, values: VariableTypeAndName.Partial) -> VariableTypeAndName.Partial:
        for validator in VariableTypeAndName.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postvariable_type_and_name_validate(cls, values: VariableTypeAndName.Partial) -> VariableTypeAndName.Partial:
        for validator in VariableTypeAndName.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("variable_type", pre=True)
    def _pre_validate_variable_type(cls, v: VariableType, values: VariableTypeAndName.Partial) -> VariableType:
        for validator in VariableTypeAndName.Validators._variable_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("variable_type", pre=False)
    def _post_validate_variable_type(cls, v: VariableType, values: VariableTypeAndName.Partial) -> VariableType:
        for validator in VariableTypeAndName.Validators._variable_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: VariableTypeAndName.Partial) -> str:
        for validator in VariableTypeAndName.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: VariableTypeAndName.Partial) -> str:
        for validator in VariableTypeAndName.Validators._name_post_validators:
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
