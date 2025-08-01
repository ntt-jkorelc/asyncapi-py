from pydantic import BaseModel, ConfigDict


frozen_model_config: ConfigDict = ConfigDict(extra="forbid")


class Binding(BaseModel):
    model_config: ConfigDict = frozen_model_config

    expiration: int | None = None
    user_id: str | None = None


class BindingFrozen(BaseModel):
    model_config: ConfigDict = frozen_model_config

class Binding2(BindingFrozen):
    expiration: int | None = None
    user_id: str | None = None


config_data = {"expiration": 20, "user_id": "user"}
config_extra = {**config_data, "extra_field": True}

"""
binding = Binding()
print(binding)

binding = Binding(**config_data)
print(binding)

binding = Binding(**config_extra)
print(binding)
"""

binding = Binding2(**config_extra)
print(binding)
