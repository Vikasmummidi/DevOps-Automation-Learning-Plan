#!/usr/bin/env python3
#error_handling

def risky_operation():
    a=a*b
try:
    risky_operation()
except ValueError:
    print("Value error occured")
except Exception as e:
    print("General error:", e)
else: 
    print("Runs only if no exception")
finally:
    print("Always executed")

