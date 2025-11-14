#!/usr/bin/env python3
import json

with open ("pods.json") as f:
    p = json.load(f)

not_ready=[
        i["metadata"]["name"] 
        for i in p["items"]
        if not i["status"]["phase"] == "Running"

        ]

print(not_ready)
