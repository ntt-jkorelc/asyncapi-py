from __future__ import annotations

from typing import Union

from pydantic import (
    BaseModel,
    Field,
)

from asyncapi.auth import OAuthFlows
from asyncapi.base import BaseApi
from asyncapi.server import ServerVariable
from asyncapi.types import Reference


class Contact(BaseApi):
    name: str
    url: str
    email: str


class Correlation(BaseApi):
    description: str                    # TODO: CommonMark syntax
    location: str                       # TODO: runtime expression


class License(BaseApi):
    name: str
    url: str | None     # TODO: MUST be an absolute URL


class SecurityScheme(BaseApi):
    type: str           # TODO: list of values validation
    description: str    # TODO: CommonMark syntax
    name: str
    in_: str = Field(serialization_alias="in")
    scheme: str
    bearer_format: str
    flows: OAuthFlows


class Server(BaseApi):
    host: str
    protocol: str
    protocol_version: str | None = None
    pathname: str | None = None     # TODO: Server Variables
    description: str | None = None  # TODO: Common Mark
    title: str | None = None
    summary: str | None = None
    variables: dict[str, ServerVariable | Reference] | None = None
    security: Union[SecurityScheme | Reference] | None = None
    tags: Tags
    external_docs: Union[ExternalDoc | Reference] | None = None
    bindings: Union[ServerBinding | Reference] | None = None


class ServerVariable(BaseApi):
    """
    https://www.asyncapi.com/docs/reference/specification/v3.0.0#serverVariableObject
    """

    enum: list[str] | None = None
    default: str | None = None
    description: str | None = None      # TODO: CommonMark syntax
    examples: list[str] | None = None


class Tags(BaseApi):
    name: str
    description: str | None = None      # TODO: CommonMark syntax
    external_docs: ExternalDoc | Reference | None = None


class Variable(BaseApi):
    enum: list[str] | None = None
    default: str | None = None
    description: str | None = None      # TODO: CommonMark syntax
    examples: list[str] | None = None