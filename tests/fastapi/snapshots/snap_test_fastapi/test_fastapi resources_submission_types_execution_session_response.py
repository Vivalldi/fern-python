# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.language import Language
from .execution_session_status import ExecutionSessionStatus


class ExecutionSessionResponse(pydantic.BaseModel):
    session_id: str = pydantic.Field(alias="sessionId")
    execution_session_url: typing.Optional[str] = pydantic.Field(alias="executionSessionUrl")
    language: Language
    status: ExecutionSessionStatus

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExecutionSessionResponse.Validators.field("session_id")
            def validate_session_id(v: str, values: ExecutionSessionResponse.Partial) -> str:
                ...

            @ExecutionSessionResponse.Validators.field("execution_session_url")
            def validate_execution_session_url(v: typing.Optional[str], values: ExecutionSessionResponse.Partial) -> typing.Optional[str]:
                ...

            @ExecutionSessionResponse.Validators.field("language")
            def validate_language(v: Language, values: ExecutionSessionResponse.Partial) -> Language:
                ...

            @ExecutionSessionResponse.Validators.field("status")
            def validate_status(v: ExecutionSessionStatus, values: ExecutionSessionResponse.Partial) -> ExecutionSessionStatus:
                ...
        """

        _session_id_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.SessionIdValidator]
        ] = []
        _execution_session_url_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.ExecutionSessionUrlValidator]
        ] = []
        _language_validators: typing.ClassVar[typing.List[ExecutionSessionResponse.Validators.LanguageValidator]] = []
        _status_validators: typing.ClassVar[typing.List[ExecutionSessionResponse.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["session_id"]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.SessionIdValidator],
            ExecutionSessionResponse.Validators.SessionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["execution_session_url"]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.ExecutionSessionUrlValidator],
            ExecutionSessionResponse.Validators.ExecutionSessionUrlValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.LanguageValidator],
            ExecutionSessionResponse.Validators.LanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.StatusValidator], ExecutionSessionResponse.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "session_id":
                    cls._session_id_validators.append(validator)
                if field_name == "execution_session_url":
                    cls._execution_session_url_validators.append(validator)
                if field_name == "language":
                    cls._language_validators.append(validator)
                if field_name == "status":
                    cls._status_validators.append(validator)
                return validator

            return decorator

        class SessionIdValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: ExecutionSessionResponse.Partial) -> str:
                ...

        class ExecutionSessionUrlValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[str], *, values: ExecutionSessionResponse.Partial
            ) -> typing.Optional[str]:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, v: Language, *, values: ExecutionSessionResponse.Partial) -> Language:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, v: ExecutionSessionStatus, *, values: ExecutionSessionResponse.Partial
            ) -> ExecutionSessionStatus:
                ...

    @pydantic.validator("session_id")
    def _validate_session_id(cls, v: str, values: ExecutionSessionResponse.Partial) -> str:
        for validator in ExecutionSessionResponse.Validators._session_id_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("execution_session_url")
    def _validate_execution_session_url(
        cls, v: typing.Optional[str], values: ExecutionSessionResponse.Partial
    ) -> typing.Optional[str]:
        for validator in ExecutionSessionResponse.Validators._execution_session_url_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("language")
    def _validate_language(cls, v: Language, values: ExecutionSessionResponse.Partial) -> Language:
        for validator in ExecutionSessionResponse.Validators._language_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("status")
    def _validate_status(
        cls, v: ExecutionSessionStatus, values: ExecutionSessionResponse.Partial
    ) -> ExecutionSessionStatus:
        for validator in ExecutionSessionResponse.Validators._status_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        session_id: typing_extensions.NotRequired[str]
        execution_session_url: typing_extensions.NotRequired[typing.Optional[str]]
        language: typing_extensions.NotRequired[Language]
        status: typing_extensions.NotRequired[ExecutionSessionStatus]

    class Config:
        frozen = True
        allow_population_by_field_name = True
