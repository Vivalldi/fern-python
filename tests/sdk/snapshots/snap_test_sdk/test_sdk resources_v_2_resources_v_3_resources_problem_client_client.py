# This file was auto-generated by Fern from our API Definition.

import typing
import urllib

import httpx
import pydantic

from ........core.api_error import ApiError
from ........core.remove_none_from_headers import remove_none_from_headers
from .......commons.types.problem_id import ProblemId
from ..types.lightweight_problem_info_v_2 import LightweightProblemInfoV2
from ..types.problem_info_v_2 import ProblemInfoV2


class Client:
    def __init__(self, *, environment: str, x_random_header: typing.Optional[str], token: typing.Optional[str]):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    def get_lightweight_problems(self) -> typing.List[LightweightProblemInfoV2]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "problems-v2/lightweight-problem-info"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LightweightProblemInfoV2], _response)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_problems(self) -> typing.List[ProblemInfoV2]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "problems-v2/problem-info"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ProblemInfoV2], _response)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_latest_problem(self, *, problem_id: ProblemId) -> ProblemInfoV2:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"problems-v2/problem-info/{problem_id}"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ProblemInfoV2, _response)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_problem_version(self, *, problem_id: ProblemId, problem_version: int) -> ProblemInfoV2:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment}/", f"problems-v2/problem-info/{problem_id}/version/{problem_version}"
            ),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ProblemInfoV2, _response)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
