from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)

from pydantic.


def normalize_field_name(value: str) -> str:
    return to_camel(value).lstrip("_")


class FrozenBinding(BaseModel):
    model_config: ConfigDict = ConfigDict(
        extra="forbid",
        alias_generator=normalize_field_name,
    )


class Exchange(BaseModel):
    name: str
    type_: str
    durable: bool
    auto_delete: bool
    vhost: str = Field("/")


class Queue(BaseModel):
    name: str = Field(constr=255)
    durable: bool
    exclusive: bool
    auto_delete: bool
    vhost: str = Field("/")
