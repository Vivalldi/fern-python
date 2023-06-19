# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class GenericCreateProblemError(pydantic.BaseModel):
    message: str
    type: str
    stacktrace: str

    class Partial(typing_extensions.TypedDict):
        message: typing_extensions.NotRequired[str]
        type: typing_extensions.NotRequired[str]
        stacktrace: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GenericCreateProblemError.Validators.root()
            def validate(values: GenericCreateProblemError.Partial) -> GenericCreateProblemError.Partial:
                ...

            @GenericCreateProblemError.Validators.field("message")
            def validate_message(message: str, values: GenericCreateProblemError.Partial) -> str:
                ...

            @GenericCreateProblemError.Validators.field("type")
            def validate_type(type: str, values: GenericCreateProblemError.Partial) -> str:
                ...

            @GenericCreateProblemError.Validators.field("stacktrace")
            def validate_stacktrace(stacktrace: str, values: GenericCreateProblemError.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[GenericCreateProblemError.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[GenericCreateProblemError.Validators._RootValidator]] = []
        _message_pre_validators: typing.ClassVar[
            typing.List[GenericCreateProblemError.Validators.PreMessageValidator]
        ] = []
        _message_post_validators: typing.ClassVar[
            typing.List[GenericCreateProblemError.Validators.MessageValidator]
        ] = []
        _type_pre_validators: typing.ClassVar[typing.List[GenericCreateProblemError.Validators.PreTypeValidator]] = []
        _type_post_validators: typing.ClassVar[typing.List[GenericCreateProblemError.Validators.TypeValidator]] = []
        _stacktrace_pre_validators: typing.ClassVar[
            typing.List[GenericCreateProblemError.Validators.PreStacktraceValidator]
        ] = []
        _stacktrace_post_validators: typing.ClassVar[
            typing.List[GenericCreateProblemError.Validators.StacktraceValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators._RootValidator], GenericCreateProblemError.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators._PreRootValidator],
            GenericCreateProblemError.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["message"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.PreMessageValidator],
            GenericCreateProblemError.Validators.PreMessageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["message"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.MessageValidator],
            GenericCreateProblemError.Validators.MessageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.PreTypeValidator],
            GenericCreateProblemError.Validators.PreTypeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["type"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.TypeValidator], GenericCreateProblemError.Validators.TypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stacktrace"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.PreStacktraceValidator],
            GenericCreateProblemError.Validators.PreStacktraceValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stacktrace"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.StacktraceValidator],
            GenericCreateProblemError.Validators.StacktraceValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "message":
                    if pre:
                        cls._message_pre_validators.append(validator)
                    else:
                        cls._message_post_validators.append(validator)
                if field_name == "type":
                    if pre:
                        cls._type_pre_validators.append(validator)
                    else:
                        cls._type_post_validators.append(validator)
                if field_name == "stacktrace":
                    if pre:
                        cls._stacktrace_pre_validators.append(validator)
                    else:
                        cls._stacktrace_post_validators.append(validator)
                return validator

            return decorator

        class PreMessageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GenericCreateProblemError.Partial) -> typing.Any:
                ...

        class MessageValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericCreateProblemError.Partial) -> str:
                ...

        class PreTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GenericCreateProblemError.Partial) -> typing.Any:
                ...

        class TypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericCreateProblemError.Partial) -> str:
                ...

        class PreStacktraceValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GenericCreateProblemError.Partial) -> typing.Any:
                ...

        class StacktraceValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericCreateProblemError.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: GenericCreateProblemError.Partial) -> GenericCreateProblemError.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pregeneric_create_problem_error_validate(
        cls, values: GenericCreateProblemError.Partial
    ) -> GenericCreateProblemError.Partial:
        for validator in GenericCreateProblemError.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postgeneric_create_problem_error_validate(
        cls, values: GenericCreateProblemError.Partial
    ) -> GenericCreateProblemError.Partial:
        for validator in GenericCreateProblemError.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("message", pre=True)
    def _pre_validate_message(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._message_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("message", pre=False)
    def _post_validate_message(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._message_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("type", pre=True)
    def _pre_validate_type(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("type", pre=False)
    def _post_validate_type(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stacktrace", pre=True)
    def _pre_validate_stacktrace(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._stacktrace_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stacktrace", pre=False)
    def _post_validate_stacktrace(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._stacktrace_post_validators:
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
