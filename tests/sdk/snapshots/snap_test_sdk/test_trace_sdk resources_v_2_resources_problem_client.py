# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....environment import FernIrEnvironment
from ....commons.types.problem_id import ProblemId
from .types.lightweight_problem_info_v_2 import LightweightProblemInfoV2
from .types.problem_info_v_2 import ProblemInfoV2


class ProblemClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PROD, client_wrapper: AsyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def get_lightweight_problems(self) -> typing.List[LightweightProblemInfoV2]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "problems-v2/lightweight-problem-info"),
            headers=self.__client_wrapper,
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LightweightProblemInfoV2], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_problems(self) -> typing.List[ProblemInfoV2]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "problems-v2/problem-info"),
            headers=self.__client_wrapper,
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ProblemInfoV2], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_latest_problem(self, problem_id: ProblemId) -> ProblemInfoV2:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"problems-v2/problem-info/{problem_id}"),
            headers=self.__client_wrapper,
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_problem_version(self, problem_id: ProblemId, problem_version: int) -> ProblemInfoV2:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"problems-v2/problem-info/{problem_id}/version/{problem_version}"
            ),
            headers=self.__client_wrapper,
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncProblemClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PROD, client_wrapper: SyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def get_lightweight_problems(self) -> typing.List[LightweightProblemInfoV2]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "problems-v2/lightweight-problem-info"),
                headers=self.__client_wrapper,
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LightweightProblemInfoV2], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_problems(self) -> typing.List[ProblemInfoV2]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "problems-v2/problem-info"),
                headers=self.__client_wrapper,
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ProblemInfoV2], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_latest_problem(self, problem_id: ProblemId) -> ProblemInfoV2:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"problems-v2/problem-info/{problem_id}"),
                headers=self.__client_wrapper,
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_problem_version(self, problem_id: ProblemId, problem_version: int) -> ProblemInfoV2:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"problems-v2/problem-info/{problem_id}/version/{problem_version}"
                ),
                headers=self.__client_wrapper,
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ProblemInfoV2, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
