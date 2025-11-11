
---

# 🧾 **Day-8 Practice Worksheet**

**Date:** 09-Nov-2025
**Focus Area:** Python
**Topic:** Functions & File Handling (`os`, `shutil`)
**Overview:** Read/write files, manage directories, and build file automation scripts.
**Total Duration:** ⏱️ *2 Hours*

---

## 🕐 **Time Allocation Plan**

| Section   | Topic / Activity                          | Time                 |
| --------- | ----------------------------------------- | -------------------- |
| 1         | Core Concept Explanation                  | 20 mins              |
| 2         | File Handling Practice                    | 25 mins              |
| 3         | Directory Management with `os` & `shutil` | 25 mins              |
| 4         | Function-based Scripting                  | 25 mins              |
| 5         | Real-world Automation (Subprocess Alert)  | 20 mins              |
| 6         | Quick Recap & Review Questions            | 5 mins               |
| **Total** |                                           | **120 mins (2 hrs)** |

---

## 🧠 **1️⃣ Topic Explanation (20 mins)**

### 🔹 **Functions in Python**

* A *function* is a reusable block of code that performs a specific task.
* Defined using `def` keyword.

**Example:**

```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Vikas"))
```

**Key Points:**

* Functions help modularize code.
* Variables declared inside functions are **local**.
* You can pass arguments and return multiple values.
* Use **default arguments** and **keyword arguments** for flexibility.

---

### 🔹 **File Handling Basics**

Python allows file operations using the built-in `open()` function.

**Syntax:**

```python
file = open("demo.txt", "r")   # open file for reading
data = file.read()
file.close()
```

**Modes:**

| Mode | Meaning           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write (overwrite) |
| `a`  | Append            |
| `r+` | Read + Write      |

**Best Practice:** Always use a context manager

```python
with open("demo.txt", "w") as f:
    f.write("Hello File Handling!")
```

→ Auto closes the file safely.

---

### 🔹 **`os` and `shutil` Modules**

Used for file/directory management and automation.

**Common `os` functions:**

```python
import os
os.getcwd()            # Get current directory
os.listdir()           # List all files
os.mkdir("backup")     # Create directory
os.remove("file.txt")  # Delete file
os.path.exists("file") # Check existence
```

**Common `shutil` functions:**

```python
import shutil
shutil.copy("a.txt", "backup/")     # Copy file
shutil.move("a.txt", "archive/")    # Move file
shutil.rmtree("temp/")              # Delete folder tree
shutil.disk_usage("/")              # Get total/free/used space
```

---

## 💻 **2️⃣ File Handling Practice (25 mins)**

### 🧩 Program 1: Write and Read File

**Goal:** Practice file creation, writing, reading, and appending.

```python
# file_practice.py
def write_data():
    with open("notes.txt", "w") as f:
        f.writelines(["DevOps\n", "AWS\n", "Terraform\n"])
    print("File created and written.")

def read_data():
    with open("notes.txt", "r") as f:
        for line in f:
            print(line.strip())

def append_data():
    with open("notes.txt", "a") as f:
        f.write("Docker\n")
    print("Appended successfully!")

write_data()
read_data()
append_data()
```

✅ **Try This:**

* Count number of lines in the file.
* Replace a specific line (e.g., “AWS” → “AWS Cloud”).

---

## 📁 **3️⃣ Directory Management with `os` & `shutil` (25 mins)**

### 🧩 Program 2: Create Backup Folder and Copy File

**Goal:** Automate directory creation and file management.

```python
import os
import shutil

def setup_backup():
    if not os.path.exists("backup"):
        os.mkdir("backup")
        print("Backup folder created.")
    else:
        print("Backup folder already exists.")

def backup_file():
    if os.path.exists("notes.txt"):
        shutil.copy("notes.txt", "backup/notes_backup.txt")
        print("File backed up successfully.")
    else:
        print("File not found!")

def clean_backup():
    if os.path.exists("backup"):
        shutil.rmtree("backup")
        print("Backup folder deleted.")

setup_backup()
backup_file()
# clean_backup()  # Uncomment to remove folder
```

✅ **Try This:**

* List files in the backup directory.
* Move the backup to another folder named `archive/`.

---

## 🧩 **4️⃣ Function-based Scripting (25 mins)**

### Program 3: Combine All Operations

**Goal:** Build modular code using functions.

```python
import os
import shutil

def create_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def backup_file(filename):
    os.makedirs("backup", exist_ok=True)
    shutil.copy(filename, f"backup/{filename}")
    print(f"{filename} copied to backup.")

def read_file(filename):
    with open(filename) as f:
        print(f.read())

if __name__ == "__main__":
    file = create_file("report.txt", "System Health Report\n")
    read_file(file)
    backup_file(file)
```

✅ **Try This:**

* Add a function to delete files older than 7 days (use `os.path.getmtime()`).

---

## ⚙️ **5️⃣ Real-world Automation (20 mins)**

### Program 4: Disk Usage Alert Script

**Goal:** Use `subprocess` to run `df -h`, parse the output, and alert if usage > 80%.

```python
import subprocess

def check_disk_usage():
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    for line in lines[1:]:  # Skip header
        parts = line.split()
        if len(parts) >= 5:
            filesystem, size, used, avail, percent, mount = parts[:6]
            usage = int(percent.strip('%'))
            if usage > 80:
                print(f"ALERT ⚠️ {filesystem} mounted on {mount} is {usage}% full")

if __name__ == "__main__":
    check_disk_usage()
```

✅ **Try This:**

* Redirect alerts to a file `disk_alerts.log`.
* Send alert mail using subprocess and `mail` command (Linux only).

📘 **Reference:** [RealPython subprocess guide](https://realpython.com/python-subprocess/)

---

## 🧩 **6️⃣ Review & Self-Check (5 mins)**

### ✅ Quick Questions:

1. What is the difference between `os.remove()` and `shutil.rmtree()`?
2. Why is `with open()` preferred for file handling?
3. How can you check free disk space using Python?
4. How to handle file not found errors gracefully?
5. What’s the use of `subprocess.run()` over `os.system()`?

---

### 🧭 **Progress Tracker**

| Task                  | Status (✔️/❌) |
| --------------------- | ------------- |
| File Handling Basics  |               |
| Directory Operations  |               |
| Function-based Script |               |
| Disk Usage Automation |               |
| Self-Test             |               |

---


