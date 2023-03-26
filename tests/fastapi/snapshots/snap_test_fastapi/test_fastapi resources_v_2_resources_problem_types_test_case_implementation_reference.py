# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .....commons.types.list_type import ListType
from .....commons.types.map_type import MapType
from .....commons.types.variable_type import VariableType
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
            return template_id(self.__root__.value)
        if self.__root__.type == "implementation":
            return implementation(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation],
        pydantic.Field(discriminator="type"),
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseImplementationReference.Validators.validate
            def validate(value: typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation]) -> typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation]:
                ...
        """

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
        def validate(
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

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(
            typing.Union[_TestCaseImplementationReference.TemplateId, _TestCaseImplementationReference.Implementation],
            values.get("__root__"),
        )
        for validator in TestCaseImplementationReference.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _TestCaseImplementationReference:
    class TemplateId(pydantic.BaseModel):
        type: typing_extensions.Literal["templateId"] = "templateId"
        value: TestCaseTemplateId

        class Config:
            frozen = True

    class Implementation(TestCaseImplementation):
        type: typing_extensions.Literal["implementation"] = "implementation"

        class Config:
            frozen = True


_TestCaseImplementationReference.Implementation.update_forward_refs(
    ListType=ListType, MapType=MapType, VariableType=VariableType
)
TestCaseImplementationReference.update_forward_refs()
