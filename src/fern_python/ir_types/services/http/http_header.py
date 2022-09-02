from __future__ import annotations
from ...commons.with_docs import WithDocs
from ...commons.wire_string_with_all_casings import WireStringWithAllCasings
from ...types.type_reference import TypeReference
import pydantic


class HttpHeader(WithDocs):
    name: WireStringWithAllCasings
    value_type: TypeReference = pydantic.Field(alias="valueType")

    class Config:
        allow_population_by_field_name = True
