# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from .....core.datetime_utils import serialize_datetime


class Responsibilities(pydantic.BaseModel):
    job_title: typing.Optional[str] = pydantic.Field(alias="jobTitle")
    is_controller: typing.Optional[bool] = pydantic.Field(alias="isController")
    is_owner: typing.Optional[bool] = pydantic.Field(alias="isOwner")
    ownership_percentage: typing.Optional[float] = pydantic.Field(alias="ownershipPercentage")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
