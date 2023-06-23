# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .resources.ai.client import AiClient, AsyncAiClient


class FernIr:
    def __init__(self, *, environment: str, timeout: typing.Optional[float] = 60):
        self._environment = environment
        self._client = httpx.Client(timeout=timeout)
        self.ai = AiClient(environment=self._environment, client=self._client)


class AsyncFernIr:
    def __init__(self, *, environment: str, timeout: typing.Optional[float] = 60):
        self._environment = environment
        self._client = httpx.AsyncClient(timeout=timeout)
        self.ai = AsyncAiClient(environment=self._environment, client=self._client)
