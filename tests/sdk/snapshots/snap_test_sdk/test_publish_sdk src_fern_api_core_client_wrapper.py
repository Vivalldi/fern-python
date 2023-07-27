# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(self, *, api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None):
        self._api_key = api_key

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {}
        api_key = self._get_api_key()
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"
        return headers

    def _get_api_key(self) -> typing.Optional[str]:
        if isinstance(self._api_key, str) or self._api_key is None:
            return self._api_key
        else:
            return self._api_key()


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(api_key=api_key)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(api_key=api_key)
        self.httpx_client = httpx_client
