# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ...core.datetime_utils import serialize_datetime
from ..commons.address import Address
from ..commons.birth_date import BirthDate
from ..commons.full_name import FullName
from ..commons.individual_government_id import IndividualGovernmentId
from ..commons.phone_number import PhoneNumber


class IndividualProfileRequest(pydantic.BaseModel):
    email: typing.Optional[str]
    name: FullName
    phone: typing.Optional[PhoneNumber]
    address: typing.Optional[Address]
    birth_date: typing.Optional[BirthDate] = pydantic.Field(alias="birthDate")
    government_id: typing.Optional[IndividualGovernmentId] = pydantic.Field(alias="governmentID")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
