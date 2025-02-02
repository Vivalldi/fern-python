# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ...core.datetime_utils import serialize_datetime
from .card_brand import CardBrand
from .card_type import CardType


class CardBaseRequest(pydantic.BaseModel):
    card_type: typing.Optional[CardType] = pydantic.Field(alias="cardType")
    card_brand: typing.Optional[CardBrand] = pydantic.Field(alias="cardBrand")
    last_four: typing.Optional[str] = pydantic.Field(alias="lastFour")
    exp_month: typing.Optional[str] = pydantic.Field(alias="expMonth")
    exp_year: typing.Optional[str] = pydantic.Field(alias="expYear")
    token: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
