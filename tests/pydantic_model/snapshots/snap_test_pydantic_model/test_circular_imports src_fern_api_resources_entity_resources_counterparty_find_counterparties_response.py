# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from .....core.datetime_utils import serialize_datetime
from .counterparty_response import CounterpartyResponse


class FindCounterpartiesResponse(pydantic.BaseModel):
    entity_counterparties: typing.List[CounterpartyResponse] = pydantic.Field(
        alias="entityCounterparties", description=("Counterparties that have been paid by this entity\n")
    )
    platform_counterparties: typing.List[CounterpartyResponse] = pydantic.Field(
        alias="platformCounterparties", description=("Counterparties that have paid by any entity on your platform\n")
    )
    mercoa_counterparties: typing.List[CounterpartyResponse] = pydantic.Field(
        alias="mercoaCounterparties", description=("External counterparties that have been verified by Mercoa\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
