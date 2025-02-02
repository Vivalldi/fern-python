# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..errors.errors.property_based_error_test import PropertyBasedErrorTest
from ..errors.types.property_based_error_test_body import PropertyBasedErrorTestBody


class PropertyBasedErrorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def throw_error(self) -> str:
        """
        GET request that always throws an error
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "property-based-error"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "PropertyBasedErrorTest":
                raise PropertyBasedErrorTest(
                    pydantic.parse_obj_as(PropertyBasedErrorTestBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPropertyBasedErrorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def throw_error(self) -> str:
        """
        GET request that always throws an error
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "property-based-error"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "PropertyBasedErrorTest":
                raise PropertyBasedErrorTest(
                    pydantic.parse_obj_as(PropertyBasedErrorTestBody, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
