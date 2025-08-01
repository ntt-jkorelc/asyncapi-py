from asyncapi.core import BaseApi

from asyncapi.binding.core import FrozenBinding


BINDING_VERSION: str = "0.1.0"


class Server(FrozenBinding):
    protocol: Literal["anypointmq"]
    host: HttpUrl       # TODO: url validation without path suffix
    pathname: str
    protocol_version: str = Field("v1")
    security: str


class ServerBinding(FrozenBinding):
    """
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class ChannelBinding(FrozenBinding):
    """
    The Anypoint MQ Channel Binding Object is defined by a JSON Schema.
    """
    destination: str | None = None
    destination_type: str | None = None
    binding_version: str = Field(BINDING_VERSION)


class QueueBinding(FrozenBinding):
    """
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class MessageBinding(FrozenBinding):
    headers: Union[Schema | Reference] | None = None
    binding_version: str = Field(BINDING_VERSION)
