# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ..errors.errors.bad_request import BadRequest
from ..errors.errors.unauthorized_request import UnauthorizedRequest
from ..errors.types.unauthorized_request_error_body import UnauthorizedRequestErrorBody

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BasicAuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_with_basic_auth(self) -> bool:
        """
        GET request with basic auth scheme
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "basic-auth"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(bool, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedRequest(
                pydantic.parse_obj_as(UnauthorizedRequestErrorBody, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def post_with_basic_auth(self, *, request: typing.Any) -> bool:
        """
        POST request with basic auth scheme

        Parameters:
            - request: typing.Any.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "basic-auth"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(bool, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedRequest(
                pydantic.parse_obj_as(UnauthorizedRequestErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 400:
            raise BadRequest()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBasicAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_with_basic_auth(self) -> bool:
        """
        GET request with basic auth scheme
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "basic-auth"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(bool, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedRequest(
                pydantic.parse_obj_as(UnauthorizedRequestErrorBody, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def post_with_basic_auth(self, *, request: typing.Any) -> bool:
        """
        POST request with basic auth scheme

        Parameters:
            - request: typing.Any.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "basic-auth"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(bool, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedRequest(
                pydantic.parse_obj_as(UnauthorizedRequestErrorBody, _response.json())  # type: ignore
            )
        if _response.status_code == 400:
            raise BadRequest()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
