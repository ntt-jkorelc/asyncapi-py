from pydantic import BaseModel



class InfoObject(BaseModel):
    title: str
    version: str
    description: str | None = None
    terms_of_service: str | None = None
    contact: Contact | None = None
    license: License | None = None
    tags: list[Tag] | None = None
    external_docs: Union[ExternalDoc | Reference | None] = None


class AsyncApi(BaseModel):
    asyncapi: str       # TODO: major.minor.patch validation
    id: str             # TODO: URN format and validation
    info: Info
    servers: Server
