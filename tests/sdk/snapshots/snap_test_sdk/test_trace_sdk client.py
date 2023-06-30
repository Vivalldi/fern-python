# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernIrEnvironment
from .resources.admin.client import AdminClient, AsyncAdminClient
from .resources.homepage.client import AsyncHomepageClient, HomepageClient
from .resources.migration.client import AsyncMigrationClient, MigrationClient
from .resources.playlist.client import AsyncPlaylistClient, PlaylistClient
from .resources.problem.client import AsyncProblemClient, ProblemClient
from .resources.submission.client import AsyncSubmissionClient, SubmissionClient
from .resources.sysprop.client import AsyncSyspropClient, SyspropClient
from .resources.v_2.client import AsyncV2Client, V2Client


class FernIr:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = None
    ):
        self._environment = environment
        self._x_random_header = x_random_header
        self._token = token
        self._client_wrapper = AsyncClientWrapper(
            x_random_header=x_random_header, token=token, httpx_client=httpx.Client(timeout=timeout)
        )
        self.v_2 = V2Client(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.admin = AdminClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.homepage = HomepageClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.migration = MigrationClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.playlist = PlaylistClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.problem = ProblemClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.submission = SubmissionClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.sysprop = SyspropClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )


class AsyncFernIr:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = None
    ):
        self._environment = environment
        self._x_random_header = x_random_header
        self._token = token
        self._client_wrapper = SyncClientWrapper(
            x_random_header=x_random_header, token=token, httpx_client=httpx.AsyncClient(timeout=timeout)
        )
        self.v_2 = AsyncV2Client(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.admin = AsyncAdminClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.homepage = AsyncHomepageClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.migration = AsyncMigrationClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.playlist = AsyncPlaylistClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.problem = AsyncProblemClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.submission = AsyncSubmissionClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
        self.sysprop = AsyncSyspropClient(
            environment=self._environment,
            x_random_header=self._x_random_header,
            token=self._token,
            client=self._client_wrapper,
        )
