# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.language import Language
from ....problem.problem_description import ProblemDescription
from .custom_files import CustomFiles
from .test_case_template import TestCaseTemplate
from .test_case_v_2 import TestCaseV2


class CreateProblemRequestV2(pydantic.BaseModel):
    problem_name: str = pydantic.Field(alias="problemName")
    problem_description: ProblemDescription = pydantic.Field(alias="problemDescription")
    custom_files: CustomFiles = pydantic.Field(alias="customFiles")
    custom_test_case_templates: typing.List[TestCaseTemplate] = pydantic.Field(alias="customTestCaseTemplates")
    testcases: typing.List[TestCaseV2]
    supported_languages: typing.List[Language] = pydantic.Field(alias="supportedLanguages")
    is_public: bool = pydantic.Field(alias="isPublic")

    class Partial(typing_extensions.TypedDict):
        problem_name: typing_extensions.NotRequired[str]
        problem_description: typing_extensions.NotRequired[ProblemDescription]
        custom_files: typing_extensions.NotRequired[CustomFiles]
        custom_test_case_templates: typing_extensions.NotRequired[typing.List[TestCaseTemplate]]
        testcases: typing_extensions.NotRequired[typing.List[TestCaseV2]]
        supported_languages: typing_extensions.NotRequired[typing.List[Language]]
        is_public: typing_extensions.NotRequired[bool]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CreateProblemRequestV2.Validators.root
            def validate(values: CreateProblemRequestV2.Partial) -> CreateProblemRequestV2.Partial:
                ...

            @CreateProblemRequestV2.Validators.field("problem_name")
            def validate_problem_name(problem_name: str, values: CreateProblemRequestV2.Partial) -> str:
                ...

            @CreateProblemRequestV2.Validators.field("problem_description")
            def validate_problem_description(problem_description: ProblemDescription, values: CreateProblemRequestV2.Partial) -> ProblemDescription:
                ...

            @CreateProblemRequestV2.Validators.field("custom_files")
            def validate_custom_files(custom_files: CustomFiles, values: CreateProblemRequestV2.Partial) -> CustomFiles:
                ...

            @CreateProblemRequestV2.Validators.field("custom_test_case_templates")
            def validate_custom_test_case_templates(custom_test_case_templates: typing.List[TestCaseTemplate], values: CreateProblemRequestV2.Partial) -> typing.List[TestCaseTemplate]:
                ...

            @CreateProblemRequestV2.Validators.field("testcases")
            def validate_testcases(testcases: typing.List[TestCaseV2], values: CreateProblemRequestV2.Partial) -> typing.List[TestCaseV2]:
                ...

            @CreateProblemRequestV2.Validators.field("supported_languages")
            def validate_supported_languages(supported_languages: typing.List[Language], values: CreateProblemRequestV2.Partial) -> typing.List[Language]:
                ...

            @CreateProblemRequestV2.Validators.field("is_public")
            def validate_is_public(is_public: bool, values: CreateProblemRequestV2.Partial) -> bool:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[typing.Callable[[CreateProblemRequestV2.Partial], CreateProblemRequestV2.Partial]]
        ] = []
        _problem_name_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.ProblemNameValidator]
        ] = []
        _problem_description_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.ProblemDescriptionValidator]
        ] = []
        _custom_files_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.CustomFilesValidator]
        ] = []
        _custom_test_case_templates_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.CustomTestCaseTemplatesValidator]
        ] = []
        _testcases_validators: typing.ClassVar[typing.List[CreateProblemRequestV2.Validators.TestcasesValidator]] = []
        _supported_languages_validators: typing.ClassVar[
            typing.List[CreateProblemRequestV2.Validators.SupportedLanguagesValidator]
        ] = []
        _is_public_validators: typing.ClassVar[typing.List[CreateProblemRequestV2.Validators.IsPublicValidator]] = []

        @classmethod
        def root(
            cls, validator: typing.Callable[[CreateProblemRequestV2.Partial], CreateProblemRequestV2.Partial]
        ) -> typing.Callable[[CreateProblemRequestV2.Partial], CreateProblemRequestV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_name"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.ProblemNameValidator],
            CreateProblemRequestV2.Validators.ProblemNameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problem_description"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.ProblemDescriptionValidator],
            CreateProblemRequestV2.Validators.ProblemDescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_files"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.CustomFilesValidator],
            CreateProblemRequestV2.Validators.CustomFilesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["custom_test_case_templates"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.CustomTestCaseTemplatesValidator],
            CreateProblemRequestV2.Validators.CustomTestCaseTemplatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["testcases"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.TestcasesValidator], CreateProblemRequestV2.Validators.TestcasesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["supported_languages"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.SupportedLanguagesValidator],
            CreateProblemRequestV2.Validators.SupportedLanguagesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_public"]
        ) -> typing.Callable[
            [CreateProblemRequestV2.Validators.IsPublicValidator], CreateProblemRequestV2.Validators.IsPublicValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "problem_name":
                    cls._problem_name_validators.append(validator)
                if field_name == "problem_description":
                    cls._problem_description_validators.append(validator)
                if field_name == "custom_files":
                    cls._custom_files_validators.append(validator)
                if field_name == "custom_test_case_templates":
                    cls._custom_test_case_templates_validators.append(validator)
                if field_name == "testcases":
                    cls._testcases_validators.append(validator)
                if field_name == "supported_languages":
                    cls._supported_languages_validators.append(validator)
                if field_name == "is_public":
                    cls._is_public_validators.append(validator)
                return validator

            return decorator

        class ProblemNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: CreateProblemRequestV2.Partial) -> str:
                ...

        class ProblemDescriptionValidator(typing_extensions.Protocol):
            def __call__(self, __v: ProblemDescription, __values: CreateProblemRequestV2.Partial) -> ProblemDescription:
                ...

        class CustomFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: CustomFiles, __values: CreateProblemRequestV2.Partial) -> CustomFiles:
                ...

        class CustomTestCaseTemplatesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseTemplate], __values: CreateProblemRequestV2.Partial
            ) -> typing.List[TestCaseTemplate]:
                ...

        class TestcasesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TestCaseV2], __values: CreateProblemRequestV2.Partial
            ) -> typing.List[TestCaseV2]:
                ...

        class SupportedLanguagesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[Language], __values: CreateProblemRequestV2.Partial
            ) -> typing.List[Language]:
                ...

        class IsPublicValidator(typing_extensions.Protocol):
            def __call__(self, __v: bool, __values: CreateProblemRequestV2.Partial) -> bool:
                ...

    @pydantic.root_validator
    def _validate(cls, values: CreateProblemRequestV2.Partial) -> CreateProblemRequestV2.Partial:
        for validator in CreateProblemRequestV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("problem_name")
    def _validate_problem_name(cls, v: str, values: CreateProblemRequestV2.Partial) -> str:
        for validator in CreateProblemRequestV2.Validators._problem_name_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problem_description")
    def _validate_problem_description(
        cls, v: ProblemDescription, values: CreateProblemRequestV2.Partial
    ) -> ProblemDescription:
        for validator in CreateProblemRequestV2.Validators._problem_description_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_files")
    def _validate_custom_files(cls, v: CustomFiles, values: CreateProblemRequestV2.Partial) -> CustomFiles:
        for validator in CreateProblemRequestV2.Validators._custom_files_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("custom_test_case_templates")
    def _validate_custom_test_case_templates(
        cls, v: typing.List[TestCaseTemplate], values: CreateProblemRequestV2.Partial
    ) -> typing.List[TestCaseTemplate]:
        for validator in CreateProblemRequestV2.Validators._custom_test_case_templates_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("testcases")
    def _validate_testcases(
        cls, v: typing.List[TestCaseV2], values: CreateProblemRequestV2.Partial
    ) -> typing.List[TestCaseV2]:
        for validator in CreateProblemRequestV2.Validators._testcases_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("supported_languages")
    def _validate_supported_languages(
        cls, v: typing.List[Language], values: CreateProblemRequestV2.Partial
    ) -> typing.List[Language]:
        for validator in CreateProblemRequestV2.Validators._supported_languages_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_public")
    def _validate_is_public(cls, v: bool, values: CreateProblemRequestV2.Partial) -> bool:
        for validator in CreateProblemRequestV2.Validators._is_public_validators:
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
