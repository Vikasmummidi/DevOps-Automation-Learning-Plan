#!/usr/bin/env python3
#Directory management

import os
import shutil


def setup_backup():
    if not os.path.exists("backup"):
        os.mkdir("backup")
        print("backup directory created")
    else:
        print("backup directory already exists")


def backup_file():
    if os.path.exists("notes.txt"):
        shutil.copy("notes.txt","backup/backup_file.txt")
        print("file is backed up")
    else:
        print("file not found")

def clean_backup():
    if os.path.exists("backup"):
        shutil.rmtree("backup")
        print("Backup folder removed")


setup_backup()
backup_file()

