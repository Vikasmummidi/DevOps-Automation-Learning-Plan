#!/usr/bin/env python3
import yaml

with open("deployment.yaml", 'r') as f:
    d = yaml.safe_load(f)

env_var=d["spec"]["template"]["spec"]["containers"][0]["env"][0]   
print(f"printing env variable: {env_var}")
