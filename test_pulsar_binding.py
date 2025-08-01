from asyncapi.bindings.pulsar import PulsarServerBinding


api = PulsarServerBinding.from_json("tests/data/bindings/pulsar.json")
print(api)
print(api.model_dump_json(indent=4))