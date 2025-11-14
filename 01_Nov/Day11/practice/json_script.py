#!/usr/bin/env python3
#python json

import json

data = '{"name":"vikas","role":"Devops"}'
parsed = json.loads(data)
print(parsed["role"])

with open ("cofig.json","w") as f:
    json.dump(data, f, indent =4)
