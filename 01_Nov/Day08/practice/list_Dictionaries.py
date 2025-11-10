#!/usr/bin/env python3
#lists and dictionaries

tools = ["Git", "Docker","Jenkins"]
tools.append("kubernetes")
print(tools)

versions = {"Python": 3.11, "Docker": "25.0", "AWS_CLI": 2.15}
print("Tools dictionary:", versions)
print("Docker version:", versions["Docker"])

#how to remove first element from the list
print(tools.pop(0))
print(tools)
del tools[1]
print (tools)
print (f"appending terraform to tools list:{tools.append('Terraform')}")
print (tools)
tools = tools[1:] #slicing excluding 0th element
print (tools)
tools.remove("Terraform") # if we know only name(case-sensitive)
print (tools)

#how to iterate through all keys in dictionary
for key in versions.keys():
    print (key)

for value in versions.values():
    print (value)

for key, value in versions.items():
    print(f"{key} version is {value}")

#how to check a key is present in the dictionary

if "Python" in versions:
    print ("Python exists")
