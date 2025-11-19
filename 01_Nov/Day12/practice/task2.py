#!/usr/bin/env python3
#logging


try:
    with open("data.txt") as f:
     num=int(f.read())

except FileNotFoundError:
    print("No file with such name")

except valueError:
    print("content cannot be parsed")

finally:
    print("cleaning up ...")
