import typing

import pydantic

from ..commons.problem_id import ProblemId


class PlaylistCreateRequest(pydantic.BaseModel):
    name: str
    problems: typing.List[ProblemId]

    def json(self, **kwargs) -> str:  # type: ignore
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)
