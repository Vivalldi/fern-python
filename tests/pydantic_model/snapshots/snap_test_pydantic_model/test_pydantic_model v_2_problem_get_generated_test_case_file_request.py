# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_template import TestCaseTemplate
from .test_case_v_2 import TestCaseV2


class GetGeneratedTestCaseFileRequest(pydantic.BaseModel):
    template: typing.Optional[TestCaseTemplate]
    test_case: TestCaseV2 = pydantic.Field(alias="testCase")

    class Partial(typing_extensions.TypedDict):
        template: typing_extensions.NotRequired[typing.Optional[TestCaseTemplate]]
        test_case: typing_extensions.NotRequired[TestCaseV2]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetGeneratedTestCaseFileRequest.Validators.root
            def validate(values: GetGeneratedTestCaseFileRequest.Partial) -> GetGeneratedTestCaseFileRequest.Partial:
                ...

            @GetGeneratedTestCaseFileRequest.Validators.field("template")
            def validate_template(template: typing.Optional[TestCaseTemplate], values: GetGeneratedTestCaseFileRequest.Partial) -> typing.Optional[TestCaseTemplate]:
                ...

            @GetGeneratedTestCaseFileRequest.Validators.field("test_case")
            def validate_test_case(test_case: TestCaseV2, values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[GetGeneratedTestCaseFileRequest.Partial], GetGeneratedTestCaseFileRequest.Partial]
            ]
        ] = []
        _template_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseFileRequest.Validators.TemplateValidator]
        ] = []
        _test_case_validators: typing.ClassVar[
            typing.List[GetGeneratedTestCaseFileRequest.Validators.TestCaseValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [GetGeneratedTestCaseFileRequest.Partial], GetGeneratedTestCaseFileRequest.Partial
            ],
        ) -> typing.Callable[[GetGeneratedTestCaseFileRequest.Partial], GetGeneratedTestCaseFileRequest.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["template"]
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators.TemplateValidator],
            GetGeneratedTestCaseFileRequest.Validators.TemplateValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["test_case"]
        ) -> typing.Callable[
            [GetGeneratedTestCaseFileRequest.Validators.TestCaseValidator],
            GetGeneratedTestCaseFileRequest.Validators.TestCaseValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "template":
                    cls._template_validators.append(validator)
                if field_name == "test_case":
                    cls._test_case_validators.append(validator)
                return validator

            return decorator

        class TemplateValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[TestCaseTemplate], __values: GetGeneratedTestCaseFileRequest.Partial
            ) -> typing.Optional[TestCaseTemplate]:
                ...

        class TestCaseValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseV2, __values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GetGeneratedTestCaseFileRequest.Partial) -> GetGeneratedTestCaseFileRequest.Partial:
        for validator in GetGeneratedTestCaseFileRequest.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("template")
    def _validate_template(
        cls, v: typing.Optional[TestCaseTemplate], values: GetGeneratedTestCaseFileRequest.Partial
    ) -> typing.Optional[TestCaseTemplate]:
        for validator in GetGeneratedTestCaseFileRequest.Validators._template_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("test_case")
    def _validate_test_case(cls, v: TestCaseV2, values: GetGeneratedTestCaseFileRequest.Partial) -> TestCaseV2:
        for validator in GetGeneratedTestCaseFileRequest.Validators._test_case_validators:
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
