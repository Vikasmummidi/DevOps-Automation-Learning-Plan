#!/usr/bin/env python3
# subprocess

import subprocess

subprocess.run(["find","/var/log", "-name", "*.log"])
result=subprocess.run(["df", "-h"],capture_output=True, text = True)
#print(result.stdout)
#print(result.returncode)
usage=result.stdout.splitlines()[1].split()[4]
print(f"Diskusage: {usage}")

result = subprocess.run(["ls", "/nonexistent"], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Exit Code:", result.returncode)


#checking if a service is running
result = subprocess.run(["systemctl","is-active","nginx"], capture_output=True, text=True)
if result.returncode == 0:
    print("✅✅✅ nginx is active")
else:
    print("❌❌❌ nginx is down",result.stdout.strip())

subprocess.run(["false"], check=True)
