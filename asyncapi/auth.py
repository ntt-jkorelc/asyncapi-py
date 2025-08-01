from __future__ import annotations

from typing import Literal

from pydantic import HttpUrl

from .base import BaseApi


class OAuthFlows(BaseApi):
    implicit: OAuthFlow
    password: OAuthFlow
    client_credentials: OAuthFlow
    authorization_code: OAuthFlow


class OAuthFlow(BaseApi):
    authorization_url: HttpUrl      # Literal["implicit", "authorizationCode"]
    token_url: HttpUrl              # Literal["password", "clientCredentials", "authorizationCode"]
    refresh_url: HttpUrl | None = None # oauth2
    available_scopes: dict[str, str]
