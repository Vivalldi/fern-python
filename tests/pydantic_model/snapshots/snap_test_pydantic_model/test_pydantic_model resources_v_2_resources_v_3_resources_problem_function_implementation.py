# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .......core.datetime_utils import serialize_datetime


class FunctionImplementation(pydantic.BaseModel):
    impl: str
    imports: typing.Optional[str]

    class Partial(typing_extensions.TypedDict):
        impl: typing_extensions.NotRequired[str]
        imports: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FunctionImplementation.Validators.root()
            def validate(values: FunctionImplementation.Partial) -> FunctionImplementation.Partial:
                ...

            @FunctionImplementation.Validators.field("impl")
            def validate_impl(impl: str, values: FunctionImplementation.Partial) -> str:
                ...

            @FunctionImplementation.Validators.field("imports")
            def validate_imports(imports: typing.Optional[str], values: FunctionImplementation.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators._RootValidator]] = []
        _impl_pre_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators.PreImplValidator]] = []
        _impl_post_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators.ImplValidator]] = []
        _imports_pre_validators: typing.ClassVar[
            typing.List[FunctionImplementation.Validators.PreImportsValidator]
        ] = []
        _imports_post_validators: typing.ClassVar[typing.List[FunctionImplementation.Validators.ImportsValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [FunctionImplementation.Validators._RootValidator], FunctionImplementation.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [FunctionImplementation.Validators._PreRootValidator], FunctionImplementation.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["impl"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [FunctionImplementation.Validators.PreImplValidator], FunctionImplementation.Validators.PreImplValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["impl"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [FunctionImplementation.Validators.ImplValidator], FunctionImplementation.Validators.ImplValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["imports"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [FunctionImplementation.Validators.PreImportsValidator],
            FunctionImplementation.Validators.PreImportsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["imports"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [FunctionImplementation.Validators.ImportsValidator], FunctionImplementation.Validators.ImportsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "impl":
                    if pre:
                        cls._impl_pre_validators.append(validator)
                    else:
                        cls._impl_post_validators.append(validator)
                if field_name == "imports":
                    if pre:
                        cls._imports_pre_validators.append(validator)
                    else:
                        cls._imports_post_validators.append(validator)
                return validator

            return decorator

        class PreImplValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: FunctionImplementation.Partial) -> typing.Any:
                ...

        class ImplValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FunctionImplementation.Partial) -> str:
                ...

        class PreImportsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: FunctionImplementation.Partial) -> typing.Any:
                ...

        class ImportsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: FunctionImplementation.Partial
            ) -> typing.Optional[str]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: FunctionImplementation.Partial) -> FunctionImplementation.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _prev_2_v_3_function_implementation_validate(
        cls, values: FunctionImplementation.Partial
    ) -> FunctionImplementation.Partial:
        for validator in FunctionImplementation.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postv_2_v_3_function_implementation_validate(
        cls, values: FunctionImplementation.Partial
    ) -> FunctionImplementation.Partial:
        for validator in FunctionImplementation.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("impl", pre=True)
    def _pre_validate_impl(cls, v: str, values: FunctionImplementation.Partial) -> str:
        for validator in FunctionImplementation.Validators._impl_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("impl", pre=False)
    def _post_validate_impl(cls, v: str, values: FunctionImplementation.Partial) -> str:
        for validator in FunctionImplementation.Validators._impl_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("imports", pre=True)
    def _pre_validate_imports(
        cls, v: typing.Optional[str], values: FunctionImplementation.Partial
    ) -> typing.Optional[str]:
        for validator in FunctionImplementation.Validators._imports_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("imports", pre=False)
    def _post_validate_imports(
        cls, v: typing.Optional[str], values: FunctionImplementation.Partial
    ) -> typing.Optional[str]:
        for validator in FunctionImplementation.Validators._imports_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        json_encoders = {dt.datetime: serialize_datetime}
