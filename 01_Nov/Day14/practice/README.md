
---

# 📝 **Day-14 Practice Worksheet**

### **Focus Area:** Python

### **Topic:** *Mini Project – Disk Usage Checker & JSON Parser*

### **Goal:**

Combine file-system checks, JSON parsing, and optionally subprocess execution to build a practical utility.

---

## 📘 **1. Overview**

Today you will build a mini-project that:

✔ Checks disk usage using `shutil` or `subprocess`
✔ Parses JSON configuration files
✔ Sends alerts or prints warnings based on thresholds
✔ Practices exception handling & modular Python code

This is extremely useful for DevOps tasks like monitoring, health checks, and automation.

---

# 📚 **2. Resources**

* Python official tutorial
  [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
* RealPython on subprocess
  [https://realpython.com/python-subprocess/](https://realpython.com/python-subprocess/)
* Python getting started
  [https://www.python.org/about/gettingstarted/](https://www.python.org/about/gettingstarted/)

---

# 🧠 **3. Concepts to Know**

Before writing the project, ensure you understand:

### **File & Disk Handling**

* `shutil.disk_usage(path)`
* `os.path.exists(path)`
* `subprocess.run()`

### **JSON Handling**

* `json.load()`
* `json.loads()`
* Handling malformed JSON errors

### **Error Handling**

* `try-except-finally`
* Custom exceptions
* Returning error codes (optional)

---

# 🧪 **4. Practice Tasks**

## **Task 1: Write a disk usage function**

Write a Python function:

```python
def check_disk_usage(path):
    """
    Returns disk usage as % used for the given path.
    """
```

Expected output:

```
Path: /  | Used: 63.2%
```

---

## **Task 2: Read a JSON config file**

Create a JSON config file `config.json`:

```json
{
  "path": "/",
  "threshold": 70,
  "email_alert": false
}
```

Write Python code that:

* Loads the file
* Validates keys exist
* Fails gracefully if file is missing or corrupted

---

## **Task 3: Integrate JSON + disk check**

Combine them:

✔ Read path & threshold from JSON
✔ Use your disk usage function
✔ Print:

```
Disk usage is normal.
```

OR

```
WARNING: Disk usage exceeded threshold! (78% > 70%)
```

---

## **Task 4 (Optional Stretch): Use subprocess**

Use:

```python
subprocess.run(["df", "-h"])
```

Then extract and print only the `/` line using Python string methods.

---

## **Task 5: Write a complete script**

Create `disk_monitor.py`:

### Minimum requirements:

* Read JSON
* Validate keys
* Calculate disk usage
* Compare with threshold
* Print final result

### Bonus:

* Log output to a file `monitor.log`
* Trigger an email using `mail` command
* Wrap everything inside `if __name__ == "__main__":`

---

# 🧩 **5. Challenge Problems**

### **Challenge 1:**

Write a function that checks multiple paths from JSON:

```json
{
  "paths": [
    { "path": "/", "threshold": 70 },
    { "path": "/var", "threshold": 80 }
  ]
}
```

Output sample:

```
/: OK (58% < 70%)
/var: ALERT (82% > 80%)
```

---

### **Challenge 2:**

Add exception logging.
If the JSON fails to load due to invalid format, log:

```
ERROR: Invalid JSON configuration - Expecting ',' delimiter
```

---

### **Challenge 3:**

Convert the final result into a JSON report:

```json
{
  "status": "ALERT",
  "current_usage": 82,
  "threshold": 70
}
```

Save it to `report.json`.

---

# 🎯 **6. Quick Interview Questions (Day-14 Focus)**

1. What is the difference between `json.load()` and `json.loads()`?
2. How do you check if a file exists in Python?
3. What does `shutil.disk_usage()` return?
4. How do you handle corrupted JSON input?
5. Why is `subprocess.run()` preferred over `os.system()`?
6. Can you parse JSON without storing it in a file? How?
7. How to catch multiple exceptions in Python?
8. What is `__name__ == "__main__"` used for?
9. Why is JSON widely used in DevOps tooling?
10. What are common pitfalls when parsing external JSON files?

---

# 🏁 **7. Submission Checklist**

Before closing Day-14, make sure:

✔ You wrote `disk_monitor.py`
✔ You created a valid + invalid `config.json` to test
✔ You tested threshold alerts
✔ You practiced custom exceptions
✔ You can explain JSON parsing in interviews

---



