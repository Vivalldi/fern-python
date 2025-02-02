# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .stack_frame import StackFrame


class StackInformation(pydantic.BaseModel):
    num_stack_frames: int = pydantic.Field(alias="numStackFrames")
    top_stack_frame: typing.Optional[StackFrame] = pydantic.Field(alias="topStackFrame", default=None)

    class Partial(typing_extensions.TypedDict):
        num_stack_frames: typing_extensions.NotRequired[int]
        top_stack_frame: typing_extensions.NotRequired[typing.Optional[StackFrame]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StackInformation.Validators.root()
            def validate(values: StackInformation.Partial) -> StackInformation.Partial:
                ...

            @StackInformation.Validators.field("num_stack_frames")
            def validate_num_stack_frames(num_stack_frames: int, values: StackInformation.Partial) -> int:
                ...

            @StackInformation.Validators.field("top_stack_frame")
            def validate_top_stack_frame(top_stack_frame: typing.Optional[StackFrame], values: StackInformation.Partial) -> typing.Optional[StackFrame]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StackInformation.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StackInformation.Validators._RootValidator]] = []
        _num_stack_frames_pre_validators: typing.ClassVar[
            typing.List[StackInformation.Validators.PreNumStackFramesValidator]
        ] = []
        _num_stack_frames_post_validators: typing.ClassVar[
            typing.List[StackInformation.Validators.NumStackFramesValidator]
        ] = []
        _top_stack_frame_pre_validators: typing.ClassVar[
            typing.List[StackInformation.Validators.PreTopStackFrameValidator]
        ] = []
        _top_stack_frame_post_validators: typing.ClassVar[
            typing.List[StackInformation.Validators.TopStackFrameValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StackInformation.Validators._RootValidator], StackInformation.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StackInformation.Validators._PreRootValidator], StackInformation.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["num_stack_frames"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StackInformation.Validators.PreNumStackFramesValidator],
            StackInformation.Validators.PreNumStackFramesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["num_stack_frames"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [StackInformation.Validators.NumStackFramesValidator], StackInformation.Validators.NumStackFramesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["top_stack_frame"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StackInformation.Validators.PreTopStackFrameValidator],
            StackInformation.Validators.PreTopStackFrameValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["top_stack_frame"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [StackInformation.Validators.TopStackFrameValidator], StackInformation.Validators.TopStackFrameValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "num_stack_frames":
                    if pre:
                        cls._num_stack_frames_pre_validators.append(validator)
                    else:
                        cls._num_stack_frames_post_validators.append(validator)
                if field_name == "top_stack_frame":
                    if pre:
                        cls._top_stack_frame_pre_validators.append(validator)
                    else:
                        cls._top_stack_frame_post_validators.append(validator)
                return validator

            return decorator

        class PreNumStackFramesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StackInformation.Partial) -> typing.Any:
                ...

        class NumStackFramesValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: StackInformation.Partial) -> int:
                ...

        class PreTopStackFrameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StackInformation.Partial) -> typing.Any:
                ...

        class TopStackFrameValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[StackFrame], __values: StackInformation.Partial
            ) -> typing.Optional[StackFrame]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StackInformation.Partial) -> StackInformation.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate_stack_information(cls, values: StackInformation.Partial) -> StackInformation.Partial:
        for validator in StackInformation.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate_stack_information(cls, values: StackInformation.Partial) -> StackInformation.Partial:
        for validator in StackInformation.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("num_stack_frames", pre=True)
    def _pre_validate_num_stack_frames(cls, v: int, values: StackInformation.Partial) -> int:
        for validator in StackInformation.Validators._num_stack_frames_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("num_stack_frames", pre=False)
    def _post_validate_num_stack_frames(cls, v: int, values: StackInformation.Partial) -> int:
        for validator in StackInformation.Validators._num_stack_frames_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("top_stack_frame", pre=True)
    def _pre_validate_top_stack_frame(
        cls, v: typing.Optional[StackFrame], values: StackInformation.Partial
    ) -> typing.Optional[StackFrame]:
        for validator in StackInformation.Validators._top_stack_frame_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("top_stack_frame", pre=False)
    def _post_validate_top_stack_frame(
        cls, v: typing.Optional[StackFrame], values: StackInformation.Partial
    ) -> typing.Optional[StackFrame]:
        for validator in StackInformation.Validators._top_stack_frame_post_validators:
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
