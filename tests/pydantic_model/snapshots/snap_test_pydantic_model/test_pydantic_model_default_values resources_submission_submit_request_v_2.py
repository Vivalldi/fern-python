# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from ..commons.language import Language
from ..commons.problem_id import ProblemId
from .submission_file_info import SubmissionFileInfo
from .submission_id import SubmissionId


class SubmitRequestV2(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    language: Language
    submission_files: typing.List[SubmissionFileInfo] = pydantic.Field(alias="submissionFiles")
    problem_id: ProblemId = pydantic.Field(alias="problemId")
    problem_version: typing.Optional[int] = pydantic.Field(alias="problemVersion", default=None)
    user_id: typing.Optional[str] = pydantic.Field(alias="userId", default=None)

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        language: typing_extensions.NotRequired[Language]
        submission_files: typing_extensions.NotRequired[typing.List[SubmissionFileInfo]]
        problem_id: typing_extensions.NotRequired[ProblemId]
        problem_version: typing_extensions.NotRequired[typing.Optional[int]]
        user_id: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmitRequestV2.Validators.root()
            def validate(values: SubmitRequestV2.Partial) -> SubmitRequestV2.Partial:
                ...

            @SubmitRequestV2.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: SubmitRequestV2.Partial) -> SubmissionId:
                ...

            @SubmitRequestV2.Validators.field("language")
            def validate_language(language: Language, values: SubmitRequestV2.Partial) -> Language:
                ...

            @SubmitRequestV2.Validators.field("submission_files")
            def validate_submission_files(submission_files: typing.List[SubmissionFileInfo], values: SubmitRequestV2.Partial) -> typing.List[SubmissionFileInfo]:
                ...

            @SubmitRequestV2.Validators.field("problem_id")
            def validate_problem_id(problem_id: ProblemId, values: SubmitRequestV2.Partial) -> ProblemId:
                ...

            @SubmitRequestV2.Validators.field("problem_version")
            def validate_problem_version(problem_version: typing.Optional[int], values: SubmitRequestV2.Partial) -> typing.Optional[int]:
                ...

            @SubmitRequestV2.Validators.field("user_id")
            def validate_user_id(user_id: typing.Optional[str], values: SubmitRequestV2.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[SubmitRequestV2.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[SubmitRequestV2.Validators.SubmissionIdValidator]
        ] = []
        _language_pre_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators.PreLanguageValidator]] = []
        _language_post_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators.LanguageValidator]] = []
        _submission_files_pre_validators: typing.ClassVar[
            typing.List[SubmitRequestV2.Validators.PreSubmissionFilesValidator]
        ] = []
        _submission_files_post_validators: typing.ClassVar[
            typing.List[SubmitRequestV2.Validators.SubmissionFilesValidator]
        ] = []
        _problem_id_pre_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators.PreProblemIdValidator]] = []
        _problem_id_post_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators.ProblemIdValidator]] = []
        _problem_version_pre_validators: typing.ClassVar[
            typing.List[SubmitRequestV2.Validators.PreProblemVersionValidator]
        ] = []
        _problem_version_post_validators: typing.ClassVar[
            typing.List[SubmitRequestV2.Validators.ProblemVersionValidator]
        ] = []
        _user_id_pre_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators.PreUserIdValidator]] = []
        _user_id_post_validators: typing.ClassVar[typing.List[SubmitRequestV2.Validators.UserIdValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[SubmitRequestV2.Validators._RootValidator], SubmitRequestV2.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators._PreRootValidator], SubmitRequestV2.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.PreSubmissionIdValidator], SubmitRequestV2.Validators.PreSubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.SubmissionIdValidator], SubmitRequestV2.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.PreLanguageValidator], SubmitRequestV2.Validators.PreLanguageValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["language"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.LanguageValidator], SubmitRequestV2.Validators.LanguageValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.PreSubmissionFilesValidator],
            SubmitRequestV2.Validators.PreSubmissionFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.SubmissionFilesValidator], SubmitRequestV2.Validators.SubmissionFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.PreProblemIdValidator], SubmitRequestV2.Validators.PreProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.ProblemIdValidator], SubmitRequestV2.Validators.ProblemIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_version"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.PreProblemVersionValidator],
            SubmitRequestV2.Validators.PreProblemVersionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["problem_version"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.ProblemVersionValidator], SubmitRequestV2.Validators.ProblemVersionValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [SubmitRequestV2.Validators.PreUserIdValidator], SubmitRequestV2.Validators.PreUserIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["user_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[SubmitRequestV2.Validators.UserIdValidator], SubmitRequestV2.Validators.UserIdValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "language":
                    if pre:
                        cls._language_pre_validators.append(validator)
                    else:
                        cls._language_post_validators.append(validator)
                if field_name == "submission_files":
                    if pre:
                        cls._submission_files_pre_validators.append(validator)
                    else:
                        cls._submission_files_post_validators.append(validator)
                if field_name == "problem_id":
                    if pre:
                        cls._problem_id_pre_validators.append(validator)
                    else:
                        cls._problem_id_post_validators.append(validator)
                if field_name == "problem_version":
                    if pre:
                        cls._problem_version_pre_validators.append(validator)
                    else:
                        cls._problem_version_post_validators.append(validator)
                if field_name == "user_id":
                    if pre:
                        cls._user_id_pre_validators.append(validator)
                    else:
                        cls._user_id_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmitRequestV2.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: SubmitRequestV2.Partial) -> SubmissionId:
                ...

        class PreLanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmitRequestV2.Partial) -> typing.Any:
                ...

        class LanguageValidator(typing_extensions.Protocol):
            def __call__(self, __v: Language, __values: SubmitRequestV2.Partial) -> Language:
                ...

        class PreSubmissionFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmitRequestV2.Partial) -> typing.Any:
                ...

        class SubmissionFilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[SubmissionFileInfo], __values: SubmitRequestV2.Partial
            ) -> typing.List[SubmissionFileInfo]:
                ...

        class PreProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmitRequestV2.Partial) -> typing.Any:
                ...

        class ProblemIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemId, __values: SubmitRequestV2.Partial) -> ProblemId:
                ...

        class PreProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmitRequestV2.Partial) -> typing.Any:
                ...

        class ProblemVersionValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[int], __values: SubmitRequestV2.Partial) -> typing.Optional[int]:
                ...

        class PreUserIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: SubmitRequestV2.Partial) -> typing.Any:
                ...

        class UserIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: SubmitRequestV2.Partial) -> typing.Optional[str]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: SubmitRequestV2.Partial) -> SubmitRequestV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_submit_request_v_2(cls, values: SubmitRequestV2.Partial) -> SubmitRequestV2.Partial:
        for validator in SubmitRequestV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_submit_request_v_2(cls, values: SubmitRequestV2.Partial) -> SubmitRequestV2.Partial:
        for validator in SubmitRequestV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: SubmitRequestV2.Partial) -> SubmissionId:
        for validator in SubmitRequestV2.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: SubmitRequestV2.Partial) -> SubmissionId:
        for validator in SubmitRequestV2.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language", pre=True)
    def _pre_validate_language(cls, v: Language, values: SubmitRequestV2.Partial) -> Language:
        for validator in SubmitRequestV2.Validators._language_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("language", pre=False)
    def _post_validate_language(cls, v: Language, values: SubmitRequestV2.Partial) -> Language:
        for validator in SubmitRequestV2.Validators._language_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_files", pre=True)
    def _pre_validate_submission_files(
        cls, v: typing.List[SubmissionFileInfo], values: SubmitRequestV2.Partial
    ) -> typing.List[SubmissionFileInfo]:
        for validator in SubmitRequestV2.Validators._submission_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_files", pre=False)
    def _post_validate_submission_files(
        cls, v: typing.List[SubmissionFileInfo], values: SubmitRequestV2.Partial
    ) -> typing.List[SubmissionFileInfo]:
        for validator in SubmitRequestV2.Validators._submission_files_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=True)
    def _pre_validate_problem_id(cls, v: ProblemId, values: SubmitRequestV2.Partial) -> ProblemId:
        for validator in SubmitRequestV2.Validators._problem_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_id", pre=False)
    def _post_validate_problem_id(cls, v: ProblemId, values: SubmitRequestV2.Partial) -> ProblemId:
        for validator in SubmitRequestV2.Validators._problem_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=True)
    def _pre_validate_problem_version(
        cls, v: typing.Optional[int], values: SubmitRequestV2.Partial
    ) -> typing.Optional[int]:
        for validator in SubmitRequestV2.Validators._problem_version_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_version", pre=False)
    def _post_validate_problem_version(
        cls, v: typing.Optional[int], values: SubmitRequestV2.Partial
    ) -> typing.Optional[int]:
        for validator in SubmitRequestV2.Validators._problem_version_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("user_id", pre=True)
    def _pre_validate_user_id(cls, v: typing.Optional[str], values: SubmitRequestV2.Partial) -> typing.Optional[str]:
        for validator in SubmitRequestV2.Validators._user_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("user_id", pre=False)
    def _post_validate_user_id(cls, v: typing.Optional[str], values: SubmitRequestV2.Partial) -> typing.Optional[str]:
        for validator in SubmitRequestV2.Validators._user_id_post_validators:
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
