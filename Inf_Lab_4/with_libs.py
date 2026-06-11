import yaml
import tomli_w

with open("input2.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
if isinstance(data, list):
    data = {"item": data}
with open("output2.toml", "w", encoding="utf-8") as f:
    f.write(tomli_w.dumps(data))