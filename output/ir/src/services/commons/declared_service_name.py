import pydantic

from ...commons.fern_filepath import FernFilepath


class DeclaredServiceName(pydantic.BaseModel):
    fern_filepath: FernFilepath = pydantic.Field(alias="fernFilepath")
    name: int

    class Config:
        allow_population_by_field_name = True
