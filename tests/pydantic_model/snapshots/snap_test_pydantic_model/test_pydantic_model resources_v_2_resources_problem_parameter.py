# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime
from ....commons.variable_type import VariableType
from .parameter_id import ParameterId


class Parameter(pydantic.BaseModel):
    parameter_id: ParameterId = pydantic.Field(alias="parameterId")
    name: str
    variable_type: VariableType = pydantic.Field(alias="variableType")

    class Partial(typing_extensions.TypedDict):
        parameter_id: typing_extensions.NotRequired[ParameterId]
        name: typing_extensions.NotRequired[str]
        variable_type: typing_extensions.NotRequired[VariableType]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Parameter.Validators.root()
            def validate(values: Parameter.Partial) -> Parameter.Partial:
                ...

            @Parameter.Validators.field("parameter_id")
            def validate_parameter_id(parameter_id: ParameterId, values: Parameter.Partial) -> ParameterId:
                ...

            @Parameter.Validators.field("name")
            def validate_name(name: str, values: Parameter.Partial) -> str:
                ...

            @Parameter.Validators.field("variable_type")
            def validate_variable_type(variable_type: VariableType, values: Parameter.Partial) -> VariableType:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Parameter.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Parameter.Validators._RootValidator]] = []
        _parameter_id_pre_validators: typing.ClassVar[typing.List[Parameter.Validators.PreParameterIdValidator]] = []
        _parameter_id_post_validators: typing.ClassVar[typing.List[Parameter.Validators.ParameterIdValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[Parameter.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[Parameter.Validators.NameValidator]] = []
        _variable_type_pre_validators: typing.ClassVar[typing.List[Parameter.Validators.PreVariableTypeValidator]] = []
        _variable_type_post_validators: typing.ClassVar[typing.List[Parameter.Validators.VariableTypeValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Parameter.Validators._RootValidator], Parameter.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Parameter.Validators._PreRootValidator], Parameter.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["parameter_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [Parameter.Validators.PreParameterIdValidator], Parameter.Validators.PreParameterIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameter_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Parameter.Validators.ParameterIdValidator], Parameter.Validators.ParameterIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Parameter.Validators.PreNameValidator], Parameter.Validators.PreNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Parameter.Validators.NameValidator], Parameter.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["variable_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [Parameter.Validators.PreVariableTypeValidator], Parameter.Validators.PreVariableTypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["variable_type"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[[Parameter.Validators.VariableTypeValidator], Parameter.Validators.VariableTypeValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameter_id":
                    if pre:
                        cls._parameter_id_pre_validators.append(validator)
                    else:
                        cls._parameter_id_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "variable_type":
                    if pre:
                        cls._variable_type_pre_validators.append(validator)
                    else:
                        cls._variable_type_post_validators.append(validator)
                return validator

            return decorator

        class PreParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Parameter.Partial) -> typing.Any:
                ...

        class ParameterIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ParameterId, __values: Parameter.Partial) -> ParameterId:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Parameter.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: Parameter.Partial) -> str:
                ...

        class PreVariableTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Parameter.Partial) -> typing.Any:
                ...

        class VariableTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: Parameter.Partial) -> VariableType:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Parameter.Partial) -> Parameter.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _prev_2_parameter_validate(cls, values: Parameter.Partial) -> Parameter.Partial:
        for validator in Parameter.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postv_2_parameter_validate(cls, values: Parameter.Partial) -> Parameter.Partial:
        for validator in Parameter.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("parameter_id", pre=True)
    def _pre_validate_parameter_id(cls, v: ParameterId, values: Parameter.Partial) -> ParameterId:
        for validator in Parameter.Validators._parameter_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("parameter_id", pre=False)
    def _post_validate_parameter_id(cls, v: ParameterId, values: Parameter.Partial) -> ParameterId:
        for validator in Parameter.Validators._parameter_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: Parameter.Partial) -> str:
        for validator in Parameter.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: Parameter.Partial) -> str:
        for validator in Parameter.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("variable_type", pre=True)
    def _pre_validate_variable_type(cls, v: VariableType, values: Parameter.Partial) -> VariableType:
        for validator in Parameter.Validators._variable_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("variable_type", pre=False)
    def _post_validate_variable_type(cls, v: VariableType, values: Parameter.Partial) -> VariableType:
        for validator in Parameter.Validators._variable_type_post_validators:
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
