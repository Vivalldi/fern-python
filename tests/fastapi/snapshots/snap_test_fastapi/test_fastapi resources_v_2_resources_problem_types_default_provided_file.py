# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .....commons.types.variable_type import VariableType
from .file_info_v_2 import FileInfoV2


class DefaultProvidedFile(pydantic.BaseModel):
    file: FileInfoV2
    related_types: typing.List[VariableType] = pydantic.Field(alias="relatedTypes")

    class Partial(typing_extensions.TypedDict):
        file: typing_extensions.NotRequired[FileInfoV2]
        related_types: typing_extensions.NotRequired[typing.List[VariableType]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DefaultProvidedFile.Validators.root()
            def validate(values: DefaultProvidedFile.Partial) -> DefaultProvidedFile.Partial:
                ...

            @DefaultProvidedFile.Validators.field("file")
            def validate_file(file: FileInfoV2, values: DefaultProvidedFile.Partial) -> FileInfoV2:
                ...

            @DefaultProvidedFile.Validators.field("related_types")
            def validate_related_types(related_types: typing.List[VariableType], values: DefaultProvidedFile.Partial) -> typing.List[VariableType]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[DefaultProvidedFile.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[DefaultProvidedFile.Validators._RootValidator]] = []
        _file_pre_validators: typing.ClassVar[typing.List[DefaultProvidedFile.Validators.PreFileValidator]] = []
        _file_post_validators: typing.ClassVar[typing.List[DefaultProvidedFile.Validators.FileValidator]] = []
        _related_types_pre_validators: typing.ClassVar[
            typing.List[DefaultProvidedFile.Validators.PreRelatedTypesValidator]
        ] = []
        _related_types_post_validators: typing.ClassVar[
            typing.List[DefaultProvidedFile.Validators.RelatedTypesValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators._RootValidator], DefaultProvidedFile.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators._PreRootValidator], DefaultProvidedFile.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["file"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators.PreFileValidator], DefaultProvidedFile.Validators.PreFileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["file"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators.FileValidator], DefaultProvidedFile.Validators.FileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["related_types"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators.PreRelatedTypesValidator],
            DefaultProvidedFile.Validators.PreRelatedTypesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["related_types"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [DefaultProvidedFile.Validators.RelatedTypesValidator], DefaultProvidedFile.Validators.RelatedTypesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "file":
                    if pre:
                        cls._file_pre_validators.append(validator)
                    else:
                        cls._file_post_validators.append(validator)
                if field_name == "related_types":
                    if pre:
                        cls._related_types_pre_validators.append(validator)
                    else:
                        cls._related_types_post_validators.append(validator)
                return validator

            return decorator

        class PreFileValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DefaultProvidedFile.Partial) -> typing.Any:
                ...

        class FileValidator(typing_extensions.Protocol):
            def __call__(self, __v: FileInfoV2, __values: DefaultProvidedFile.Partial) -> FileInfoV2:
                ...

        class PreRelatedTypesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: DefaultProvidedFile.Partial) -> typing.Any:
                ...

        class RelatedTypesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[VariableType], __values: DefaultProvidedFile.Partial
            ) -> typing.List[VariableType]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: DefaultProvidedFile.Partial) -> DefaultProvidedFile.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _prev_2_default_provided_file_validate(cls, values: DefaultProvidedFile.Partial) -> DefaultProvidedFile.Partial:
        for validator in DefaultProvidedFile.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postv_2_default_provided_file_validate(
        cls, values: DefaultProvidedFile.Partial
    ) -> DefaultProvidedFile.Partial:
        for validator in DefaultProvidedFile.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("file", pre=True)
    def _pre_validate_file(cls, v: FileInfoV2, values: DefaultProvidedFile.Partial) -> FileInfoV2:
        for validator in DefaultProvidedFile.Validators._file_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("file", pre=False)
    def _post_validate_file(cls, v: FileInfoV2, values: DefaultProvidedFile.Partial) -> FileInfoV2:
        for validator in DefaultProvidedFile.Validators._file_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("related_types", pre=True)
    def _pre_validate_related_types(
        cls, v: typing.List[VariableType], values: DefaultProvidedFile.Partial
    ) -> typing.List[VariableType]:
        for validator in DefaultProvidedFile.Validators._related_types_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("related_types", pre=False)
    def _post_validate_related_types(
        cls, v: typing.List[VariableType], values: DefaultProvidedFile.Partial
    ) -> typing.List[VariableType]:
        for validator in DefaultProvidedFile.Validators._related_types_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
