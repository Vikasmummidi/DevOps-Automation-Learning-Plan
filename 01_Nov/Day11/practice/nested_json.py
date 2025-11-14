#!/usr/bin/env python3
#nested json parsing
import json
with open("instances.json") as f:
    d= json.load(f)

high_cpu=[i["id"] for i in d["instances"] if i["cpu"] > 80]
print (high_cpu)
