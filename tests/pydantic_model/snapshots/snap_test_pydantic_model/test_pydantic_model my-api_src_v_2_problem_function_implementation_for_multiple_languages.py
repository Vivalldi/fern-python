import typing

import pydantic

from ...commons.language import Language
from .function_implementation import FunctionImplementation


class FunctionImplementationForMultipleLanguages(pydantic.BaseModel):
    code_by_language: typing.Dict[Language, FunctionImplementation] = pydantic.Field(alias="codeByLanguage")

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
