import typing

import pydantic

from ....commons.variable_type import VariableType
from .file_info_v2 import FileInfoV2


class DefaultProvidedFile(pydantic.BaseModel):
    file: FileInfoV2
    related_types: typing.List[VariableType] = pydantic.Field(alias="relatedTypes")

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
