#!/usr/bin/env python3
#function based scripting

import os
import shutil

def create_file(filename, content):
    with open (filename, 'w') as f:
        f.write(content)
    return filename

def backup_file(filename):
    os.makedirs("backup",exist_ok=True)
    shutil.copy(filename,f"backup/{filename}")
    print (f"{filename} copied to backup")

def read_file(filename):
    with open (filename,'r') as f:
        print(f.read())



if __name__=="__main__":
    file=create_file("report.txt","System health report\n")
    read_file(file)
    backup_file(file)
