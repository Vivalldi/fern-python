# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class LangServerRequest(pydantic.BaseModel):
    request: typing.Any

    class Partial(typing_extensions.TypedDict):
        request: typing_extensions.NotRequired[typing.Any]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LangServerRequest.Validators.root()
            def validate(values: LangServerRequest.Partial) -> LangServerRequest.Partial:
                ...

            @LangServerRequest.Validators.field("request")
            def validate_request(request: typing.Any, values: LangServerRequest.Partial) -> typing.Any:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[LangServerRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[LangServerRequest.Validators._RootValidator]] = []
        _request_pre_validators: typing.ClassVar[typing.List[LangServerRequest.Validators.PreRequestValidator]] = []
        _request_post_validators: typing.ClassVar[typing.List[LangServerRequest.Validators.RequestValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [LangServerRequest.Validators._RootValidator], LangServerRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [LangServerRequest.Validators._PreRootValidator], LangServerRequest.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["request"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [LangServerRequest.Validators.PreRequestValidator], LangServerRequest.Validators.PreRequestValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["request"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [LangServerRequest.Validators.RequestValidator], LangServerRequest.Validators.RequestValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "request":
                    if pre:
                        cls._request_pre_validators.append(validator)
                    else:
                        cls._request_post_validators.append(validator)
                return validator

            return decorator

        class PreRequestValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: LangServerRequest.Partial) -> typing.Any:
                ...

        class RequestValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: LangServerRequest.Partial) -> typing.Any:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: LangServerRequest.Partial) -> LangServerRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _prelang_server_request_validate(cls, values: LangServerRequest.Partial) -> LangServerRequest.Partial:
        for validator in LangServerRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postlang_server_request_validate(cls, values: LangServerRequest.Partial) -> LangServerRequest.Partial:
        for validator in LangServerRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("request", pre=True)
    def _pre_validate_request(cls, v: typing.Any, values: LangServerRequest.Partial) -> typing.Any:
        for validator in LangServerRequest.Validators._request_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("request", pre=False)
    def _post_validate_request(cls, v: typing.Any, values: LangServerRequest.Partial) -> typing.Any:
        for validator in LangServerRequest.Validators._request_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        json_encoders = {dt.datetime: serialize_datetime}
