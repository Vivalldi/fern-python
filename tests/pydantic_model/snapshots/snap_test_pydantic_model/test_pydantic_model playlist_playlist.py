# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ..commons.user_id import UserId
from .playlist_create_request import PlaylistCreateRequest
from .playlist_id import PlaylistId


class Playlist(PlaylistCreateRequest):
    playlist_id: PlaylistId
    owner_id: UserId = pydantic.Field(alias="owner-id")

    class Partial(PlaylistCreateRequest.Partial):
        playlist_id: typing_extensions.NotRequired[PlaylistId]
        owner_id: typing_extensions.NotRequired[UserId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Playlist.Validators.root()
            def validate(values: Playlist.Partial) -> Playlist.Partial:
                ...

            @Playlist.Validators.field("playlist_id")
            def validate_playlist_id(playlist_id: PlaylistId, values: Playlist.Partial) -> PlaylistId:
                ...

            @Playlist.Validators.field("owner_id")
            def validate_owner_id(owner_id: UserId, values: Playlist.Partial) -> UserId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Playlist.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Playlist.Validators._RootValidator]] = []
        _playlist_id_pre_validators: typing.ClassVar[typing.List[Playlist.Validators.PlaylistIdValidator]] = []
        _playlist_id_post_validators: typing.ClassVar[typing.List[Playlist.Validators.PlaylistIdValidator]] = []
        _owner_id_pre_validators: typing.ClassVar[typing.List[Playlist.Validators.OwnerIdValidator]] = []
        _owner_id_post_validators: typing.ClassVar[typing.List[Playlist.Validators.OwnerIdValidator]] = []

        @classmethod
        def root(
            cls, *, pre: bool = False
        ) -> typing.Callable[[Playlist.Validators._RootValidator], Playlist.Validators._RootValidator]:
            def decorator(validator: Playlist.Validators._RootValidator) -> Playlist.Validators._RootValidator:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["playlist_id"], *, pre: bool = False
        ) -> typing.Callable[[Playlist.Validators.PlaylistIdValidator], Playlist.Validators.PlaylistIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["owner_id"], *, pre: bool = False
        ) -> typing.Callable[[Playlist.Validators.OwnerIdValidator], Playlist.Validators.OwnerIdValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "playlist_id":
                    if pre:
                        cls._playlist_id_pre_validators.append(validator)
                    else:
                        cls._playlist_id_post_validators.append(validator)
                if field_name == "owner_id":
                    if pre:
                        cls._owner_id_pre_validators.append(validator)
                    else:
                        cls._owner_id_post_validators.append(validator)
                return validator

            return decorator

        class PlaylistIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: PlaylistId, __values: Playlist.Partial) -> PlaylistId:
                ...

        class OwnerIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: UserId, __values: Playlist.Partial) -> UserId:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Playlist.Partial) -> Playlist.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: Playlist.Partial) -> Playlist.Partial:
        for validator in Playlist.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: Playlist.Partial) -> Playlist.Partial:
        for validator in Playlist.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("playlist_id", pre=True)
    def _pre_validate_playlist_id(cls, v: PlaylistId, values: Playlist.Partial) -> PlaylistId:
        for validator in Playlist.Validators._playlist_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("playlist_id", pre=False)
    def _post_validate_playlist_id(cls, v: PlaylistId, values: Playlist.Partial) -> PlaylistId:
        for validator in Playlist.Validators._playlist_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("owner_id", pre=True)
    def _pre_validate_owner_id(cls, v: UserId, values: Playlist.Partial) -> UserId:
        for validator in Playlist.Validators._owner_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("owner_id", pre=False)
    def _post_validate_owner_id(cls, v: UserId, values: Playlist.Partial) -> UserId:
        for validator in Playlist.Validators._owner_id_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
