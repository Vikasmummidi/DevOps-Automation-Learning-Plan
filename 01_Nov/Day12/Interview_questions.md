
---

# ✅ **Day-12 Interview Q&A: Python Error Handling & Debugging**

---

# 🔹 **1. What is an exception in Python?**

**Answer:**
An exception is an event that occurs during program execution that disrupts the normal flow. Python raises exceptions when something goes wrong (e.g., `NameError`, `ValueError`, `IOError`). Exceptions can be handled using `try–except`.

---

# 🔹 **2. Difference between syntax error and exception?**

**Answer:**

* **Syntax Error** → occurs at compile/parse time. Code cannot run.
  Example: missing colon in loop.
* **Exception** → occurs at runtime while executing valid Python code.
  Example: division by zero.

---

# 🔹 **3. Explain try–except–else–finally with a simple example.**

**Answer:**

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception occurred")
finally:
    print("Always executed")
```

* `try` → code that may raise an exception
* `except` → handles specific exception
* `else` → runs only if no exception
* `finally` → always executes (closing files, connections)

---

# 🔹 **4. What was wrong in this code?**

```python
except 'ValueError':
```

**Answer:**
You cannot catch a string. Python expects an **Exception class**, not a string.

✔ Correct:

```python
except ValueError:
```

---

# 🔹 **5. What does this error mean?**

```
NameError: name 'risky_operation' is not defined
```

**Answer:**
Python cannot find the function or variable. It is either misspelled, not imported, or declared later in the script.

---

# 🔹 **6. How do you catch multiple exceptions?**

**Answer:**

```python
try:
    risky_operation()
except (ValueError, TypeError, KeyError) as e:
    print("Error:", e)
```

---

# 🔹 **7. How do you create a custom exception?**

**Answer:**

```python
class DiskFullError(Exception):
    pass

raise DiskFullError("Disk usage crossed threshold")
```

---

# 🔹 **8. What is the purpose of the `finally` block?**

**Answer:**
It executes **every time**, whether an exception occurs or not.

Common DevOps usage:

* close SSH connections
* close file handles
* delete temp files
* kill subprocesses

---

# 🔹 **9. What is the difference between raising and handling an exception?**

**Handling:**
You catch the exception using `try–except`.

**Raising:**
You intentionally throw an exception using `raise`.

---

# 🔹 **10. How do you log exceptions properly?**

**Answer:**
Using the `logging` module:

```python
import logging

try:
    risky_operation()
except Exception as e:
    logging.exception("Something went wrong")
```

This logs stack trace + message.

---

# 🔹 **11. What does this line do?**

```python
except Exception as e:
```

**Answer:**

* Catches **all built-in exceptions** except `SystemExit`, `KeyboardInterrupt`.
* Stores the exception object in variable `e`.

⚠ In production, prefer catching specific exceptions.

---

# 🔹 **12. How do you re-raise an exception?**

**Answer:**

```python
try:
    risky_operation()
except Exception:
    print("Logging error")
    raise
```

Useful when you want to log but still let the program fail.

---

# 🔹 **13. What is traceback in Python?**

**Answer:**
A traceback is the detailed error report that shows:

* file name
* line number
* function
* error message

It helps in debugging.

---

# 🔹 **14. What is `assert` used for?**

**Answer:**
`assert` is used for internal sanity checks.

```python
assert x > 0, "x must be positive"
```

If the condition is False → raises `AssertionError`.

---

# 🔹 **15. How do you handle file-related errors safely?**

**Answer using context manager:**

```python
try:
    with open("data.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
```

---

# 🔹 **16. How would you debug a Python script in production?**

**Answer:**

* Add logging instead of print
* Use log levels (`INFO`, `ERROR`, `DEBUG`)
* Use try–except around risky areas
* Use `pdb` for local debugging
* Use structured logs (JSON) for pipelines

---

# 🔹 **17. What is the purpose of `pdb`?**

**Answer:**
`pdb` = Python Debugger.

Example:

```python
import pdb; pdb.set_trace()
```

Lets you step through code line by line.

---

# 🔹 **18. Why should we avoid bare `except:`?**

**Answer:**
Because it catches **everything**, including:

* `KeyboardInterrupt`
* `SystemExit`

It hides bugs and makes debugging difficult.

Better:

```python
except Exception:
    pass
```

---

# 🔹 **19. What happens if exception is not caught?**

**Answer:**
The program terminates and Python prints a traceback.

---

# 🔹 **20. How do you catch only one exception and ignore others?**

```python
try:
    int("abc")
except ValueError:
    print("Only ValueError caught")
```

---

# 🔥 Bonus DevOps Scenario Questions

---

### **21. How do you handle subprocess failures in Python?**

```python
import subprocess

try:
    subprocess.run(["ls", "/root"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed:", e)
```

---

### **22. Your Python script reads logs but sometimes fails due to missing file. How do you handle it?**

Use `FileNotFoundError`.

---

### **23. How do you write a retry mechanism?**

```python
import time

for i in range(3):
    try:
        connect_to_server()
        break
    except ConnectionError:
        time.sleep(2)
```

---


