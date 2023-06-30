# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import FernIrEnvironment
from .types.migration import Migration


class MigrationClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PROD, client_wrapper: AsyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def get_attempted_migrations(self, *, admin_key_header: str) -> typing.List[Migration]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "migration-info/all"),
            headers=remove_none_from_headers({**self.__client_wrapper, "admin-key-header": admin_key_header}),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Migration], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMigrationClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PROD, client_wrapper: SyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def get_attempted_migrations(self, *, admin_key_header: str) -> typing.List[Migration]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "migration-info/all"),
                headers=remove_none_from_headers({**self.__client_wrapper, "admin-key-header": admin_key_header}),
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Migration], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
