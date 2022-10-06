import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from .execution_session_status import ExecutionSessionStatus


class ExecutionSessionState(pydantic.BaseModel):
    last_time_contacted: typing.Optional[str] = pydantic.Field(alias="lastTimeContacted")
    session_id: str = pydantic.Field(alias="sessionId")
    is_warm_instance: bool = pydantic.Field(alias="isWarmInstance")
    aws_task_id: typing.Optional[str] = pydantic.Field(alias="awsTaskId")
    language: Language
    status: ExecutionSessionStatus

    @pydantic.validator("last_time_contacted")
    def _validate_last_time_contacted(cls, last_time_contacted: typing.Optional[str]) -> typing.Optional[str]:
        for validator in ExecutionSessionState.Validators._last_time_contacted:
            last_time_contacted = validator(last_time_contacted)
        return last_time_contacted

    @pydantic.validator("session_id")
    def _validate_session_id(cls, session_id: str) -> str:
        for validator in ExecutionSessionState.Validators._session_id:
            session_id = validator(session_id)
        return session_id

    @pydantic.validator("is_warm_instance")
    def _validate_is_warm_instance(cls, is_warm_instance: bool) -> bool:
        for validator in ExecutionSessionState.Validators._is_warm_instance:
            is_warm_instance = validator(is_warm_instance)
        return is_warm_instance

    @pydantic.validator("aws_task_id")
    def _validate_aws_task_id(cls, aws_task_id: typing.Optional[str]) -> typing.Optional[str]:
        for validator in ExecutionSessionState.Validators._aws_task_id:
            aws_task_id = validator(aws_task_id)
        return aws_task_id

    @pydantic.validator("language")
    def _validate_language(cls, language: Language) -> Language:
        for validator in ExecutionSessionState.Validators._language:
            language = validator(language)
        return language

    @pydantic.validator("status")
    def _validate_status(cls, status: ExecutionSessionStatus) -> ExecutionSessionStatus:
        for validator in ExecutionSessionState.Validators._status:
            status = validator(status)
        return status

    class Validators:
        _last_time_contacted: typing.ClassVar[typing.Optional[str]] = []
        _session_id: typing.ClassVar[str] = []
        _is_warm_instance: typing.ClassVar[bool] = []
        _aws_task_id: typing.ClassVar[typing.Optional[str]] = []
        _language: typing.ClassVar[Language] = []
        _status: typing.ClassVar[ExecutionSessionStatus] = []

        @typing.overload
        @classmethod
        def field(last_time_contacted: typing_extensions.Literal["last_time_contacted"]) -> typing.Optional[str]:
            ...

        @typing.overload
        @classmethod
        def field(session_id: typing_extensions.Literal["session_id"]) -> str:
            ...

        @typing.overload
        @classmethod
        def field(is_warm_instance: typing_extensions.Literal["is_warm_instance"]) -> bool:
            ...

        @typing.overload
        @classmethod
        def field(aws_task_id: typing_extensions.Literal["aws_task_id"]) -> typing.Optional[str]:
            ...

        @typing.overload
        @classmethod
        def field(language: typing_extensions.Literal["language"]) -> Language:
            ...

        @typing.overload
        @classmethod
        def field(status: typing_extensions.Literal["status"]) -> ExecutionSessionStatus:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "last_time_contacted":
                    cls._last_time_contacted.append(validator)  # type: ignore
                elif field_name == "session_id":
                    cls._session_id.append(validator)  # type: ignore
                elif field_name == "is_warm_instance":
                    cls._is_warm_instance.append(validator)  # type: ignore
                elif field_name == "aws_task_id":
                    cls._aws_task_id.append(validator)  # type: ignore
                elif field_name == "language":
                    cls._language.append(validator)  # type: ignore
                elif field_name == "status":
                    cls._status.append(validator)  # type: ignore
                else:
                    raise RuntimeError("Field does not exist on ExecutionSessionState: " + field_name)

                return validator

            return validator  # type: ignore

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
