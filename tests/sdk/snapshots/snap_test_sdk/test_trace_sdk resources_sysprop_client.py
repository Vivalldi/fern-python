# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import FernIrEnvironment
from ..commons.types.language import Language


class SyspropClient:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    def set_num_warm_instances(self, language: Language, num_warm_instances: int) -> None:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"sysprop/num-warm-instances/{language}/{num_warm_instances}"
            ),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_num_warm_instances(self) -> typing.Dict[Language, int]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "sysprop/num-warm-instances"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[Language, int], _response.json())  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSyspropClient:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    async def set_num_warm_instances(self, language: Language, num_warm_instances: int) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"sysprop/num-warm-instances/{language}/{num_warm_instances}"
                ),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
                timeout=None,
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_num_warm_instances(self) -> typing.Dict[Language, int]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "sysprop/num-warm-instances"),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[Language, int], _response.json())  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
