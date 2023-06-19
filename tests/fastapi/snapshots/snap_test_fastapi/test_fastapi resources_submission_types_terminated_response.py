# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime


class TerminatedResponse(pydantic.BaseModel):
    class Partial(typing_extensions.TypedDict):
        pass

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TerminatedResponse.Validators.root()
            def validate(values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TerminatedResponse.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TerminatedResponse.Validators._RootValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TerminatedResponse.Validators._RootValidator], TerminatedResponse.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TerminatedResponse.Validators._PreRootValidator], TerminatedResponse.Validators._PreRootValidator
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

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _preterminated_response_validate(cls, values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
        for validator in TerminatedResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postterminated_response_validate(cls, values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
        for validator in TerminatedResponse.Validators._post_validators:
            values = validator(values)
        return values

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
