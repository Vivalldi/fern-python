# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId
from .workspace_run_details import WorkspaceRunDetails


class WorkspaceRanResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    run_details: WorkspaceRunDetails = pydantic.Field(alias="runDetails")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        run_details: typing_extensions.NotRequired[WorkspaceRunDetails]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceRanResponse.Validators.root()
            def validate(values: WorkspaceRanResponse.Partial) -> WorkspaceRanResponse.Partial:
                ...

            @WorkspaceRanResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: WorkspaceRanResponse.Partial) -> SubmissionId:
                ...

            @WorkspaceRanResponse.Validators.field("run_details")
            def validate_run_details(run_details: WorkspaceRunDetails, values: WorkspaceRanResponse.Partial) -> WorkspaceRunDetails:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceRanResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceRanResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[WorkspaceRanResponse.Validators.SubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[WorkspaceRanResponse.Validators.SubmissionIdValidator]
        ] = []
        _run_details_pre_validators: typing.ClassVar[
            typing.List[WorkspaceRanResponse.Validators.RunDetailsValidator]
        ] = []
        _run_details_post_validators: typing.ClassVar[
            typing.List[WorkspaceRanResponse.Validators.RunDetailsValidator]
        ] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRanResponse.Validators._RootValidator], WorkspaceRanResponse.Validators._RootValidator
        ]:
            def decorator(
                validator: WorkspaceRanResponse.Validators._RootValidator,
            ) -> WorkspaceRanResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRanResponse.Validators.SubmissionIdValidator],
            WorkspaceRanResponse.Validators.SubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["run_details"], *, pre: bool = False
        ) -> typing.Callable[
            [WorkspaceRanResponse.Validators.RunDetailsValidator], WorkspaceRanResponse.Validators.RunDetailsValidator
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
                if field_name == "run_details":
                    if pre:
                        cls._run_details_pre_validators.append(validator)
                    else:
                        cls._run_details_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: WorkspaceRanResponse.Partial) -> SubmissionId:
                ...

        class RunDetailsValidator(typing_extensions.Protocol):
            def __call__(self, __v: WorkspaceRunDetails, __values: WorkspaceRanResponse.Partial) -> WorkspaceRunDetails:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: WorkspaceRanResponse.Partial) -> WorkspaceRanResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceRanResponse.Partial) -> WorkspaceRanResponse.Partial:
        for validator in WorkspaceRanResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceRanResponse.Partial) -> WorkspaceRanResponse.Partial:
        for validator in WorkspaceRanResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: WorkspaceRanResponse.Partial) -> SubmissionId:
        for validator in WorkspaceRanResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: WorkspaceRanResponse.Partial) -> SubmissionId:
        for validator in WorkspaceRanResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("run_details", pre=True)
    def _pre_validate_run_details(
        cls, v: WorkspaceRunDetails, values: WorkspaceRanResponse.Partial
    ) -> WorkspaceRunDetails:
        for validator in WorkspaceRanResponse.Validators._run_details_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("run_details", pre=False)
    def _post_validate_run_details(
        cls, v: WorkspaceRunDetails, values: WorkspaceRanResponse.Partial
    ) -> WorkspaceRunDetails:
        for validator in WorkspaceRanResponse.Validators._run_details_post_validators:
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
