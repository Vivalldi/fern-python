# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.language import Language
from .file_info_v_2 import FileInfoV2


class GetBasicSolutionFileResponse(pydantic.BaseModel):
    solution_file_by_language: typing.Dict[Language, FileInfoV2] = pydantic.Field(alias="solutionFileByLanguage")

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetBasicSolutionFileResponse.Validators.field("solution_file_by_language")
            def validate_solution_file_by_language(v: typing.Dict[Language, FileInfoV2], values: GetBasicSolutionFileResponse.Partial) -> typing.Dict[Language, FileInfoV2]:
                ...
        """

        _solution_file_by_language_validators: typing.ClassVar[
            typing.List[GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator]
        ] = []

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["solution_file_by_language"]
        ) -> typing.Callable[
            [GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator],
            GetBasicSolutionFileResponse.Validators.SolutionFileByLanguageValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "solution_file_by_language":
                    cls._solution_file_by_language_validators.append(validator)
                return validator

            return decorator

        class SolutionFileByLanguageValidator(typing_extensions.Protocol):
            def __call__(
                self, v: typing.Dict[Language, FileInfoV2], *, values: GetBasicSolutionFileResponse.Partial
            ) -> typing.Dict[Language, FileInfoV2]:
                ...

    @pydantic.validator("solution_file_by_language")
    def _validate_solution_file_by_language(
        cls, v: typing.Dict[Language, FileInfoV2], values: GetBasicSolutionFileResponse.Partial
    ) -> typing.Dict[Language, FileInfoV2]:
        for validator in GetBasicSolutionFileResponse.Validators._solution_file_by_language_validators:
            v = validator(v, values=values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Partial(typing.TypedDict):
        solution_file_by_language: typing_extensions.NotRequired[typing.Dict[Language, FileInfoV2]]

    class Config:
        frozen = True
        allow_population_by_field_name = True
