import yaml

with open("config.yaml") as f:
    data= yaml.safe_load(f)
    print(data["database"]["host"])
with open("output.yaml", 'w') as f:
    yaml.safe_dump(data,f)
