#!/usr/bin/env python3
#functions script
import os
import shutil

def greet(name):
    return f"Hi {name}!!!"


print(greet("vikas"))

#filehandling

#with open() as is an context manager it opens and closes the files for you without explicitly calling f.close()
def write_data():
    with open("notes.txt", 'w')as f:
        f.writelines(["DevOps\n", "AWS\n", "Terraform\n"])
    print("File created and written.")

def read_data():
    with open("notes.txt", 'r') as f:
        for line in f:
            print(line.strip())

def append_data():
    with open("notes.txt", 'a') as f:
        f.write("Docker/n")

    print("appended successfully!")

write_data()
read_data()
append_data()



