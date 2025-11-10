#!/usr/bin/env python3
#startswith()

servers = ["prod-app1", "dev-db", "prod-db2", "stage-web", "prod-redis"]
for server in servers:
    if server.startswith("prod"):
        print(server)

#conditionals
cpu_usage = int(input("Please enter the current cpu usage:"))

if cpu_usage > 90:
    print("CRITICAL: CPU usage high")
elif cpu_usage > 70:
    print("WARNING: CPU usage moderate")
else:
    print("OK: CPU normal")

#for and while loops
for i in range(1, 10):
    print (f"iteration: {i}")

#while loop
x = 1
while x<=5:
    print("counting:",x)
    x += 1

