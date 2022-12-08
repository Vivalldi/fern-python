# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.variable_type import VariableType
from .variable_type_and_name import VariableTypeAndName


class GetDefaultStarterFilesRequest(pydantic.BaseModel):
    input_params: typing.List[VariableTypeAndName] = pydantic.Field(alias="inputParams")
    output_type: VariableType = pydantic.Field(alias="outputType")
    method_name: str = pydantic.Field(alias="methodName")

    class Partial(typing_extensions.TypedDict):
        input_params: typing_extensions.NotRequired[typing.List[VariableTypeAndName]]
        output_type: typing_extensions.NotRequired[VariableType]
        method_name: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetDefaultStarterFilesRequest.Validators.root()
            def validate(values: GetDefaultStarterFilesRequest.Partial) -> GetDefaultStarterFilesRequest.Partial:
                ...

            @GetDefaultStarterFilesRequest.Validators.field("input_params")
            def validate_input_params(input_params: typing.List[VariableTypeAndName], values: GetDefaultStarterFilesRequest.Partial) -> typing.List[VariableTypeAndName]:
                ...

            @GetDefaultStarterFilesRequest.Validators.field("output_type")
            def validate_output_type(output_type: VariableType, values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
                ...

            @GetDefaultStarterFilesRequest.Validators.field("method_name")
            def validate_method_name(method_name: str, values: GetDefaultStarterFilesRequest.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GetDefaultStarterFilesRequest.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GetDefaultStarterFilesRequest.Validators._RootValidator]] = []
        _input_params_pre_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.InputParamsValidator]
        ] = []
        _input_params_post_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.InputParamsValidator]
        ] = []
        _output_type_pre_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.OutputTypeValidator]
        ] = []
        _output_type_post_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.OutputTypeValidator]
        ] = []
        _method_name_pre_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.MethodNameValidator]
        ] = []
        _method_name_post_validators: typing.ClassVar[
            typing.List[GetDefaultStarterFilesRequest.Validators.MethodNameValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators._RootValidator],
            GetDefaultStarterFilesRequest.Validators._RootValidator,
        ]:
            def decorator(
                validator: GetDefaultStarterFilesRequest.Validators._RootValidator,
            ) -> GetDefaultStarterFilesRequest.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["input_params"], *, pre: bool = False
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators.InputParamsValidator],
            GetDefaultStarterFilesRequest.Validators.InputParamsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["output_type"], *, pre: bool = False
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators.OutputTypeValidator],
            GetDefaultStarterFilesRequest.Validators.OutputTypeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: bool = False
        ) -> typing.Callable[
            [GetDefaultStarterFilesRequest.Validators.MethodNameValidator],
            GetDefaultStarterFilesRequest.Validators.MethodNameValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "input_params":
                    if pre:
                        cls._input_params_pre_validators.append(validator)
                    else:
                        cls._input_params_post_validators.append(validator)
                if field_name == "output_type":
                    if pre:
                        cls._output_type_pre_validators.append(validator)
                    else:
                        cls._output_type_post_validators.append(validator)
                if field_name == "method_name":
                    if pre:
                        cls._method_name_pre_validators.append(validator)
                    else:
                        cls._method_name_post_validators.append(validator)
                return validator

            return decorator

        class InputParamsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[VariableTypeAndName], __values: GetDefaultStarterFilesRequest.Partial
            ) -> typing.List[VariableTypeAndName]:
                ...

        class OutputTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GetDefaultStarterFilesRequest.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: GetDefaultStarterFilesRequest.Partial
            ) -> GetDefaultStarterFilesRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: GetDefaultStarterFilesRequest.Partial) -> GetDefaultStarterFilesRequest.Partial:
        for validator in GetDefaultStarterFilesRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: GetDefaultStarterFilesRequest.Partial) -> GetDefaultStarterFilesRequest.Partial:
        for validator in GetDefaultStarterFilesRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("input_params", pre=True)
    def _pre_validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: GetDefaultStarterFilesRequest.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in GetDefaultStarterFilesRequest.Validators._input_params_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("input_params", pre=False)
    def _post_validate_input_params(
        cls, v: typing.List[VariableTypeAndName], values: GetDefaultStarterFilesRequest.Partial
    ) -> typing.List[VariableTypeAndName]:
        for validator in GetDefaultStarterFilesRequest.Validators._input_params_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("output_type", pre=True)
    def _pre_validate_output_type(cls, v: VariableType, values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
        for validator in GetDefaultStarterFilesRequest.Validators._output_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("output_type", pre=False)
    def _post_validate_output_type(cls, v: VariableType, values: GetDefaultStarterFilesRequest.Partial) -> VariableType:
        for validator in GetDefaultStarterFilesRequest.Validators._output_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=True)
    def _pre_validate_method_name(cls, v: str, values: GetDefaultStarterFilesRequest.Partial) -> str:
        for validator in GetDefaultStarterFilesRequest.Validators._method_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=False)
    def _post_validate_method_name(cls, v: str, values: GetDefaultStarterFilesRequest.Partial) -> str:
        for validator in GetDefaultStarterFilesRequest.Validators._method_name_post_validators:
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
