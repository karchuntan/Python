import yaml
import random

with open("example.yml", "r") as f:
    data = yaml.safe_load(f)

print(data, '\n')

with open("game_config.yml", "r") as f:
    config = yaml.safe_load(f)

range_min = config['range']['min']

data = {
    "name": "Mike",
    "age": 25,
    "languages": ["python", "java"],
    "address": {
        "city": "BM"
    }
}

# write yaml files
with open("write.yml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)

# referencing objects in yaml
with open("complex.yml", "r") as f:
    data = yaml.safe_load(f)
print(data)