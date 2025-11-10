 **Day-8 focus area** is **Python basics: data types & control flow**, and you have about **2 hours**,
here’s a **structured, time-bounded practice worksheet** designed specifically for a **DevOps-oriented Python foundation** day.

---

# 🧭 **Day-8 Practice Worksheet (Duration: 2 Hours)**

**Date:** 08-Nov-2025
**Focus Area:** Python basics — variables, data types, control flow, subprocess usage
**Goal:** Build confidence with Python syntax and use it in a small DevOps-style automation script.

---

## ⏰ **Total Time: 2 Hours**

| Segment        | Topic                                     | Duration |
| -------------- | ----------------------------------------- | -------- |
| 🕐 0–20 min    | Python setup & basic syntax               | 20 min   |
| 🕑 20–45 min   | Data types: lists, tuples, dicts, strings | 25 min   |
| 🕒 45–75 min   | Control flow: `if`, `for`, `while`        | 30 min   |
| 🕓 75–105 min  | Functions & subprocess module             | 30 min   |
| 🕔 105–120 min | Final practice script (disk usage alert)  | 15 min   |

---

## 🧩 **Section-1: Basics & Data Types (0–45 min)**

### 🧠 1.1 Create a Python file

File: `day8_basics.py`

Try the following and print outputs:

```python
# Variables
name = "Vikas"
experience = 3
skills = ["Linux", "AWS", "Terraform", "Jenkins"]

print(f"Name: {name}, Experience: {experience} years")
print("Skills:", ", ".join(skills))
```

---

### 🧠 1.2 Lists & Dictionaries

```python
tools = ["Git", "Docker", "Kubernetes"]
tools.append("Terraform")
print(tools)

versions = {"Python": 3.11, "Docker": "25.0", "AWS_CLI": 2.15}
print("Tools dictionary:", versions)
print("Docker version:", versions["Docker"])
```

**Practice Questions:**

1. How to remove the first element from a list?
2. How to iterate through all keys in a dictionary?
3. How to check if a key exists in a dictionary?

---

### 🧠 1.3 Quick mini-exercise

Write code to:

* Store 5 server names in a list.
* Print only servers whose name starts with “prod”.

```python
servers = ["prod-app1", "dev-db", "prod-db2", "stage-web", "prod-redis"]
for s in servers:
    if s.startswith("prod"):
        print(s)
```

---

## ⚙️ **Section-2: Control Flow & Loops (45–75 min)**

### 🧠 2.1 `if / elif / else` practice

```python
cpu_usage = 75

if cpu_usage > 90:
    print("CRITICAL: CPU usage high")
elif cpu_usage > 70:
    print("WARNING: CPU usage moderate")
else:
    print("OK: CPU normal")
```

**Tasks:**

* Modify this script to take user input (`int(input())`) for CPU usage.
* Print the message accordingly.

---

### 🧠 2.2 `for` and `while` loops

```python
for i in range(1, 6):
    print("Iteration:", i)
```

```python
x = 1
while x <= 5:
    print("Counting:", x)
    x += 1
```

**Exercise:**
Write a loop that counts even numbers between 1 and 20 and prints the total count.

---

## 🔧 **Section-3: Functions & Subprocess (75–105 min)**

### 🧠 3.1 Define and call a function

```python
def greet(name):
    print(f"Hello, {name}! Welcome to DevOps learning.")

greet("Vikas")
```

---

### 🧠 3.2 Use `subprocess` to run Linux commands

```python
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
```

**Tasks:**

1. Try running another command, e.g., `whoami` or `date`.
2. Handle errors using `try/except`.

---

## 📊 **Section-4: Final DevOps-Style Mini-Project (105–120 min)**

### 🎯 Goal:

Write a script that:

* Runs `df -h` using `subprocess`
* Parses output
* Sends a printed **alert** if any partition is > 80 % used.

File: `disk_alert.py`

```python
import subprocess

def check_disk_usage():
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]   # skip header
    for line in lines:
        parts = line.split()
        filesystem, size, used, avail, percent, mount = parts
        usage = int(percent.replace("%", ""))
        if usage > 80:
            print(f"⚠️ ALERT: {mount} is {usage}% full")
        else:
            print(f"OK: {mount} is {usage}% used")

if __name__ == "__main__":
    check_disk_usage()
```

✅ **Optional Add-on:**
Integrate with `mailx` (from your previous script) using `subprocess.run(["mail", "-s", "Disk Alert", "vikas@example.com"], input=message)`.

---

## 🧾 **Evaluation / Self-Check**

| Skill Area          | Task                          | Status |
| ------------------- | ----------------------------- | ------ |
| ✅ Variables & Lists | Completed small exercises     | ✔️ / ❌ |
| ✅ Control Flow      | Created CPU alert logic       | ✔️ / ❌ |
| ✅ Subprocess        | Successfully ran `df -h`      | ✔️ / ❌ |
| ✅ Mini-Project      | Disk usage alert script works | ✔️ / ❌ |

---

## 📚 **References**

* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [RealPython Subprocess Guide](https://realpython.com/python-subprocess/)
* [W3Schools – Python Control Flow](https://www.w3schools.com/python/python_conditions.asp)

---



