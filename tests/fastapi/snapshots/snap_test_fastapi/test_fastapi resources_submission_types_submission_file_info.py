# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class SubmissionFileInfo(pydantic.BaseModel):
    directory: str
    filename: str
    contents: str

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionFileInfo.Validators.field("directory")
            def validate_directory(v: str, values: SubmissionFileInfo.Partial) -> str:
                ...

            @SubmissionFileInfo.Validators.field("filename")
            def validate_filename(v: str, values: SubmissionFileInfo.Partial) -> str:
                ...

            @SubmissionFileInfo.Validators.field("contents")
            def validate_contents(v: str, values: SubmissionFileInfo.Partial) -> str:
                ...
        """

        _directory_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.DirectoryValidator]] = []
        _filename_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.FilenameValidator]] = []
        _contents_validators: typing.ClassVar[typing.List[SubmissionFileInfo.Validators.ContentsValidator]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.DirectoryValidator], SubmissionFileInfo.Validators.DirectoryValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.FilenameValidator], SubmissionFileInfo.Validators.FilenameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"]
        ) -> typing.Callable[
            [SubmissionFileInfo.Validators.ContentsValidator], SubmissionFileInfo.Validators.ContentsValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "directory":
                    cls._directory_validators.append(validator)
                if field_name == "filename":
                    cls._filename_validators.append(validator)
                if field_name == "contents":
                    cls._contents_validators.append(validator)
                return validator

            return decorator

        class DirectoryValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: SubmissionFileInfo.Partial) -> str:
                ...

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: SubmissionFileInfo.Partial) -> str:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, v: str, *, values: SubmissionFileInfo.Partial) -> str:
                ...

    @pydantic.validator("directory")
    def _validate_directory(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._directory_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("filename")
    def _validate_filename(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._filename_validators:
            v = validator(v, values=values)
        return v

    @pydantic.validator("contents")
    def _validate_contents(cls, v: str, values: SubmissionFileInfo.Partial) -> str:
        for validator in SubmissionFileInfo.Validators._contents_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        directory: typing_extensions.NotRequired[str]
        filename: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]

    class Config:
        frozen = True
