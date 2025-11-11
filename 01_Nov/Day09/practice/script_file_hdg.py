#!/usr/bin/env python3
#filehandling count lines
import os
import shutil

with open("notes.txt", 'r') as f:
    lines=f.readlines()
with open("notes.txt", 'w') as f:
    for line in lines:
        if "AWS" in line:
            line=line.replace("AWS","AWS_cloud")
            print(f"AWS is replaced with AWS_cloud in {line}")
        f.write(line)

