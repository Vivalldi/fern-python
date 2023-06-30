# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import FernIrEnvironment
from .errors.invalid_movie_error import InvalidMovieError
from .errors.movie_already_exists_error import MovieAlreadyExistsError
from .errors.movie_not_found_error import MovieNotFoundError
from .types.movie import Movie
from .types.movie_id import MovieId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CommonsClient:
    def __init__(
        self, *, environment: FernIrEnvironment = FernIrEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def get_movie(self, movie_id: MovieId) -> Movie:
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/movie/{movie_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all_movies(self) -> typing.List[Movie]:
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.server_a}/", "movie/all-movies"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_movie(self, *, request: Movie) -> None:
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.server_a}/", "movie/movie"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_movie(self, movie_id: MovieId) -> None:
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/{movie_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCommonsClient:
    def __init__(
        self, *, environment: FernIrEnvironment = FernIrEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def get_movie(self, movie_id: MovieId) -> Movie:
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/movie/{movie_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all_movies(self) -> typing.List[Movie]:
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.server_a}/", "movie/all-movies"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_movie(self, *, request: Movie) -> None:
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.server_a}/", "movie/movie"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_movie(self, movie_id: MovieId) -> None:
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.server_a}/", f"movie/{movie_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
