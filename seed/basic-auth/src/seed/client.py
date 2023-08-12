# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.basic_auth.client import AsyncBasicAuthClient, BasicAuthClient


class SeedBasicAuth:
    def __init__(
        self,
        *,
        environment: str,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        self._environment = environment
        self._client_wrapper = SyncClientWrapper(
            username=username, password=password, httpx_client=httpx.Client(timeout=timeout)
        )
        self.basic_auth = BasicAuthClient(environment=environment, client_wrapper=self._client_wrapper)


class AsyncSeedBasicAuth:
    def __init__(
        self,
        *,
        environment: str,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        self._environment = environment
        self._client_wrapper = AsyncClientWrapper(
            username=username, password=password, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.basic_auth = AsyncBasicAuthClient(environment=environment, client_wrapper=self._client_wrapper)
