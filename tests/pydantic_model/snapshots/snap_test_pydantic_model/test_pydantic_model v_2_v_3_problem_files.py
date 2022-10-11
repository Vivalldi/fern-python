import typing

import pydantic
import typing_extensions

from .file_info_v_2 import FileInfoV2


class Files(pydantic.BaseModel):
    files: typing.List[FileInfoV2]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    @pydantic.validator("files")
    def _validate_files(cls, files: typing.List[FileInfoV2]) -> typing.List[FileInfoV2]:
        for validator in Files.Validators._files_validators:
            files = validator(files)
        return files

    class Validators:
        _files_validators: typing.ClassVar[
            typing.List[typing.Callable[[typing.List[FileInfoV2]], typing.List[FileInfoV2]]]
        ] = []

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files"]
        ) -> typing.Callable[
            [typing.Callable[[typing.List[FileInfoV2]], typing.List[FileInfoV2]]],
            typing.Callable[[typing.List[FileInfoV2]], typing.List[FileInfoV2]],
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "files":
                    cls._files_validators.append(validator)
                else:
                    raise RuntimeError("Field does not exist on Files: " + field_name)

                return validator

            return decorator

    class Config:
        frozen = True
