from asyncapi.auth import (
    OAuthFlow,
    OAuthFlows,
)


# flows = OAuthFlows.from_json("tests/data/oauth_flows.json")
# flows = OAuthFlows.from_yaml("tests/data/oauth_flows.yaml")
# print(flows)

flow = OAuthFlow.from_yaml("tests/data/oauth_flow.json")
print(flow)

flow = OAuthFlow.from_yaml("tests/data/oauth_flow.yaml")
print(flow)