# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ...core.datetime_utils import serialize_datetime
from .color_scheme_response import ColorSchemeResponse
from .email_provider_response import EmailProviderResponse
from .organization_id import OrganizationId
from .payment_methods_response import PaymentMethodsResponse


class OrganizationResponse(pydantic.BaseModel):
    id: OrganizationId
    sandbox: bool
    name: str
    logo_url: typing.Optional[str] = pydantic.Field(alias="logoUrl")
    website_url: typing.Optional[str] = pydantic.Field(alias="websiteUrl")
    support_email: typing.Optional[str] = pydantic.Field(alias="supportEmail")
    payment_methods: typing.Optional[PaymentMethodsResponse] = pydantic.Field(alias="paymentMethods")
    email_provider: typing.Optional[EmailProviderResponse] = pydantic.Field(alias="emailProvider")
    color_scheme: typing.Optional[ColorSchemeResponse] = pydantic.Field(alias="colorScheme")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
