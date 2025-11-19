

# 📝 **Day-12 Practice Worksheet**

**Focus Area:** Python
**Topic:** Error Handling & Logging
**Duration:** ~2 hours
**Goal:** Build robust, production-ready Python scripts using `try/except`, structured exception handling, and the `logging` module.

---

# 🧭 **1. Topic Overview**

### ✅ Error handling in Python

* `try / except`
* `try / except / else`
* `try / except / finally`
* Catching specific vs generic exceptions
* Raising exceptions (`raise`)
* Custom exceptions

### ✅ Logging

* `logging.basicConfig()`
* Logger levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
* Logging to file
* Logging formatting
* Rotating logs (optional advanced)

---

# 📘 **2. Quick Reference Cheatsheet**

### **Error Handling Syntax**

```python
try:
    risky_operation()
except ValueError:
    print("Value error occurred")
except Exception as e:
    print("General error:", e)
else:
    print("Runs only if no exception")
finally:
    print("Always executed")
```

### **Basic Logging Setup**

```python
import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

---

# 🧪 **3. Practice Tasks**

## **Task 1 — Simple Error Handling**

Write a Python script:

```
task1.py
```

### Requirements:

✔ Accept two numbers from user
✔ Handle the case where input is not a number
✔ Handle division by zero
✔ Print friendly output

### Example:

```
Enter numerator: a
Invalid number. Please enter a numeric value.
```

---

## **Task 2 — File Handling with Exceptions**

Create a script:

```
task2.py
```

### Requirements:

* Try opening a file called `data.txt`
* If the file does not exist, catch `FileNotFoundError`
* If contents cannot be parsed, catch `ValueError`
* Always print `"Cleaning up..."` using `finally`

---

## **Task 3 — Logging Basic Script Execution**

Create:

```
task3_logging.py
```

### Requirements:

* Write logs to `run.log`
* Configure logging level to `INFO`
* Log:

  * Script start
  * Each step of execution
  * Errors using `logging.error()`
  * Script completion

Example format:

```
2025-02-15 12:45:33 - INFO - Script started
2025-02-15 12:45:34 - ERROR - Failed to read file
```

---

## **Task 4 — Function With Logging + Error Handling**

Create:

```
task4_function_logging.py
```

### Requirements:

* Function: `get_user_age()`
* Valid age: integer between 1 and 120
* Errors:

  * ValueError → invalid integer
  * Custom exception → out-of-range age
* Log all errors into a file
* Log success when valid age is returned

---

## **Task 5 — Logging + Try/Except for API Call Simulation**

Create:

```
task5_api_simulation.py
```

### Requirements:

* Simulate API call using `subprocess.run(["echo", "API OK"])`
* If subprocess fails → log `ERROR`
* If output received → log `INFO`
* Wrap everything inside `try/except/finally`

---

# 🔥 **4. Advanced Practice Challenges (Optional)**

### ⭐ Challenge 1 — Log Rotation

Implement rotating logs:

```python
from logging.handlers import RotatingFileHandler
```

Rotate after 1MB, keep 3 backups.

---

### ⭐ Challenge 2 — Write Your Own Custom Exception

Example:

```python
class InvalidStatus(Exception):
    pass
```

Raise it if status != "Running".

---

### ⭐ Challenge 3 — Logging + JSON Parsing

* Load a JSON file
* If missing fields → log error
* Parse safely
* Use `logging.exception()` to print traceback

---

# 🧩 **5. Mini Project (End of Day-12)**

Build:

```
monitor_disk.py
```

### Requirements:

✔ Use `subprocess` to run:

```
df -h / | tail -1 | awk '{print $5}' | sed 's/%//'
```

✔ If disk usage > 80%:

* Log WARNING
* Write timestamp + usage into `alerts.log`

✔ Everything wrapped with try/except
✔ Use logging with INFO/WARNING/ERROR
✔ Should NEVER crash

This is exactly how DevOps engineers write monitoring scripts.

---

# 📚 **6. Resources**

### 🔗 Official Python Docs

[https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html)
[https://docs.python.org/3/howto/logging.html](https://docs.python.org/3/howto/logging.html)

### 🔗 RealPython (best logging guide)

[https://realpython.com/python-logging/](https://realpython.com/python-logging/)

### 🔗 Logging Cookbook (advanced)

[https://docs.python.org/3/howto/logging-cookbook.html](https://docs.python.org/3/howto/logging-cookbook.html)

---

