# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ...core.datetime_utils import serialize_datetime
from ..commons.payment_method_id import PaymentMethodId
from .currency_code import CurrencyCode


class CheckBaseResponse(pydantic.BaseModel):
    id: PaymentMethodId
    pay_to_the_order_of: str = pydantic.Field(alias="payToTheOrderOf")
    address_line_1: str = pydantic.Field(alias="addressLine1")
    address_line_2: typing.Optional[str] = pydantic.Field(alias="addressLine2")
    city: str
    state_or_province: str = pydantic.Field(alias="stateOrProvince")
    postal_code: str = pydantic.Field(alias="postalCode")
    country: str
    supported_currencies: typing.List[CurrencyCode] = pydantic.Field(alias="supportedCurrencies")
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
