# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class GetTraceResponsesPageRequest(pydantic.BaseModel):
    offset: typing.Optional[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetTraceResponsesPageRequest.Validators.field("offset")
            def validate_offset(v: typing.Optional[int], values: GetTraceResponsesPageRequest.Partial) -> typing.Optional[int]:
                ...
        """

        _offset_validators: typing.ClassVar[typing.List[GetTraceResponsesPageRequest.Validators.OffsetValidator]] = []

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"]
        ) -> typing.Callable[
            [GetTraceResponsesPageRequest.Validators.OffsetValidator],
            GetTraceResponsesPageRequest.Validators.OffsetValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "offset":
                    cls._offset_validators.append(validator)
                return validator

            return decorator

        class OffsetValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Optional[int], *, values: GetTraceResponsesPageRequest.Partial
            ) -> typing.Optional[int]:
                ...

    @pydantic.validator("offset")
    def _validate_offset(
        cls, v: typing.Optional[int], values: GetTraceResponsesPageRequest.Partial
    ) -> typing.Optional[int]:
        for validator in GetTraceResponsesPageRequest.Validators._offset_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing_extensions.TypedDict):
        offset: typing_extensions.NotRequired[typing.Optional[int]]

    class Config:
        frozen = True
