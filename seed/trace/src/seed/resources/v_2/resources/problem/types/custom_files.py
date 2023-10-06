# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic
import typing_extensions

from .....commons.types.language import Language
from .basic_custom_files import BasicCustomFiles
from .file_info_v_2 import FileInfoV2
from .files import Files


class CustomFiles_Basic(BasicCustomFiles):
    type: typing_extensions.Literal["basic"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class CustomFiles_Custom(pydantic.BaseModel):
    type: typing_extensions.Literal["custom"]
    value: typing.Dict[Language, Files]

    class Config:
        frozen = True
        smart_union = True


CustomFiles = typing.Union[CustomFiles_Basic, CustomFiles_Custom]
