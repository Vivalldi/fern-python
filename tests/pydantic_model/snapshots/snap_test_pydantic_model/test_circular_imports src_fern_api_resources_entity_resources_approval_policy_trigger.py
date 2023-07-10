# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .amount_trigger import AmountTrigger


class Trigger_Amount(AmountTrigger):
    type: typing_extensions.Literal["amount"]

    class Config:
        allow_population_by_field_name = True


class Trigger_All(pydantic.BaseModel):
    type: typing_extensions.Literal["all"]
    value: typing.Any


Trigger = typing.Union[Trigger_Amount, Trigger_All]
