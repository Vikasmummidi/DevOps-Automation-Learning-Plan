**Day-8 Interview Question and Answer set** focused on **Python Basics + subprocess module** — the exact blend of topics DevOps interviews use to test practical scripting and automation skills.

This is written in **interview-ready format** — concise explanations + examples you can use directly in verbal or written rounds.

---

# 🧠 **Day-8 Interview Q&A (Python Basics + Subprocess for DevOps)**

---

## ⚙️ **Section 1: Python Basics**

---

### **Q1. What are Python’s core data types?**

**Answer:**
Python supports several built-in data types:

* **Numeric** → `int`, `float`, `complex`
* **Sequence** → `list`, `tuple`, `str`
* **Mapping** → `dict`
* **Set** → `set`
* **Boolean** → `bool`

Example:

```python
x = 10             # int
tools = ["Git", "Docker", "AWS"]  # list
info = {"role": "DevOps", "exp": 3}  # dict
```

---

### **Q2. How are lists and tuples different?**

**Answer:**

| Feature  | List                  | Tuple                       |
| -------- | --------------------- | --------------------------- |
| Syntax   | `[ ]`                 | `( )`                       |
| Mutable  | ✅ Yes                 | ❌ No                        |
| Example  | `tools.append("K8s")` | Not allowed                 |
| Use Case | Changing data         | Fixed config or coordinates |

---

### **Q3. How do you iterate through a dictionary?**

**Answer:**

```python
tools = {"Python": 3.11, "Docker": "25.0"}
for key, value in tools.items():
    print(f"{key}: {value}")
```

Output:

```
Python: 3.11
Docker: 25.0
```

✅ `.items()` returns both keys and values.
`.keys()` → keys only, `.values()` → values only.

---

### **Q4. How do you check if a key exists in a dictionary?**

**Answer:**

```python
if "Docker" in tools:
    print("Docker found!")
```

or safely:

```python
version = tools.get("Terraform", "Not installed")
```

✅ `.get()` avoids `KeyError`.

---

### **Q5. What’s the difference between `==` and `is`?**

**Answer:**

* `==` compares **values**
* `is` compares **object identity (memory)**

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
```

---

### **Q6. How do you remove elements from a list?**

**Answer:**

```python
tools = ["Git", "Docker", "Kubernetes"]
tools.pop(0)     # Removes first
tools.remove("Docker")  # Removes by value
tools = tools[1:]       # Removes first via slicing
```

---

### **Q7. What is the difference between `break`, `continue`, and `pass`?**

**Answer:**

| Keyword    | Use                      |
| ---------- | ------------------------ |
| `break`    | Exit loop immediately    |
| `continue` | Skip to next iteration   |
| `pass`     | Do nothing (placeholder) |

Example:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 💡 **Section 2: String Methods (Common in Log Parsing / Automation)**

---

### **Q8. What do `.startswith()` and `.endswith()` do?**

**Answer:**
They check how a string begins or ends.

```python
if filename.endswith(".log"):
    print("Log file detected")
if server.startswith("prod"):
    print("Production server")
```

✅ Useful for filtering log files, server names, or extensions.

---

### **Q9. What does `.join()` do?**

**Answer:**
It joins elements of a list into one string:

```python
skills = ["Git", "Docker", "AWS"]
print(", ".join(skills))
```

Output:

```
Git, Docker, AWS
```

---

### **Q10. What does `.split()` do?**

**Answer:**
It splits a string into a list:

```python
line = "CPU Usage: 80%"
parts = line.split()
print(parts)
```

Output:

```
['CPU', 'Usage:', '80%']
```

✅ Used for splitting `df -h` or `ps` output lines.

---

## 🧰 **Section 3: subprocess Module**

---

### **Q11. What is the purpose of the `subprocess` module?**

**Answer:**
Used to run **system commands** from Python and capture their output.

Example:

```python
import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
```

✅ Used heavily in DevOps to integrate system utilities with Python automation.

---

### **Q12. Why do we use `capture_output=True` and `text=True`?**

**Answer:**

| Argument              | Purpose                                     |
| --------------------- | ------------------------------------------- |
| `capture_output=True` | Captures stdout & stderr                    |
| `text=True`           | Returns output as string (instead of bytes) |

Without `text=True`, you must manually decode bytes.

---

### **Q13. What’s the difference between `stdout` and `stderr`?**

**Answer:**

* `stdout`: normal command output
* `stderr`: error messages

Example:

```python
result = subprocess.run(["ls", "nofile"], capture_output=True, text=True)
print(result.stderr)
```

---

### **Q14. What does `check=True` do in `subprocess.run()`?**

**Answer:**
Raises a `CalledProcessError` if the command fails.

```python
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError:
    print("Command failed!")
```

✅ Ensures your automation script detects failed commands.

---

### **Q15. What’s the difference between `subprocess.run()` and `subprocess.Popen()`?**

**Answer:**

| Method               | Use Case                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `subprocess.run()`   | Simple, runs command and waits until complete                                      |
| `subprocess.Popen()` | More advanced, runs asynchronously or allows interaction with input/output streams |

Example:

```python
from subprocess import Popen, PIPE
proc = Popen(["grep", "root"], stdin=PIPE, stdout=PIPE)
```

---

### **Q16. How do you parse output from a system command like `df -h`?**

**Answer:**

```python
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
for line in result.stdout.strip().split("\n")[1:]:
    filesystem, size, used, avail, percent, mount = line.split()
    print(mount, percent)
```

✅ Very common in disk or memory monitoring scripts.

---

### **Q17. Why does `TypeError: a bytes-like object is required` occur in subprocess?**

**Answer:**
It happens when you pass a string to `input=` without setting `text=True`.

✅ Fix:

```python
subprocess.run(["mail", "-s", "Alert", "vikas@example.com"], input="Disk full", text=True)
```

---

### **Q18. How can you send an alert email using subprocess?**

**Answer:**

```python
message = "⚠️ Disk usage high on /"
subprocess.run(["mail", "-s", "Disk Alert", "vikas@example.com"], input=message, text=True)
```

✅ Requires `mailx` configured on the system.

---

### **Q19. How do you redirect command output to a file using subprocess?**

**Answer:**

```python
with open("output.txt", "w") as f:
    subprocess.run(["df", "-h"], stdout=f, text=True)
```

✅ Useful for logging Jenkins or cron outputs.

---

### **Q20. How do you extract the return code of a command?**

**Answer:**

```python
result = subprocess.run(["ls", "/root"], capture_output=True)
print(result.returncode)
```

✅ 0 → Success, non-zero → Failure.

---

## 📊 **Section 4: Real DevOps Contextual Questions**

---

### **Q21. Write a Python script to alert if any disk is >80% full.**

**Answer:**

```python
import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True)
for line in result.stdout.strip().split("\n")[1:]:
    parts = line.split()
    if len(parts) < 6: 
        continue
    filesystem, size, used, avail, percent, mount = parts
    usage = int(percent.strip('%'))
    if usage > 80:
        print(f"⚠️ ALERT: {mount} is {usage}% full")
```

---

### **Q22. How can you write the output of `df -h` into a CSV file?**

**Answer:**

```python
import subprocess, csv

result = subprocess.run(["df", "-h"], capture_output=True, text=True)
lines = result.stdout.strip().split("\n")

header = lines[0].split()
rows = [line.split() for line in lines[1:]]

with open("disk_usage.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
```

✅ Creates structured, Excel-friendly data.

---

### **Q23. How do you make a Python script executable on Linux?**

**Answer:**

1. Add shebang:

   ```bash
   #!/usr/bin/env python3
   ```
2. Make executable:

   ```bash
   chmod +x script.py
   ```
3. Run:

   ```bash
   ./script.py
   ```

---

### **Q24. Why use `/usr/bin/env python3` instead of `/usr/bin/python3`?**

**Answer:**

* `env` finds the correct Python interpreter dynamically from `$PATH`.
* Ensures portability across systems, containers, and virtual environments.

---

### **Q25. How can you run a Python script from cron every hour?**

**Answer:**
Add to crontab:

```
0 * * * * /usr/bin/python3 /home/ec2-user/disk_alert.py >> /tmp/disk_alert.log 2>&1
```

✅ Runs the script hourly and logs output.

---

## 🏁 **Bonus Practical Questions**

| Question                                 | Hint                                                 |
| ---------------------------------------- | ---------------------------------------------------- |
| How to read command output line by line? | `for line in result.stdout.splitlines():`            |
| How to suppress command errors?          | Add `stderr=subprocess.DEVNULL`                      |
| How to combine stdout and stderr?        | Use `stderr=subprocess.STDOUT`                       |
| How to check Python version in a script? | `sys.version` or `platform.python_version()`         |
| How to send script logs to a file?       | `logging` module or `stdout=f` in `subprocess.run()` |

---

## ✅ **Summary Table**

| Concept        | Key Function                | DevOps Use               |
| -------------- | --------------------------- | ------------------------ |
| Run commands   | `subprocess.run()`          | Automate system tasks    |
| Capture output | `capture_output=True`       | Analyze system data      |
| Handle text    | `text=True`                 | Avoid encoding errors    |
| Write CSV      | `csv.writer()`              | Export system reports    |
| Send email     | `mail` via subprocess       | Monitoring alerts        |
| Control flow   | `if`, `for`, `while`        | Build automation logic   |
| Data parsing   | `.split()`, `.startswith()` | Process logs and metrics |

---


