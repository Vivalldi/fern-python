# This file was auto-generated by Fern from our API Definition.

import typing
import urllib
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ....core.api_error import ApiError
from ....core.remove_none_from_headers import remove_none_from_headers
from ..types.migration import Migration


class MigrationClient:
    def __init__(
        self, *, environment: str, x_random_header: typing.Optional[str] = None, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    def get_attempted_migrations(self, *, admin_key_header: str) -> typing.List[Migration]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "migration-info/all"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "admin-key-header": admin_key_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Migration], _response)  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
