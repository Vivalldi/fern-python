# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.language import Language
from ...v_2.problem.types.files import Files


class WorkspaceStarterFilesResponseV2(pydantic.BaseModel):
    files_by_language: typing.Dict[Language, Files] = pydantic.Field(alias="filesByLanguage")

    class Partial(typing_extensions.TypedDict):
        files_by_language: typing_extensions.NotRequired[typing.Dict[Language, Files]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceStarterFilesResponseV2.Validators.root
            def validate(values: WorkspaceStarterFilesResponseV2.Partial) -> WorkspaceStarterFilesResponseV2.Partial:
                ...

            @WorkspaceStarterFilesResponseV2.Validators.field("files_by_language")
            def validate_files_by_language(files_by_language: typing.Dict[Language, Files], values: WorkspaceStarterFilesResponseV2.Partial) -> typing.Dict[Language, Files]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[[WorkspaceStarterFilesResponseV2.Partial], WorkspaceStarterFilesResponseV2.Partial]
            ]
        ] = []
        _files_by_language_validators: typing.ClassVar[
            typing.List[WorkspaceStarterFilesResponseV2.Validators.FilesByLanguageValidator]
        ] = []

        @classmethod
        def root(
            cls,
            validator: typing.Callable[
                [WorkspaceStarterFilesResponseV2.Partial], WorkspaceStarterFilesResponseV2.Partial
            ],
        ) -> typing.Callable[[WorkspaceStarterFilesResponseV2.Partial], WorkspaceStarterFilesResponseV2.Partial]:
            cls._validators.append(validator)
            return validator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["files_by_language"]
        ) -> typing.Callable[
            [WorkspaceStarterFilesResponseV2.Validators.FilesByLanguageValidator],
            WorkspaceStarterFilesResponseV2.Validators.FilesByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "files_by_language":
                    cls._files_by_language_validators.append(validator)
                return validator

            return decorator

        class FilesByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[Language, Files], __values: WorkspaceStarterFilesResponseV2.Partial
            ) -> typing.Dict[Language, Files]:
                ...

    @pydantic.root_validator
    def _validate(cls, values: WorkspaceStarterFilesResponseV2.Partial) -> WorkspaceStarterFilesResponseV2.Partial:
        for validator in WorkspaceStarterFilesResponseV2.Validators._validators:
            values = validator(values)
        return values

    @pydantic.validator("files_by_language")
    def _validate_files_by_language(
        cls, v: typing.Dict[Language, Files], values: WorkspaceStarterFilesResponseV2.Partial
    ) -> typing.Dict[Language, Files]:
        for validator in WorkspaceStarterFilesResponseV2.Validators._files_by_language_validators:
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
        allow_population_by_field_name = True
