# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


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

            @GenericCreateProblemError.Validators.root
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

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[GenericCreateProblemError.Partial], GenericCreateProblemError.Partial]]
        ] = []
        _message_validators: typing.ClassVar[typing.List[GenericCreateProblemError.Validators.MessageValidator]] = []
        _type_validators: typing.ClassVar[typing.List[GenericCreateProblemError.Validators.TypeValidator]] = []
        _stacktrace_validators: typing.ClassVar[
            typing.List[GenericCreateProblemError.Validators.StacktraceValidator]
        ] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[GenericCreateProblemError.Partial], GenericCreateProblemError.Partial]
        ) -> typing.Callable[[GenericCreateProblemError.Partial], GenericCreateProblemError.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["message"]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.MessageValidator],
            GenericCreateProblemError.Validators.MessageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["type"]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.TypeValidator], GenericCreateProblemError.Validators.TypeValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stacktrace"]
        ) -> typing.Callable[
            [GenericCreateProblemError.Validators.StacktraceValidator],
            GenericCreateProblemError.Validators.StacktraceValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "message":
                    cls._message_validators.append(validator)
                if field_name == "type":
                    cls._type_validators.append(validator)
                if field_name == "stacktrace":
                    cls._stacktrace_validators.append(validator)
                return validator

            return decorator

        class MessageValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericCreateProblemError.Partial) -> str:
                ...

        class TypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericCreateProblemError.Partial) -> str:
                ...

        class StacktraceValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: GenericCreateProblemError.Partial) -> str:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GenericCreateProblemError.Partial) -> GenericCreateProblemError.Partial:
        for validator in GenericCreateProblemError.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("message")
    def _validate_message(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._message_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("type")
    def _validate_type(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._type_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stacktrace")
    def _validate_stacktrace(cls, v: str, values: GenericCreateProblemError.Partial) -> str:
        for validator in GenericCreateProblemError.Validators._stacktrace_validators:
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
