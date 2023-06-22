# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .resources.movie.client import AsyncMovieClient, MovieClient


class FernIr:
    def __init__(self, *, environment: str, api_key: typing.Optional[str] = None, api_secret: typing.Optional[str] = None):
        self._environment = environment
        self._api_key = api_key
        self._api_secret = api_secret
        self._client = httpx.Client(timeout=60)self.movie = MovieClient(environment=self._environment, api_key=self._api_key, api_secret=self._api_secret, client=self._client)
class AsyncFernIr:
    def __init__(self, *, environment: str, api_key: typing.Optional[str] = None, api_secret: typing.Optional[str] = None):
        self._environment = environment
        self._api_key = api_key
        self._api_secret = api_secret
        self._client = httpx.AsyncClient(timeout=60)self.movie = AsyncMovieClient(environment=self._environment, api_key=self._api_key, api_secret=self._api_secret, client=self._client)
