from __future__ import annotations

from asyncapi.core import (
    BaseApi,
    Field,
)

from asyncapi.binding.core import FrozenBinding


BINDING_VERSION: str = "0.1.0"


class MessageStoragePolicy(BaseApi):
    allowed_persistence_regions: list[str] | None = None


class SchemaSettings(BaseApi):
    encoding: str | None = None
    first_revision_id: str | None = None
    last_revision_id: str | None = None
    name: str | None = None


class Server(FrozenBinding):
    ...

class ChannelBinding(FrozenBinding):
    binding_version: str = Field(BINDING_VERSION)
    labels: dict | None = None
    message_retention_duration: str | None = None
    message_storage_policy: MessageStoragePolicy | None = None
    schema_settings: SchemaSettings | None = None


class MessageBinding(FrozenBinding):
    binding_version: str = Field(BINDING_VERSION)
    attributes: dict | None = None
    ordering_key: str | None = None
    schema: SchemaDefinition | None = None


class SchemaDefinition(BaseApi):
    name: str | None



class OperationBinding(FrozenBinding):
    ...


class ServerBinding(FrozenBinding):
    ...