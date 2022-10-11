import typing

import pydantic
import typing_extensions


class FileInfoV2(pydantic.BaseModel):
    filename: str
    directory: str
    contents: str
    editable: bool

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("filename")
    def _validate_filename(cls, filename: str) -> str:
        for validator in FileInfoV2.Validators._filename_validators:
            filename = validator(filename)
        return filename

    @pydantic.validator("directory")
    def _validate_directory(cls, directory: str) -> str:
        for validator in FileInfoV2.Validators._directory_validators:
            directory = validator(directory)
        return directory

    @pydantic.validator("contents")
    def _validate_contents(cls, contents: str) -> str:
        for validator in FileInfoV2.Validators._contents_validators:
            contents = validator(contents)
        return contents

    @pydantic.validator("editable")
    def _validate_editable(cls, editable: bool) -> bool:
        for validator in FileInfoV2.Validators._editable_validators:
            editable = validator(editable)
        return editable

    class Validators:
        _filename_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _directory_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _contents_validators: typing.ClassVar[typing.List[typing.Callable[[str], str]]] = []
        _editable_validators: typing.ClassVar[typing.List[typing.Callable[[bool], bool]]] = []

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["directory"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"]
        ) -> typing.Callable[[typing.Callable[[str], str]], typing.Callable[[str], str]]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["editable"]
        ) -> typing.Callable[[typing.Callable[[bool], bool]], typing.Callable[[bool], bool]]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    cls._filename_validators.append(validator)
                elif field_name == "directory":
                    cls._directory_validators.append(validator)
                elif field_name == "contents":
                    cls._contents_validators.append(validator)
                elif field_name == "editable":
                    cls._editable_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on FileInfoV2: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
