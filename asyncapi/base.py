from json import loads as json_loads
from pathlib import Path
from yaml import safe_load


from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)
from pydantic.alias_generators import (
    to_camel,
)


class BaseApi(BaseModel):
    model_config: ConfigDict = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    @classmethod
    def from_json(cls, pathname: str):
        data = Path(pathname).read_text(encoding="utf8")
        data = json_loads(data)
        return cls(**data)

    @classmethod
    def from_yaml(cls, pathname: str):
        data = Path(pathname).read_text(encoding="utf8")
        data = safe_load(data)
        return cls(**data)