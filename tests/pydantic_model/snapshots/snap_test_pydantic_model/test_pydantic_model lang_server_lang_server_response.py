# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class LangServerResponse(pydantic.BaseModel):
    response: typing.Any

    class Partial(typing_extensions.TypedDict):
        response: typing_extensions.NotRequired[typing.Any]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @LangServerResponse.Validators.root()
            def validate(values: LangServerResponse.Partial) -> LangServerResponse.Partial:
                ...

            @LangServerResponse.Validators.field("response")
            def validate_response(response: typing.Any, values: LangServerResponse.Partial) -> typing.Any:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[LangServerResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[LangServerResponse.Validators._RootValidator]] = []
        _response_pre_validators: typing.ClassVar[typing.List[LangServerResponse.Validators.ResponseValidator]] = []
        _response_post_validators: typing.ClassVar[typing.List[LangServerResponse.Validators.ResponseValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [LangServerResponse.Validators._RootValidator], LangServerResponse.Validators._RootValidator
        ]:
            def decorator(
                validator: LangServerResponse.Validators._RootValidator,
            ) -> LangServerResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["response"], *, pre: bool = False
        ) -> typing.Callable[
            [LangServerResponse.Validators.ResponseValidator], LangServerResponse.Validators.ResponseValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "response":
                    if pre:
                        cls._response_pre_validators.append(validator)
                    else:
                        cls._response_post_validators.append(validator)
                return validator

            return decorator

        class ResponseValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: LangServerResponse.Partial) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: LangServerResponse.Partial) -> LangServerResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: LangServerResponse.Partial) -> LangServerResponse.Partial:
        for validator in LangServerResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: LangServerResponse.Partial) -> LangServerResponse.Partial:
        for validator in LangServerResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("response", pre=True)
    def _pre_validate_response(cls, v: typing.Any, values: LangServerResponse.Partial) -> typing.Any:
        for validator in LangServerResponse.Validators._response_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("response", pre=False)
    def _post_validate_response(cls, v: typing.Any, values: LangServerResponse.Partial) -> typing.Any:
        for validator in LangServerResponse.Validators._response_post_validators:
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
