# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(
        self,
        *,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        api_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        base_url: str
    ):
        self._api_key = api_key
        self._api_secret = api_secret
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "my-package-name",
            "X-Fern-SDK-Version": "1.0.0",
        }
        api_key = self._get_api_key()
        api_secret = self._get_api_secret()
        if api_key is not None and api_secret is not None:
            headers["Authorization"] = httpx.BasicAuth(api_key, api_secret)._auth_header
        return headers

    def _get_api_key(self) -> typing.Optional[str]:
        if isinstance(self._api_key, str) or self._api_key is None:
            return self._api_key
        else:
            return self._api_key()

    def _get_api_secret(self) -> typing.Optional[str]:
        if isinstance(self._api_secret, str) or self._api_secret is None:
            return self._api_secret
        else:
            return self._api_secret()

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        api_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        base_url: str,
        httpx_client: httpx.Client
    ):
        super().__init__(api_key=api_key, api_secret=api_secret, base_url=base_url)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        api_secret: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        base_url: str,
        httpx_client: httpx.AsyncClient
    ):
        super().__init__(api_key=api_key, api_secret=api_secret, base_url=base_url)
        self.httpx_client = httpx_client
