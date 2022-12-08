# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class FileInfo(pydantic.BaseModel):
    filename: str
    contents: str

    class Partial(typing_extensions.TypedDict):
        filename: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FileInfo.Validators.root()
            def validate(values: FileInfo.Partial) -> FileInfo.Partial:
                ...

            @FileInfo.Validators.field("filename")
            def validate_filename(filename: str, values: FileInfo.Partial) -> str:
                ...

            @FileInfo.Validators.field("contents")
            def validate_contents(contents: str, values: FileInfo.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[FileInfo.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[FileInfo.Validators._RootValidator]] = []
        _filename_pre_validators: typing.ClassVar[typing.List[FileInfo.Validators.FilenameValidator]] = []
        _filename_post_validators: typing.ClassVar[typing.List[FileInfo.Validators.FilenameValidator]] = []
        _contents_pre_validators: typing.ClassVar[typing.List[FileInfo.Validators.ContentsValidator]] = []
        _contents_post_validators: typing.ClassVar[typing.List[FileInfo.Validators.ContentsValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[FileInfo.Validators._RootValidator], FileInfo.Validators._RootValidator]:
            def decorator(validator: FileInfo.Validators._RootValidator) -> FileInfo.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"], *, pre: bool = False
        ) -> typing.Callable[[FileInfo.Validators.FilenameValidator], FileInfo.Validators.FilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"], *, pre: bool = False
        ) -> typing.Callable[[FileInfo.Validators.ContentsValidator], FileInfo.Validators.ContentsValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    if pre:
                        cls._filename_pre_validators.append(validator)
                    else:
                        cls._filename_post_validators.append(validator)
                if field_name == "contents":
                    if pre:
                        cls._contents_pre_validators.append(validator)
                    else:
                        cls._contents_post_validators.append(validator)
                return validator

            return decorator

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfo.Partial) -> str:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfo.Partial) -> str:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: FileInfo.Partial) -> FileInfo.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: FileInfo.Partial) -> FileInfo.Partial:
        for validator in FileInfo.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: FileInfo.Partial) -> FileInfo.Partial:
        for validator in FileInfo.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("filename", pre=True)
    def _pre_validate_filename(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._filename_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=False)
    def _post_validate_filename(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._filename_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=True)
    def _pre_validate_contents(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._contents_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=False)
    def _post_validate_contents(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._contents_post_validators:
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
