# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing

import fastapi
import starlette

from ....core.abstract_fern_service import AbstractFernService
from ....core.exceptions.fern_http_exception import FernHTTPException
from ....core.route_args import get_route_args
from ....security import ApiAuth, FernAuth
from ..errors.playlist_id_not_found_error import PlaylistIdNotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.playlist import Playlist
from ..types.playlist_create_request import PlaylistCreateRequest
from ..types.update_playlist_request import UpdatePlaylistRequest


class AbstractPlaylistCrudService(AbstractFernService):
    """
    AbstractPlaylistCrudService is an abstract class containing the methods that your
    PlaylistCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def create_playlist(self, *, body: PlaylistCreateRequest, service_param: int, auth: ApiAuth) -> Playlist:
        """
        Create a new playlist
        """
        ...

    @abc.abstractmethod
    def get_playlists(
        self, *, service_param: int, limit: typing.Optional[int], other_field: str, auth: ApiAuth
    ) -> typing.List[Playlist]:
        """
        Returns the user's playlists
        """
        ...

    @abc.abstractmethod
    def get_playlist(self, *, service_param: int, playlist_id: str) -> Playlist:
        """
        Returns a playlist
        """
        ...

    @abc.abstractmethod
    def update_playlist(
        self, *, body: typing.Optional[UpdatePlaylistRequest], service_param: int, playlist_id: str, auth: ApiAuth
    ) -> typing.Optional[Playlist]:
        """
        Updates a playlist
        """
        ...

    @abc.abstractmethod
    def delete_playlist(self, *, service_param: int, playlist_id: str, auth: ApiAuth) -> None:
        """
        Deletes a playlist
        """
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_create_playlist(router=router)
        cls.__init_get_playlists(router=router)
        cls.__init_get_playlist(router=router)
        cls.__init_update_playlist(router=router)
        cls.__init_delete_playlist(router=router)

    @classmethod
    def __init_create_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.create_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.create_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.create_playlist)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> Playlist:
            try:
                return cls.create_playlist(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'create_playlist' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.create_playlist.__globals__)

        router.post(
            path="/v2/playlist/{service_param}/create",
            response_model=Playlist,
            description=cls.create_playlist.__doc__,
            **get_route_args(cls.create_playlist, default_tag="playlist"),
        )(wrapper)

    @classmethod
    def __init_get_playlists(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_playlists)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "limit":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=None)))
            elif parameter_name == "other_field":
                new_parameters.append(parameter.replace(default=fastapi.Query(default=..., alias="otherField")))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_playlists, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_playlists)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.List[Playlist]:
            try:
                return cls.get_playlists(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_playlists' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_playlists.__globals__)

        router.get(
            path="/v2/playlist/{service_param}/all",
            response_model=typing.List[Playlist],
            description=cls.get_playlists.__doc__,
            **get_route_args(cls.get_playlists, default_tag="playlist"),
        )(wrapper)

    @classmethod
    def __init_get_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_playlist)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> Playlist:
            try:
                return cls.get_playlist(*args, **kwargs)
            except (PlaylistIdNotFoundError, UnauthorizedError) as e:
                raise e
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_playlist' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_playlist.__globals__)

        router.get(
            path="/v2/playlist/{service_param}/{playlist_id}",
            response_model=Playlist,
            description=cls.get_playlist.__doc__,
            **get_route_args(cls.get_playlist, default_tag="playlist"),
        )(wrapper)

    @classmethod
    def __init_update_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.update_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.update_playlist)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Optional[Playlist]:
            try:
                return cls.update_playlist(*args, **kwargs)
            except PlaylistIdNotFoundError as e:
                raise e
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'update_playlist' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.update_playlist.__globals__)

        router.put(
            path="/v2/playlist/{service_param}/{playlist_id}",
            response_model=typing.Optional[Playlist],
            description=cls.update_playlist.__doc__,
            **get_route_args(cls.update_playlist, default_tag="playlist"),
        )(wrapper)

    @classmethod
    def __init_delete_playlist(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.delete_playlist)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "service_param":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "playlist_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.delete_playlist, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.delete_playlist)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.delete_playlist(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'delete_playlist' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.delete_playlist.__globals__)

        router.delete(
            path="/v2/playlist/{service_param}/{playlist_id}",
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=cls.delete_playlist.__doc__,
            **get_route_args(cls.delete_playlist, default_tag="playlist"),
        )(wrapper)
