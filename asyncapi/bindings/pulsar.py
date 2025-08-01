"""
See also:
    https://github.com/asyncapi/bindings/tree/master/pulsar#retention-definition-object
"""

from __future__ import annotations

from typing import Literal

from asyncapi.base import (
    BaseApi,
    Field,
)


class PulsarChannelBinding(BaseApi):
    namespace: str
    persistence: Literal["persistent", "non-persistent"]
    compaction: int
    geo_replication: list[str]
    retention: Retention
    ttl: int
    deduplication: bool
    binding_version: str = Field("latest")


class PulsarServerBinding(BaseApi):
    tenant: str | None = Field("public")
    binding_version: str | None = Field("latest")


class OperationBinding(BaseApi):
    ...


class MessageBinding(BaseApi):
    ...


class Retention(BaseApi):
    time: int = Field(..., description="Time given in minutes")
    size: int = Field(..., description="Size given in megabytes")