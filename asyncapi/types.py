from asyncapi.base import (
    BaseApi,
    Field,
)


class ExternalDocumentation(BaseApi):
    description: str | None = None      # TODO: CommonMark syntax
    url: str | None = None              # TODO: MUST be an absolute url


class Reference(BaseApi):
    ref: str = Field(serialization_alias="$ref")


class Schema(BaseApi):
    ...

    discriminator: str | None = None        # TODO: see Schema and Inheritence
    external_docs: ExternalDocumentation | None = None
    deprecated: bool | None = None