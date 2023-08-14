# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SeedSingleUrlEnvironmentNoDefaultEnvironment
from .resources.dummy.client import AsyncDummyClient, DummyClient


class SeedSingleUrlEnvironmentNoDefault:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: typing.Optional[SeedSingleUrlEnvironmentNoDefaultEnvironment] = None,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        if base_url is None and environment is None:
            raise Exception("Please pass in either base_url or environment to construct the client")
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url if base_url is not None else environment.value,
            token=token,
            httpx_client=httpx.Client(timeout=timeout),
        )
        self.dummy = DummyClient(client_wrapper=self._client_wrapper)


class AsyncSeedSingleUrlEnvironmentNoDefault:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: typing.Optional[SeedSingleUrlEnvironmentNoDefaultEnvironment] = None,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60
    ):
        if base_url is None and environment is None:
            raise Exception("Please pass in either base_url or environment to construct the client")
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url if base_url is not None else environment.value,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout),
        )
        self.dummy = AsyncDummyClient(client_wrapper=self._client_wrapper)
