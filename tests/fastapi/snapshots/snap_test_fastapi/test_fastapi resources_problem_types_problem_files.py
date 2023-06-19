# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ...commons.types.file_info import FileInfo


class ProblemFiles(pydantic.BaseModel):
    solution_file: FileInfo = pydantic.Field(alias="solutionFile")
    read_only_files: typing.List[FileInfo] = pydantic.Field(alias="readOnlyFiles")

    class Partial(typing_extensions.TypedDict):
        solution_file: typing_extensions.NotRequired[FileInfo]
        read_only_files: typing_extensions.NotRequired[typing.List[FileInfo]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ProblemFiles.Validators.root()
            def validate(values: ProblemFiles.Partial) -> ProblemFiles.Partial:
                ...

            @ProblemFiles.Validators.field("solution_file")
            def validate_solution_file(solution_file: FileInfo, values: ProblemFiles.Partial) -> FileInfo:
                ...

            @ProblemFiles.Validators.field("read_only_files")
            def validate_read_only_files(read_only_files: typing.List[FileInfo], values: ProblemFiles.Partial) -> typing.List[FileInfo]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ProblemFiles.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ProblemFiles.Validators._RootValidator]] = []
        _solution_file_pre_validators: typing.ClassVar[
            typing.List[ProblemFiles.Validators.PreSolutionFileValidator]
        ] = []
        _solution_file_post_validators: typing.ClassVar[typing.List[ProblemFiles.Validators.SolutionFileValidator]] = []
        _read_only_files_pre_validators: typing.ClassVar[
            typing.List[ProblemFiles.Validators.PreReadOnlyFilesValidator]
        ] = []
        _read_only_files_post_validators: typing.ClassVar[
            typing.List[ProblemFiles.Validators.ReadOnlyFilesValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ProblemFiles.Validators._RootValidator], ProblemFiles.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ProblemFiles.Validators._PreRootValidator], ProblemFiles.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["solution_file"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemFiles.Validators.PreSolutionFileValidator], ProblemFiles.Validators.PreSolutionFileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["solution_file"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemFiles.Validators.SolutionFileValidator], ProblemFiles.Validators.SolutionFileValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["read_only_files"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ProblemFiles.Validators.PreReadOnlyFilesValidator], ProblemFiles.Validators.PreReadOnlyFilesValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["read_only_files"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ProblemFiles.Validators.ReadOnlyFilesValidator], ProblemFiles.Validators.ReadOnlyFilesValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "solution_file":
                    if pre:
                        cls._solution_file_pre_validators.append(validator)
                    else:
                        cls._solution_file_post_validators.append(validator)
                if field_name == "read_only_files":
                    if pre:
                        cls._read_only_files_pre_validators.append(validator)
                    else:
                        cls._read_only_files_post_validators.append(validator)
                return validator

            return decorator

        class PreSolutionFileValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemFiles.Partial) -> typing.Any:
                ...

        class SolutionFileValidator(typing_extensions.Protocol):
            def __call__(self, __v: FileInfo, __values: ProblemFiles.Partial) -> FileInfo:
                ...

        class PreReadOnlyFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ProblemFiles.Partial) -> typing.Any:
                ...

        class ReadOnlyFilesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.List[FileInfo], __values: ProblemFiles.Partial) -> typing.List[FileInfo]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ProblemFiles.Partial) -> ProblemFiles.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _preproblem_files_validate(cls, values: ProblemFiles.Partial) -> ProblemFiles.Partial:
        for validator in ProblemFiles.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _postproblem_files_validate(cls, values: ProblemFiles.Partial) -> ProblemFiles.Partial:
        for validator in ProblemFiles.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("solution_file", pre=True)
    def _pre_validate_solution_file(cls, v: FileInfo, values: ProblemFiles.Partial) -> FileInfo:
        for validator in ProblemFiles.Validators._solution_file_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("solution_file", pre=False)
    def _post_validate_solution_file(cls, v: FileInfo, values: ProblemFiles.Partial) -> FileInfo:
        for validator in ProblemFiles.Validators._solution_file_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("read_only_files", pre=True)
    def _pre_validate_read_only_files(
        cls, v: typing.List[FileInfo], values: ProblemFiles.Partial
    ) -> typing.List[FileInfo]:
        for validator in ProblemFiles.Validators._read_only_files_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("read_only_files", pre=False)
    def _post_validate_read_only_files(
        cls, v: typing.List[FileInfo], values: ProblemFiles.Partial
    ) -> typing.List[FileInfo]:
        for validator in ProblemFiles.Validators._read_only_files_post_validators:
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
