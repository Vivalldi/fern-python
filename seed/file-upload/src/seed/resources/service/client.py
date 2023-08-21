# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from .types.maybe_list import MaybeList
from .types.maybe_list_or_set import MaybeListOrSet
from .types.my_object import MyObject

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post(
        self,
        *,
        maybe_string: typing.Optional[str] = None,
        integer: int,
        file: typing.IO,
        maybe_file: typing.IO,
        maybe_integer: typing.Optional[int] = None,
        list_of_strings: typing.List[str],
        set_of_strings: typing.List[str],
        optional_list_of_strings: typing.Optional[typing.List[str]] = None,
        optional_set_of_strings: typing.Optional[typing.List[str]] = None,
        maybe_list: MaybeList,
        optional_maybe_list: typing.Optional[MaybeList] = None,
        maybe_list_or_set: MaybeListOrSet,
        optional_maybe_list_or_set: typing.Optional[MaybeListOrSet] = None,
        list_of_objects: typing.List[MyObject],
    ) -> None:
        """
        Parameters:
            - maybe_string: typing.Optional[str].

            - integer: int.

            - file: typing.IO.

            - maybe_file: typing.IO.

            - maybe_integer: typing.Optional[int].

            - list_of_strings: typing.List[str].

            - set_of_strings: typing.List[str].

            - optional_list_of_strings: typing.Optional[typing.List[str]].

            - optional_set_of_strings: typing.Optional[typing.List[str]].

            - maybe_list: MaybeList.

            - optional_maybe_list: typing.Optional[MaybeList].

            - maybe_list_or_set: MaybeListOrSet.

            - optional_maybe_list_or_set: typing.Optional[MaybeListOrSet].

            - list_of_objects: typing.List[MyObject].
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            self._client_wrapper.get_base_url(),
            data=jsonable_encoder(
                {
                    "maybeString": maybe_string,
                    "integer": integer,
                    "maybeInteger": maybe_integer,
                    "listOfStrings": list_of_strings,
                    "setOfStrings": set_of_strings,
                    "optionalListOfStrings": optional_list_of_strings,
                    "optionalSetOfStrings": optional_set_of_strings,
                    "maybeList": maybe_list,
                    "optionalMaybeList": optional_maybe_list,
                    "maybeListOrSet": maybe_list_or_set,
                    "optionalMaybeListOrSet": optional_maybe_list_or_set,
                    "listOfObjects": list_of_objects,
                }
            ),
            files={"file": file, "maybeFile": maybe_file},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def just_file(self, *, file: typing.IO) -> None:
        """
        Parameters:
            - file: typing.IO.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "just-file"),
            data=jsonable_encoder({}),
            files={"file": file},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post(
        self,
        *,
        maybe_string: typing.Optional[str] = None,
        integer: int,
        file: typing.IO,
        maybe_file: typing.IO,
        maybe_integer: typing.Optional[int] = None,
        list_of_strings: typing.List[str],
        set_of_strings: typing.List[str],
        optional_list_of_strings: typing.Optional[typing.List[str]] = None,
        optional_set_of_strings: typing.Optional[typing.List[str]] = None,
        maybe_list: MaybeList,
        optional_maybe_list: typing.Optional[MaybeList] = None,
        maybe_list_or_set: MaybeListOrSet,
        optional_maybe_list_or_set: typing.Optional[MaybeListOrSet] = None,
        list_of_objects: typing.List[MyObject],
    ) -> None:
        """
        Parameters:
            - maybe_string: typing.Optional[str].

            - integer: int.

            - file: typing.IO.

            - maybe_file: typing.IO.

            - maybe_integer: typing.Optional[int].

            - list_of_strings: typing.List[str].

            - set_of_strings: typing.List[str].

            - optional_list_of_strings: typing.Optional[typing.List[str]].

            - optional_set_of_strings: typing.Optional[typing.List[str]].

            - maybe_list: MaybeList.

            - optional_maybe_list: typing.Optional[MaybeList].

            - maybe_list_or_set: MaybeListOrSet.

            - optional_maybe_list_or_set: typing.Optional[MaybeListOrSet].

            - list_of_objects: typing.List[MyObject].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            self._client_wrapper.get_base_url(),
            data=jsonable_encoder(
                {
                    "maybeString": maybe_string,
                    "integer": integer,
                    "maybeInteger": maybe_integer,
                    "listOfStrings": list_of_strings,
                    "setOfStrings": set_of_strings,
                    "optionalListOfStrings": optional_list_of_strings,
                    "optionalSetOfStrings": optional_set_of_strings,
                    "maybeList": maybe_list,
                    "optionalMaybeList": optional_maybe_list,
                    "maybeListOrSet": maybe_list_or_set,
                    "optionalMaybeListOrSet": optional_maybe_list_or_set,
                    "listOfObjects": list_of_objects,
                }
            ),
            files={"file": file, "maybeFile": maybe_file},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def just_file(self, *, file: typing.IO) -> None:
        """
        Parameters:
            - file: typing.IO.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "just-file"),
            data=jsonable_encoder({}),
            files={"file": file},
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
