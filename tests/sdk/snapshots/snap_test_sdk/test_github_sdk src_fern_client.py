# This file was auto-generated by Fern from our API Definition.

import typing

from .resources.movie.client import AsyncMovieClient, MovieClient


class FernIr:
    def __init__(
        self, *, environment: str, api_key: typing.Optional[str] = None, api_secret: typing.Optional[str] = None
    ):
        self._environment = environment
        self._api_key = api_key
        self._api_secret = api_secret
        self.movie = MovieClient(environment=self._environment, api_key=self._api_key, api_secret=self._api_secret)


class AsyncFernIr:
    def __init__(
        self, *, environment: str, api_key: typing.Optional[str] = None, api_secret: typing.Optional[str] = None
    ):
        self._environment = environment
        self._api_key = api_key
        self._api_secret = api_secret
        self.movie = AsyncMovieClient(environment=self._environment, api_key=self._api_key, api_secret=self._api_secret)
