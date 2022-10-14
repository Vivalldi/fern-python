# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

import fastapi

from .core.security.bearer import BearerToken, HTTPBearer

ApiAuth = BearerToken


def FernAuth(auth: BearerToken = fastapi.Depends(HTTPBearer)) -> BearerToken:
    return auth
