# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.language import Language
from .problem_files import ProblemFiles


class GetDefaultStarterFilesResponse(pydantic.BaseModel):
    files: typing.Dict[Language, ProblemFiles]

    class Partial(typing_extensions.TypedDict):
        files: typing_extensions.NotRequired[typing.Dict[Language, ProblemFiles]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetDefaultStarterFilesResponse.Validators.root
            def validate(values: GetDefaultStarterFilesResponse.Partial) -> GetDefaultStarterFilesResponse.Partial:
                ...

            @GetDefaultStarterFilesResponse.Validators.field("files")
            def validate_files(files: typing.Dict[Language, ProblemFiles], values: GetDefaultStarterFilesResponse.Partial) -> typing.Dict[Language, ProblemFiles]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[GetDefaultStarterFilesResponse.Partial], GetDefaultStarterFilesResponse.Partial]
            ]
        ] = []
        _files_validators: typing.ClassVar[typing.List[GetDefaultStarterFilesResponse.Validators.FilesValidator]] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [GetDefaultStarterFilesResponse.Partial], GetDefaultStarterFilesResponse.Partial
            ],
        ) -> typing.Callable[[GetDefaultStarterFilesResponse.Partial], GetDefaultStarterFilesResponse.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"]
        ) -> typing.Callable[
            [GetDefaultStarterFilesResponse.Validators.FilesValidator],
            GetDefaultStarterFilesResponse.Validators.FilesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "files":
                    cls._files_validators.append(validator)
                return validator

            return decorator

        class FilesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, ProblemFiles], __values: GetDefaultStarterFilesResponse.Partial
            ) -> typing.Dict[Language, ProblemFiles]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: GetDefaultStarterFilesResponse.Partial) -> GetDefaultStarterFilesResponse.Partial:
        for validator in GetDefaultStarterFilesResponse.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("files")
    def _validate_files(
        cls, v: typing.Dict[Language, ProblemFiles], values: GetDefaultStarterFilesResponse.Partial
    ) -> typing.Dict[Language, ProblemFiles]:
        for validator in GetDefaultStarterFilesResponse.Validators._files_validators:
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
        extra = pydantic.Extra.forbid
