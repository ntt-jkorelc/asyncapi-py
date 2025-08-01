"""
See also:
    https://github.com/asyncapi/bindings/tree/master/websockets#server
"""

from typing import Annotated

from pydantic import AfterValidator

from asyncapi.bindings.core import (
    Binding,
    BindingFrozen,
)



def validate_type_object(value: dict):
    if not value["type"] == "object":
        raise ValueError("This schema MUST be of type 'object'.")

    if not value["properties"] == 

    def validate_query(...):
        if not query.type == "object":
        
        
        if not hasattr(self.query, "properties"):
            raise AttributeError("This schema MUST have a 'properties' key.")



class ServerBinding(BindingFrozen):
    ...


class ChannelBinding(Binding):
    method: Literal["GET", "POST"]
    query: Annotated[Schema | Reference, AfterValidator(check_query)]
    headers: Annotated[Schema | Reference, AfterValidator(check_headers)]
    binding_version: str = Field("latest")


class OperationBinding(BindingFrozen):
    ...


class MessageBinding(BindingFrozen):
    ...