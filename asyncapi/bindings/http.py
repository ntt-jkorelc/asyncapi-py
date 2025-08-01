from typing import Literal

from asyncpi.types import (
    Schema,
    Reference,
) 


BINDING_VERSION: str = "0.3.0"

BINDING_OPERATIONS: Literal = Literal[    
    "DELETE",
    "GET",
    "CONNECT",
    "HEAD",
    "OPTIONS",
    "POST",
    "PUT",
    "PATCH",
    "TRACE"
]


class ServerBinding(FrozenBinding):
    """
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class ChannelBinding(FrozenBinding):
    """
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class OperationBinding(FrozenBinding):
    method: str
    query: SchemaObject | Reference         # TODO: MUST be of type "object" and have a "properties" key.
    binding_version: str


class MessageBinding(FrozenBinding):
    headers: Schema | Reference
    status_code: int
    binding_version: str

