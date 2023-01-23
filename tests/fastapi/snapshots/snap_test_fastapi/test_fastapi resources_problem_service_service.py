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
from ..types.create_problem_request import CreateProblemRequest
from ..types.create_problem_response import CreateProblemResponse
from ..types.get_default_starter_files_response import GetDefaultStarterFilesResponse
from ..types.update_problem_response import UpdateProblemResponse
from .get_default_starter_files_request import GetDefaultStarterFilesRequest


class AbstractProblemCrudService(AbstractFernService):
    """
    AbstractProblemCrudService is an abstract class containing the methods that your
    ProblemCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def create_problem(self, *, body: CreateProblemRequest) -> CreateProblemResponse:
        """
        Creates a problem
        """
        ...

    @abc.abstractmethod
    def update_problem(self, *, body: CreateProblemRequest, problem_id: str) -> UpdateProblemResponse:
        """
        Updates a problem
        """
        ...

    @abc.abstractmethod
    def delete_problem(self, *, problem_id: str) -> None:
        """
        Soft deletes a problem
        """
        ...

    @abc.abstractmethod
    def get_default_starter_files(self, *, body: GetDefaultStarterFilesRequest) -> GetDefaultStarterFilesResponse:
        """
        Returns default starter files for problem
        """
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_create_problem(router=router)
        cls.__init_update_problem(router=router)
        cls.__init_delete_problem(router=router)
        cls.__init_get_default_starter_files(router=router)

    @classmethod
    def __init_create_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.create_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.create_problem, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.create_problem)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> CreateProblemResponse:
            try:
                return cls.create_problem(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'create_problem' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.create_problem.__globals__)

        router.post(
            path="/problem-crud/create",
            response_model=CreateProblemResponse,
            description=AbstractProblemCrudService.__init_create_problem.__doc__,
            **get_route_args(cls.create_problem, default_tag="problem"),
        )(wrapper)

    @classmethod
    def __init_update_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.update_problem, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.update_problem)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> UpdateProblemResponse:
            try:
                return cls.update_problem(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'update_problem' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.update_problem.__globals__)

        router.post(
            path="/problem-crud/update/{problem_id}",
            response_model=UpdateProblemResponse,
            description=AbstractProblemCrudService.__init_update_problem.__doc__,
            **get_route_args(cls.update_problem, default_tag="problem"),
        )(wrapper)

    @classmethod
    def __init_delete_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.delete_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.delete_problem, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.delete_problem)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.delete_problem(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'delete_problem' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.delete_problem.__globals__)

        router.delete(
            path="/problem-crud/delete/{problem_id}",
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractProblemCrudService.__init_delete_problem.__doc__,
            **get_route_args(cls.delete_problem, default_tag="problem"),
        )(wrapper)

    @classmethod
    def __init_get_default_starter_files(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_default_starter_files)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_default_starter_files, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_default_starter_files)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> GetDefaultStarterFilesResponse:
            try:
                return cls.get_default_starter_files(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_default_starter_files' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_default_starter_files.__globals__)

        router.post(
            path="/problem-crud/default-starter-files",
            response_model=GetDefaultStarterFilesResponse,
            description=AbstractProblemCrudService.__init_get_default_starter_files.__doc__,
            **get_route_args(cls.get_default_starter_files, default_tag="problem"),
        )(wrapper)
