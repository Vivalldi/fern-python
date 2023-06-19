# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .error_info import ErrorInfo
from .submission_id import SubmissionId


class ErroredResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    error_info: ErrorInfo = pydantic.Field(alias="errorInfo")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        error_info: typing_extensions.NotRequired[ErrorInfo]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ErroredResponse.Validators.root()
            def validate(values: ErroredResponse.Partial) -> ErroredResponse.Partial:
                ...

            @ErroredResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: ErroredResponse.Partial) -> SubmissionId:
                ...

            @ErroredResponse.Validators.field("error_info")
            def validate_error_info(error_info: ErrorInfo, values: ErroredResponse.Partial) -> ErrorInfo:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ErroredResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ErroredResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[ErroredResponse.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[ErroredResponse.Validators.SubmissionIdValidator]
        ] = []
        _error_info_pre_validators: typing.ClassVar[typing.List[ErroredResponse.Validators.PreErrorInfoValidator]] = []
        _error_info_post_validators: typing.ClassVar[typing.List[ErroredResponse.Validators.ErrorInfoValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ErroredResponse.Validators._RootValidator], ErroredResponse.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ErroredResponse.Validators._PreRootValidator], ErroredResponse.Validators._PreRootValidator
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
            [ErroredResponse.Validators.PreSubmissionIdValidator], ErroredResponse.Validators.PreSubmissionIdValidator
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
            [ErroredResponse.Validators.SubmissionIdValidator], ErroredResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["error_info"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ErroredResponse.Validators.PreErrorInfoValidator], ErroredResponse.Validators.PreErrorInfoValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["error_info"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ErroredResponse.Validators.ErrorInfoValidator], ErroredResponse.Validators.ErrorInfoValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "error_info":
                    if pre:
                        cls._error_info_pre_validators.append(validator)
                    else:
                        cls._error_info_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ErroredResponse.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: ErroredResponse.Partial) -> SubmissionId:
                ...

        class PreErrorInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ErroredResponse.Partial) -> typing.Any:
                ...

        class ErrorInfoValidator(typing_extensions.Protocol):
            def __call__(self, __v: ErrorInfo, __values: ErroredResponse.Partial) -> ErrorInfo:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ErroredResponse.Partial) -> ErroredResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _preerrored_response_validate(cls, values: ErroredResponse.Partial) -> ErroredResponse.Partial:
        for validator in ErroredResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _posterrored_response_validate(cls, values: ErroredResponse.Partial) -> ErroredResponse.Partial:
        for validator in ErroredResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: ErroredResponse.Partial) -> SubmissionId:
        for validator in ErroredResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: ErroredResponse.Partial) -> SubmissionId:
        for validator in ErroredResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("error_info", pre=True)
    def _pre_validate_error_info(cls, v: ErrorInfo, values: ErroredResponse.Partial) -> ErrorInfo:
        for validator in ErroredResponse.Validators._error_info_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("error_info", pre=False)
    def _post_validate_error_info(cls, v: ErrorInfo, values: ErroredResponse.Partial) -> ErrorInfo:
        for validator in ErroredResponse.Validators._error_info_post_validators:
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
