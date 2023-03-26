# This file was auto-generated by Fern from our API Definition.

import typing
import urllib

import httpx
import pydantic

from ....core.api_error import ApiError
from ....core.remove_none_from_headers import remove_none_from_headers
from ..errors.playlist_id_not_found_error import PlaylistIdNotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.playlist import Playlist
from ..types.playlist_create_request import PlaylistCreateRequest
from ..types.playlist_id import PlaylistId
from ..types.playlist_id_not_found_error_body import PlaylistIdNotFoundErrorBody
from ..types.update_playlist_request import UpdatePlaylistRequest


class PlaylistClient:
    def __init__(
        self, *, environment: str, x_random_header: typing.Optional[str] = None, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    def create_playlist(self, service_param: int, *, request: PlaylistCreateRequest) -> Playlist:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", f"v2/playlist/{service_param}/create"),
            json=request,
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Playlist, _response)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_playlists(
        self,
        service_param: int,
        *,
        limit: typing.Optional[int] = None,
        other_field: str,
        multi_line_docs: str,
        optional_multiple_field: typing.Union[typing.Optional[str], typing.List[str]],
        multiple_field: typing.Union[str, typing.List[str]],
    ) -> typing.List[Playlist]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"v2/playlist/{service_param}/all"),
            params={
                "limit": limit,
                "otherField": other_field,
                "multiLineDocs": multi_line_docs,
                "optionalMultipleField": optional_multiple_field,
                "multipleField": multiple_field,
            },
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Playlist], _response)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_playlist(self, service_param: int, playlist_id: PlaylistId) -> Playlist:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"v2/playlist/{service_param}/{playlist_id}"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Playlist, _response)  # type: ignore
        if _response_json["errorName"] == "PlaylistIdNotFoundError":
            raise PlaylistIdNotFoundError(
                pydantic.parse_obj_as(PlaylistIdNotFoundErrorBody, _response_json[content])  # type: ignore
            )
        if _response_json["errorName"] == "UnauthorizedError":
            raise UnauthorizedError()
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_playlist(
        self, service_param: int, playlist_id: PlaylistId, *, request: typing.Optional[UpdatePlaylistRequest] = None
    ) -> typing.Optional[Playlist]:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(f"{self._environment}/", f"v2/playlist/{service_param}/{playlist_id}"),
            json=request,
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[Playlist], _response)  # type: ignore
        if _response_json["errorName"] == "PlaylistIdNotFoundError":
            raise PlaylistIdNotFoundError(
                pydantic.parse_obj_as(PlaylistIdNotFoundErrorBody, _response_json[content])  # type: ignore
            )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_playlist(self, service_param: int, playlist_id: PlaylistId) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment}/", f"v2/playlist/{service_param}/{playlist_id}"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        _response_json = _response.json()
        raise ApiError(status_code=_response.status_code, body=_response_json)
