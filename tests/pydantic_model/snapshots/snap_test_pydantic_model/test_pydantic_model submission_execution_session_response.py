# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from ..core.datetime_utils import serialize_datetime
from .execution_session_status import ExecutionSessionStatus


class ExecutionSessionResponse(pydantic.BaseModel):
    session_id: str = pydantic.Field(alias="sessionId")
    execution_session_url: typing.Optional[str] = pydantic.Field(alias="executionSessionUrl")
    language: Language
    status: ExecutionSessionStatus

    class Partial(typing_extensions.TypedDict):
        session_id: typing_extensions.NotRequired[str]
        execution_session_url: typing_extensions.NotRequired[typing.Optional[str]]
        language: typing_extensions.NotRequired[Language]
        status: typing_extensions.NotRequired[ExecutionSessionStatus]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExecutionSessionResponse.Validators.root()
            def validate(values: ExecutionSessionResponse.Partial) -> ExecutionSessionResponse.Partial:
                ...

            @ExecutionSessionResponse.Validators.field("session_id")
            def validate_session_id(session_id: str, values: ExecutionSessionResponse.Partial) -> str:
                ...

            @ExecutionSessionResponse.Validators.field("execution_session_url")
            def validate_execution_session_url(execution_session_url: typing.Optional[str], values: ExecutionSessionResponse.Partial) -> typing.Optional[str]:
                ...

            @ExecutionSessionResponse.Validators.field("language")
            def validate_language(language: Language, values: ExecutionSessionResponse.Partial) -> Language:
                ...

            @ExecutionSessionResponse.Validators.field("status")
            def validate_status(status: ExecutionSessionStatus, values: ExecutionSessionResponse.Partial) -> ExecutionSessionStatus:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ExecutionSessionResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ExecutionSessionResponse.Validators._RootValidator]] = []
        _session_id_pre_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.PreSessionIdValidator]
        ] = []
        _session_id_post_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.SessionIdValidator]
        ] = []
        _execution_session_url_pre_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.PreExecutionSessionUrlValidator]
        ] = []
        _execution_session_url_post_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.ExecutionSessionUrlValidator]
        ] = []
        _language_pre_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.PreLanguageValidator]
        ] = []
        _language_post_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.LanguageValidator]
        ] = []
        _status_pre_validators: typing.ClassVar[
            typing.List[ExecutionSessionResponse.Validators.PreStatusValidator]
        ] = []
        _status_post_validators: typing.ClassVar[typing.List[ExecutionSessionResponse.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators._RootValidator], ExecutionSessionResponse.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators._PreRootValidator],
            ExecutionSessionResponse.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["session_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.PreSessionIdValidator],
            ExecutionSessionResponse.Validators.PreSessionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["session_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.SessionIdValidator],
            ExecutionSessionResponse.Validators.SessionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["execution_session_url"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.PreExecutionSessionUrlValidator],
            ExecutionSessionResponse.Validators.PreExecutionSessionUrlValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["execution_session_url"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.ExecutionSessionUrlValidator],
            ExecutionSessionResponse.Validators.ExecutionSessionUrlValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.PreLanguageValidator],
            ExecutionSessionResponse.Validators.PreLanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.LanguageValidator],
            ExecutionSessionResponse.Validators.LanguageValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.PreStatusValidator],
            ExecutionSessionResponse.Validators.PreStatusValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExecutionSessionResponse.Validators.StatusValidator], ExecutionSessionResponse.Validators.StatusValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "session_id":
                    if pre:
                        cls._session_id_pre_validators.append(validator)
                    else:
                        cls._session_id_post_validators.append(validator)
                if field_name == "execution_session_url":
                    if pre:
                        cls._execution_session_url_pre_validators.append(validator)
                    else:
                        cls._execution_session_url_post_validators.append(validator)
                if field_name == "language":
                    if pre:
                        cls._language_pre_validators.append(validator)
                    else:
                        cls._language_post_validators.append(validator)
                if field_name == "status":
                    if pre:
                        cls._status_pre_validators.append(validator)
                    else:
                        cls._status_post_validators.append(validator)
                return validator

            return decorator

        class PreSessionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExecutionSessionResponse.Partial) -> typing.Any:
                ...

        class SessionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: ExecutionSessionResponse.Partial) -> str:
                ...

        class PreExecutionSessionUrlValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExecutionSessionResponse.Partial) -> typing.Any:
                ...

        class ExecutionSessionUrlValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: ExecutionSessionResponse.Partial
            ) -> typing.Optional[str]:
                ...

        class PreLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExecutionSessionResponse.Partial) -> typing.Any:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: ExecutionSessionResponse.Partial) -> Language:
                ...

        class PreStatusValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExecutionSessionResponse.Partial) -> typing.Any:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: ExecutionSessionStatus, __values: ExecutionSessionResponse.Partial
            ) -> ExecutionSessionStatus:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ExecutionSessionResponse.Partial) -> ExecutionSessionResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ExecutionSessionResponse.Partial) -> ExecutionSessionResponse.Partial:
        for validator in ExecutionSessionResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ExecutionSessionResponse.Partial) -> ExecutionSessionResponse.Partial:
        for validator in ExecutionSessionResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("session_id", pre=True)
    def _pre_validate_session_id(cls, v: str, values: ExecutionSessionResponse.Partial) -> str:
        for validator in ExecutionSessionResponse.Validators._session_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("session_id", pre=False)
    def _post_validate_session_id(cls, v: str, values: ExecutionSessionResponse.Partial) -> str:
        for validator in ExecutionSessionResponse.Validators._session_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("execution_session_url", pre=True)
    def _pre_validate_execution_session_url(
        cls, v: typing.Optional[str], values: ExecutionSessionResponse.Partial
    ) -> typing.Optional[str]:
        for validator in ExecutionSessionResponse.Validators._execution_session_url_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("execution_session_url", pre=False)
    def _post_validate_execution_session_url(
        cls, v: typing.Optional[str], values: ExecutionSessionResponse.Partial
    ) -> typing.Optional[str]:
        for validator in ExecutionSessionResponse.Validators._execution_session_url_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language", pre=True)
    def _pre_validate_language(cls, v: Language, values: ExecutionSessionResponse.Partial) -> Language:
        for validator in ExecutionSessionResponse.Validators._language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language", pre=False)
    def _post_validate_language(cls, v: Language, values: ExecutionSessionResponse.Partial) -> Language:
        for validator in ExecutionSessionResponse.Validators._language_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=True)
    def _pre_validate_status(
        cls, v: ExecutionSessionStatus, values: ExecutionSessionResponse.Partial
    ) -> ExecutionSessionStatus:
        for validator in ExecutionSessionResponse.Validators._status_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=False)
    def _post_validate_status(
        cls, v: ExecutionSessionStatus, values: ExecutionSessionResponse.Partial
    ) -> ExecutionSessionStatus:
        for validator in ExecutionSessionResponse.Validators._status_post_validators:
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
