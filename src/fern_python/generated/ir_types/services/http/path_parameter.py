import typing

import pydantic
import typing_extensions

from ...commons.string_with_all_casings import StringWithAllCasings
from ...commons.with_docs import WithDocs
from ...types.type_reference import TypeReference


class PathParameter(WithDocs):
    name: StringWithAllCasings
    value_type: TypeReference = pydantic.Field(alias="valueType")

    @pydantic.validator("name")
    def _validate_name(cls, name: StringWithAllCasings) -> StringWithAllCasings:
        for validator in PathParameter.Validators._name:
            name = validator(name)
        return name

    @pydantic.validator("value_type")
    def _validate_value_type(cls, value_type: TypeReference) -> TypeReference:
        for validator in PathParameter.Validators._value_type:
            value_type = validator(value_type)
        return value_type

    class Validators:
        _name: typing.ClassVar[typing.List[typing.Callable[[StringWithAllCasings], StringWithAllCasings]]] = []
        _value_type: typing.ClassVar[typing.List[typing.Callable[[TypeReference], TypeReference]]] = []

        @typing.overload
        @classmethod
        def field(cls, field_name: typing_extensions.Literal["name"]) -> StringWithAllCasings:
            ...

        @typing.overload
        @classmethod
        def field(cls, field_name: typing_extensions.Literal["value_type"]) -> TypeReference:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "name":
                    cls._name.append(validator)
                elif field_name == "value_type":
                    cls._value_type.append(validator)
                else:
                    raise RuntimeError("Field does not exist on PathParameter: " + field_name)

                return validator

            return decorator

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
