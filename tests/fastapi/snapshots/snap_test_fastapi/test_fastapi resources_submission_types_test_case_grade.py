# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...commons.types.key_value_pair import KeyValuePair
from ...commons.types.map_value import MapValue
from ...commons.types.variable_value import VariableValue
from .test_case_hidden_grade import TestCaseHiddenGrade
from .test_case_non_hidden_grade import TestCaseNonHiddenGrade

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def hidden(self, value: TestCaseHiddenGrade) -> TestCaseGrade:
        return TestCaseGrade(__root__=_TestCaseGrade.Hidden(**value.dict(exclude_unset=True), type="hidden"))

    def non_hidden(self, value: TestCaseNonHiddenGrade) -> TestCaseGrade:
        return TestCaseGrade(__root__=_TestCaseGrade.NonHidden(**value.dict(exclude_unset=True), type="nonHidden"))


class TestCaseGrade(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden]:
        return self.__root__

    def visit(
        self,
        hidden: typing.Callable[[TestCaseHiddenGrade], T_Result],
        non_hidden: typing.Callable[[TestCaseNonHiddenGrade], T_Result],
    ) -> T_Result:
        if self.__root__.type == "hidden":
            return hidden(TestCaseHiddenGrade(**self.__root__.dict(exclude_unset=True)))
        if self.__root__.type == "nonHidden":
            return non_hidden(TestCaseNonHiddenGrade(**self.__root__.dict(exclude_unset=True)))

    __root__: typing_extensions.Annotated[
        typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden], pydantic.Field(discriminator="type")
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseGrade.Validators.validate
            def validate(value: typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden]) -> typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden]],
                    typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden]],
                typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(typing.Union[_TestCaseGrade.Hidden, _TestCaseGrade.NonHidden], values.get("__root__"))
        for validator in TestCaseGrade.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _TestCaseGrade:
    class Hidden(TestCaseHiddenGrade):
        type: typing_extensions.Literal["hidden"]

        class Config:
            allow_population_by_field_name = True

    class NonHidden(TestCaseNonHiddenGrade):
        type: typing_extensions.Literal["nonHidden"]

        class Config:
            allow_population_by_field_name = True


_TestCaseGrade.NonHidden.update_forward_refs(KeyValuePair=KeyValuePair, MapValue=MapValue, VariableValue=VariableValue)
TestCaseGrade.update_forward_refs()
