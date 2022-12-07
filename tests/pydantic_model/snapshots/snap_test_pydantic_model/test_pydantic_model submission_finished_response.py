# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class FinishedResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FinishedResponse.Validators.root
            def validate(values: FinishedResponse.Partial) -> FinishedResponse.Partial:
                ...

            @FinishedResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: FinishedResponse.Partial) -> SubmissionId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[FinishedResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[FinishedResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[FinishedResponse.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[FinishedResponse.Validators.SubmissionIdValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> FinishedResponse.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool
        ) -> typing.Callable[
            [FinishedResponse.Validators.SubmissionIdValidator], FinishedResponse.Validators.SubmissionIdValidator
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
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: FinishedResponse.Partial) -> SubmissionId:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: FinishedResponse.Partial) -> FinishedResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: FinishedResponse.Partial) -> FinishedResponse.Partial:
        for validator in FinishedResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: FinishedResponse.Partial) -> FinishedResponse.Partial:
        for validator in FinishedResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: FinishedResponse.Partial) -> SubmissionId:
        for validator in FinishedResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: FinishedResponse.Partial) -> SubmissionId:
        for validator in FinishedResponse.Validators._submission_id_post_validators:
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
