#!/usr/bin/env python3
import subprocess
cmd1=subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
cmd2=subprocess.Popen(["grep","/dev"], stdin=cmd1.stdout,stdout=subprocess.PIPE, text=True)
output,_=cmd2.communicate()
print(output)
print (_)

#timeout handling

try:
    subprocess.run(["sleep","5"], timeout=2)
except subprocess.TimeoutExpired:
    print("command timed out")
