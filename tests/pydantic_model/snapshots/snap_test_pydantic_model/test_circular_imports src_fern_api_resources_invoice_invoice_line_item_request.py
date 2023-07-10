# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ...core.datetime_utils import serialize_datetime
from ..payment_method.currency_code import CurrencyCode


class InvoiceLineItemRequest(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(
        description=(
            "If provided, will overwrite line item on the invoice with this ID. If not provided, will create a new line item.\n"
        )
    )
    amount: typing.Optional[float]
    currency: typing.Optional[CurrencyCode]
    description: typing.Optional[str]
    name: typing.Optional[str]
    quantity: typing.Optional[int]
    unit_price: typing.Optional[float] = pydantic.Field(alias="unitPrice")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
