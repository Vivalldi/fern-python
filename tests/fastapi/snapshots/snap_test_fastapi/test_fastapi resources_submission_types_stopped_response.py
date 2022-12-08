# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class StoppedResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StoppedResponse.Validators.root()
            def validate(values: StoppedResponse.Partial) -> StoppedResponse.Partial:
                ...

            @StoppedResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: StoppedResponse.Partial) -> SubmissionId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StoppedResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StoppedResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[StoppedResponse.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[StoppedResponse.Validators.SubmissionIdValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[StoppedResponse.Validators._RootValidator], StoppedResponse.Validators._RootValidator]:
            def decorator(
                validator: StoppedResponse.Validators._RootValidator,
            ) -> StoppedResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [StoppedResponse.Validators.SubmissionIdValidator], StoppedResponse.Validators.SubmissionIdValidator
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
            def __call__(self, __v: SubmissionId, __values: StoppedResponse.Partial) -> SubmissionId:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StoppedResponse.Partial) -> StoppedResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StoppedResponse.Partial) -> StoppedResponse.Partial:
        for validator in StoppedResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StoppedResponse.Partial) -> StoppedResponse.Partial:
        for validator in StoppedResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: StoppedResponse.Partial) -> SubmissionId:
        for validator in StoppedResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: StoppedResponse.Partial) -> SubmissionId:
        for validator in StoppedResponse.Validators._submission_id_post_validators:
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
        extra = pydantic.Extra.forbid
