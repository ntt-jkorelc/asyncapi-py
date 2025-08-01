from .base import BaseApi


class ServerVariable(BaseApi):
    enum: list[str] | None = None
    default: str | None = None
    description: str | None = None      # TODO: CommonMark syntax
    examples: list[str] | None = None