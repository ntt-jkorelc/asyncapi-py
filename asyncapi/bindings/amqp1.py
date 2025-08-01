from asyncapi.core import BaseApi

from asyncapi.binding.core import FrozenBinding


__all__ = ["AMPQ1Binding"]


BINDING_VERSION: str = "0.1.0"


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


class QueueBinding(FrozenBinding):
    """
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class MessageBinding(FrozenBinding):
    """
    This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class AMPQ1Binding(BaseApi):
    server: ServerBinding
    channel: ChannelBinding
    queue: QueueBinding
    message: MessageBinding