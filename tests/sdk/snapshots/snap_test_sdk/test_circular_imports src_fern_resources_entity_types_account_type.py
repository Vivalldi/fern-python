# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountType(str, enum.Enum):
    BUSINESS = "business"
    INDIVIDUAL = "individual"

    def visit(self, business: typing.Callable[[], T_Result], individual: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccountType.BUSINESS:
            return business()
        if self is AccountType.INDIVIDUAL:
            return individual()
