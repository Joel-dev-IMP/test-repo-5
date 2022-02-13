import json
import os

INIT_PATH = "./__init__.py"
ENDPOINT_PATH = "./SuperAddonManager-Endpoint.json"
ENDPOINT_OUT_PATH = "./SuperAddonManager-EndpointN.json"

print(os.listdir("./"))

with open(INIT_PATH, "r") as f:
    data: str = f.read()

data = data.replace("d!", "d Version 1.1!")
data = data.replace("(1, 0, 0)", "(1, 1, 0)")

with open(INIT_PATH, "w+") as f:
    f.write(data)

new_endpoint_version = {
    "version": [
        1,
        1,
        0
    ],
    "allow_automatic_download": True,
    "download_url": "https://github.com/Joel-dev-IMP/test-repo-5/releases/download/1_1_0/test-repo-5.zip",
    "minimum_blender_version": [
        2,
        83,
        0
    ]
}

with open(ENDPOINT_PATH, "r") as f:
    endpoint_data = json.load(f)

endpoint_data["versions"].insert(0, new_endpoint_version)

with open(ENDPOINT_OUT_PATH, "w+") as f:
    json.dump(endpoint_data, f, indent=4)
