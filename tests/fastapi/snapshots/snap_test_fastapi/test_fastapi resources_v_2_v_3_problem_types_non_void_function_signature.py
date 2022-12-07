# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .....commons.types.variable_type import VariableType
from .parameter import Parameter


class NonVoidFunctionSignature(pydantic.BaseModel):
    parameters: typing.List[Parameter]
    return_type: VariableType = pydantic.Field(alias="returnType")

    class Partial(typing_extensions.TypedDict):
        parameters: typing_extensions.NotRequired[typing.List[Parameter]]
        return_type: typing_extensions.NotRequired[VariableType]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @NonVoidFunctionSignature.Validators.root
            def validate(values: NonVoidFunctionSignature.Partial) -> NonVoidFunctionSignature.Partial:
                ...

            @NonVoidFunctionSignature.Validators.field("parameters")
            def validate_parameters(parameters: typing.List[Parameter], values: NonVoidFunctionSignature.Partial) -> typing.List[Parameter]:
                ...

            @NonVoidFunctionSignature.Validators.field("return_type")
            def validate_return_type(return_type: VariableType, values: NonVoidFunctionSignature.Partial) -> VariableType:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[NonVoidFunctionSignature.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[NonVoidFunctionSignature.Validators._RootValidator]] = []
        _parameters_pre_validators: typing.ClassVar[
            typing.List[NonVoidFunctionSignature.Validators.ParametersValidator]
        ] = []
        _parameters_post_validators: typing.ClassVar[
            typing.List[NonVoidFunctionSignature.Validators.ParametersValidator]
        ] = []
        _return_type_pre_validators: typing.ClassVar[
            typing.List[NonVoidFunctionSignature.Validators.ReturnTypeValidator]
        ] = []
        _return_type_post_validators: typing.ClassVar[
            typing.List[NonVoidFunctionSignature.Validators.ReturnTypeValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> NonVoidFunctionSignature.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["parameters"], *, pre: bool
        ) -> typing.Callable[
            [NonVoidFunctionSignature.Validators.ParametersValidator],
            NonVoidFunctionSignature.Validators.ParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["return_type"], *, pre: bool
        ) -> typing.Callable[
            [NonVoidFunctionSignature.Validators.ReturnTypeValidator],
            NonVoidFunctionSignature.Validators.ReturnTypeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameters":
                    if pre:
                        cls._parameters_pre_validators.append(validator)
                    else:
                        cls._parameters_post_validators.append(validator)
                if field_name == "return_type":
                    if pre:
                        cls._return_type_pre_validators.append(validator)
                    else:
                        cls._return_type_post_validators.append(validator)
                return validator

            return decorator

        class ParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[Parameter], __values: NonVoidFunctionSignature.Partial
            ) -> typing.List[Parameter]:
                ...

        class ReturnTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: NonVoidFunctionSignature.Partial) -> VariableType:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: NonVoidFunctionSignature.Partial) -> NonVoidFunctionSignature.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: NonVoidFunctionSignature.Partial) -> NonVoidFunctionSignature.Partial:
        for validator in NonVoidFunctionSignature.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: NonVoidFunctionSignature.Partial) -> NonVoidFunctionSignature.Partial:
        for validator in NonVoidFunctionSignature.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("parameters", pre=True)
    def _pre_validate_parameters(
        cls, v: typing.List[Parameter], values: NonVoidFunctionSignature.Partial
    ) -> typing.List[Parameter]:
        for validator in NonVoidFunctionSignature.Validators._parameters_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("parameters", pre=False)
    def _post_validate_parameters(
        cls, v: typing.List[Parameter], values: NonVoidFunctionSignature.Partial
    ) -> typing.List[Parameter]:
        for validator in NonVoidFunctionSignature.Validators._parameters_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("return_type", pre=True)
    def _pre_validate_return_type(cls, v: VariableType, values: NonVoidFunctionSignature.Partial) -> VariableType:
        for validator in NonVoidFunctionSignature.Validators._return_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("return_type", pre=False)
    def _post_validate_return_type(cls, v: VariableType, values: NonVoidFunctionSignature.Partial) -> VariableType:
        for validator in NonVoidFunctionSignature.Validators._return_type_post_validators:
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
