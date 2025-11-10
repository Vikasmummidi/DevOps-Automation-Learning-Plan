#!/usr/bin/env python3
import subprocess

result=subprocess.run(["ls","-l"],capture_output=True, text=True)
print(result.stdout)

subprocess.run(["whoami"])
subprocess.run(["df","-h"])

response=subprocess.run(["df","-h"],capture_output=True,text=True)

for line in response.stdout.strip().split("\n")[1:]:
    parts = line.split()
    filesystem, size, used, avail, percent, mount = parts
    usage = int(percent.strip('%'))
    if usage < 80:
        print(f"⚠️ ALERT:{mount} is {usage}% full")
        message=f"⚠️ ALERT:{mount} is {usage}% full"
        subprocess.run(["mail", "-s", "Disk Alert-python", "vikasmummidi@gmail.com"], input=message, text=True)
