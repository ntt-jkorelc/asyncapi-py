from pydantic import BaseModel, ConfigDict


class Channels(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="allow")

    def __getattr__(self, key: str):
        if not hasattr(self, key):
            

class MagicMethod(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")

    channels: Channels