import httpx
import typing

class BaseClientWrapper:
    def __init__(self, token: typing.Union[str, typing.Callable[[], str]]): 
        self._token = token

    def get_headers(self) -> typing.Dict[str, str]:
        return {
            "X-Fern-Version": "1324",
            "Authorization": f"Bearer {self._get_token()}",
        }

    def _get_token(self) -> str:
        if isinstance(self._token, str):
            return self._token
        else:
            return self._token()


class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, httpx_client: httpx.Client, token: typing.Union[str, typing.Callable[[], str]]): 
        super().__init__(token)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper): 
    def __init__(self, httpx_client: httpx.AsyncClient, token: typing.Union[str, typing.Callable[[], str]]): 
        super().__init__(token)
        self.httpx_client = httpx_client
