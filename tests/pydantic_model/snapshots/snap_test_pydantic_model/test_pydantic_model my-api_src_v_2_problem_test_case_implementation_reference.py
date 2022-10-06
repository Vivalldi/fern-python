from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_implementation import TestCaseImplementation
from .test_case_template_id import TestCaseTemplateId

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def template_id(self, value: TestCaseTemplateId) -> TestCaseImplementationReference:
        return TestCaseImplementationReference(
            __root__=_TestCaseImplementationReference.TemplateId(type="templateId", value=value)
        )

    def implementation(self, value: TestCaseImplementation) -> TestCaseImplementationReference:
        return TestCaseImplementationReference(
            __root__=_TestCaseImplementationReference.Implementation(**dict(value), type="implementation")
        )


class TestCaseImplementationReference(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation]:
        return self.__root__

    def visit(
        self,
        template_id: typing.Callable[[TestCaseTemplateId], T_Result],
        implementation: typing.Callable[[TestCaseImplementation], T_Result],
    ) -> T_Result:
        if self.__root__.type == "templateId":
            return template_id(self.__root__.template_id)
        if self.__root__.type == "implementation":
            return implementation(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation],
        pydantic.Field(discriminator="type"),
    ]

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation],
            values.get("__root__"),
        )
        for validator in TestCaseImplementationReference.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    class Validators:
        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [
                        typing.Union[
                            _TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation
                        ]
                    ],
                    typing.Union[
                        _TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation
                    ],
                ]
            ]
        ] = []

        @classmethod
        def add_validator(
            cls,
            validator: typing.Callable[
                [
                    typing.Union[
                        _TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation
                    ]
                ],
                typing.Union[
                    _TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation
                ],
            ],
        ) -> None:
            cls._validators.append(validator)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        frozen = True


class _TestCaseImplementationReference:
    class TemplateId(pydantic.BaseModel):
        type: typing_extensions.Literal["templateId"]
        value: TestCaseTemplateId

        class Config:
            frozen = True

    class Implementation(TestCaseImplementation):
        type: typing_extensions.Literal["implementation"]

        class Config:
            frozen = True


TestCaseImplementationReference.update_forward_refs()
