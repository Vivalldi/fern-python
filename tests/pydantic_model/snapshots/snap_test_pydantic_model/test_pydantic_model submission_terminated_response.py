# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


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

        _pre_validators: typing.ClassVar[typing.List[TerminatedResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TerminatedResponse.Validators._RootValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[
            [TerminatedResponse.Validators._RootValidator], TerminatedResponse.Validators._RootValidator
        ]:
            def decorator(
                validator: TerminatedResponse.Validators._RootValidator,
            ) -> TerminatedResponse.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
        for validator in TerminatedResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TerminatedResponse.Partial) -> TerminatedResponse.Partial:
        for validator in TerminatedResponse.Validators._post_validators:
            values = validator(values)
        return values

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
