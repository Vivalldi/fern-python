# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .playlist_id import PlaylistId

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def playlist_id(self, value: PlaylistId) -> PlaylistIdNotFoundErrorBody:
        return PlaylistIdNotFoundErrorBody(
            __root__=_PlaylistIdNotFoundErrorBody.PlaylistId(type="playlistId", value=value)
        )


class PlaylistIdNotFoundErrorBody(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]:
        return self.__root__

    def visit(self, playlist_id: typing.Callable[[PlaylistId], T_Result]) -> T_Result:
        if self.__root__.type == "playlistId":
            return playlist_id(self.__root__.playlist_id)

    __root__: typing_extensions.Annotated[
        typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId], pydantic.Field(discriminator="type")
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @PlaylistIdNotFoundErrorBody.Validators.validate
            def validate(value: typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]) -> typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]],
                    typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId]],
                typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(typing.Union[_PlaylistIdNotFoundErrorBody.PlaylistId], values.get("__root__"))
        for validator in PlaylistIdNotFoundErrorBody.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True


class _PlaylistIdNotFoundErrorBody:
    class PlaylistId(pydantic.BaseModel):
        type: typing_extensions.Literal["playlistId"]
        value: PlaylistId

        class Config:
            frozen = True


PlaylistIdNotFoundErrorBody.update_forward_refs()
