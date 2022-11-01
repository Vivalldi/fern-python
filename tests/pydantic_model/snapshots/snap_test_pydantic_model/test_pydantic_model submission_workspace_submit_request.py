# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.language import Language
from .submission_file_info import SubmissionFileInfo
from .submission_id import SubmissionId


class WorkspaceSubmitRequest(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    language: Language
    submission_files: typing.List[SubmissionFileInfo] = pydantic.Field(alias="submissionFiles")
    user_id: typing.Optional[str] = pydantic.Field(alias="userId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        language: typing_extensions.NotRequired[Language]
        submission_files: typing_extensions.NotRequired[typing.List[SubmissionFileInfo]]
        user_id: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceSubmitRequest.Validators.root
            def validate(values: WorkspaceSubmitRequest.Partial) -> WorkspaceSubmitRequest.Partial:
                ...

            @WorkspaceSubmitRequest.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
                ...

            @WorkspaceSubmitRequest.Validators.field("language")
            def validate_language(language: Language, values: WorkspaceSubmitRequest.Partial) -> Language:
                ...

            @WorkspaceSubmitRequest.Validators.field("submission_files")
            def validate_submission_files(submission_files: typing.List[SubmissionFileInfo], values: WorkspaceSubmitRequest.Partial) -> typing.List[SubmissionFileInfo]:
                ...

            @WorkspaceSubmitRequest.Validators.field("user_id")
            def validate_user_id(user_id: typing.Optional[str], values: WorkspaceSubmitRequest.Partial) -> typing.Optional[str]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[WorkspaceSubmitRequest.Partial], WorkspaceSubmitRequest.Partial]]
        ] = []
        _submission_id_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.SubmissionIdValidator]
        ] = []
        _language_validators: typing.ClassVar[typing.List[WorkspaceSubmitRequest.Validators.LanguageValidator]] = []
        _submission_files_validators: typing.ClassVar[
            typing.List[WorkspaceSubmitRequest.Validators.SubmissionFilesValidator]
        ] = []
        _user_id_validators: typing.ClassVar[typing.List[WorkspaceSubmitRequest.Validators.UserIdValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[WorkspaceSubmitRequest.Partial], WorkspaceSubmitRequest.Partial]
        ) -> typing.Callable[[WorkspaceSubmitRequest.Partial], WorkspaceSubmitRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.SubmissionIdValidator],
            WorkspaceSubmitRequest.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.LanguageValidator], WorkspaceSubmitRequest.Validators.LanguageValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_files"]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.SubmissionFilesValidator],
            WorkspaceSubmitRequest.Validators.SubmissionFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"]
        ) -> typing.Callable[
            [WorkspaceSubmitRequest.Validators.UserIdValidator], WorkspaceSubmitRequest.Validators.UserIdValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    cls._submission_id_validators.append(validator)
                if field_name == "language":
                    cls._language_validators.append(validator)
                if field_name == "submission_files":
                    cls._submission_files_validators.append(validator)
                if field_name == "user_id":
                    cls._user_id_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: WorkspaceSubmitRequest.Partial) -> Language:
                ...

        class SubmissionFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[SubmissionFileInfo], __values: WorkspaceSubmitRequest.Partial
            ) -> typing.List[SubmissionFileInfo]:
                ...

        class UserIdValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[str], __values: WorkspaceSubmitRequest.Partial
            ) -> typing.Optional[str]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: WorkspaceSubmitRequest.Partial) -> WorkspaceSubmitRequest.Partial:
        for validator in WorkspaceSubmitRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id")
    def _validate_submission_id(cls, v: SubmissionId, values: WorkspaceSubmitRequest.Partial) -> SubmissionId:
        for validator in WorkspaceSubmitRequest.Validators._submission_id_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language")
    def _validate_language(cls, v: Language, values: WorkspaceSubmitRequest.Partial) -> Language:
        for validator in WorkspaceSubmitRequest.Validators._language_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_files")
    def _validate_submission_files(
        cls, v: typing.List[SubmissionFileInfo], values: WorkspaceSubmitRequest.Partial
    ) -> typing.List[SubmissionFileInfo]:
        for validator in WorkspaceSubmitRequest.Validators._submission_files_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("user_id")
    def _validate_user_id(cls, v: typing.Optional[str], values: WorkspaceSubmitRequest.Partial) -> typing.Optional[str]:
        for validator in WorkspaceSubmitRequest.Validators._user_id_validators:
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
