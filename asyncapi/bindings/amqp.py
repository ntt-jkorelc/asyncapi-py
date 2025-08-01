from .core import (
    FrozenBinding,
    Exchange,
    Field,
    Queue,
)


BINDING_VERSION: str = "0.3.0"


class ServerBinding(BindingFrozen):
    """
        This object MUST NOT contain any properties. Its name is reserved for future use.
    """
    ...


class ChannelBinding(FrozenBinding):
    is_: Literal["queue", "routingKey"] = Field("routingKey")
    exchange: Exchange | None = None
    queue: Queue | None = None
    binding_version: str = Field(BINDING_VERSION)


class OperationBinding(FrozenBinding):
    """
    This object contains information about the operation representation in AMQP.
    """

    expiration: int = Field(ge=1)
    user_id: str | None = None
    cc: list[str] | None = None
    priority: int | None = None
    delivery_mode: str | None = None
    mandatory: bool | None = None
    bcc: list[str] | None = None
    timestamp: bool | None = None
    ack: bool | None = None
    binding_version: Field(BINDING_VERSION)


class MessageBinding(FrozenBinding):
    """
    This object contains information about the message representation in AMQP.
    """

    content_encoding: str | None = None
    message_type: str | None = None
    binding_version: str = Field(BINDING_VERSION)
