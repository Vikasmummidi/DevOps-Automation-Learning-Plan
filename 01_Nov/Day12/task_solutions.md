---

# ✅ **Task 1 — Simple Error Handling (Division Calculator)**

**File: `task1.py`**

```python
def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

num1 = get_number("Enter numerator: ")
num2 = get_number("Enter denominator: ")

if num1 is not None and num2 is not None:
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
```

---

# ✅ **Task 2 — File Handling With Exceptions**

**File: `task2.py`**

```python
try:
    with open("data.txt") as f:
        content = f.read()

    number = int(content)  # may raise ValueError
    print("Number in file:", number)

except FileNotFoundError:
    print("Error: data.txt not found.")

except ValueError:
    print("Error: File does not contain a valid integer.")

finally:
    print("Cleaning up... (this always runs)")
```

---

# 🟦 **Task 3 — Logging Basic Script Execution**

**File: `task3_logging.py`**

```python
import logging

logging.basicConfig(
    filename="run.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")

try:
    # Example risky section
    with open("sample.txt") as f:
        data = f.read()
    logging.info("File read successfully")

except Exception as e:
    logging.error(f"Error reading file: {e}")

finally:
    logging.info("Script completed")
```

---

# 🟩 **Task 4 — Function With Logging + Custom Exceptions**

**File: `task4_function_logging.py`**

```python
import logging

logging.basicConfig(
    filename="age.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class AgeOutOfRange(Exception):
    pass

def get_user_age():
    try:
        age = int(input("Enter your age: "))
        if not 1 <= age <= 120:
            raise AgeOutOfRange("Age must be between 1 and 120")

        logging.info(f"Valid age entered: {age}")
        return age

    except ValueError:
        logging.error("Invalid number entered")
    except AgeOutOfRange as e:
        logging.error(str(e))

age = get_user_age()
print("Age processed:", age)
```

---

# 🟧 **Task 5 — Logging + Try/Except for API Simulation**

**File: `task5_api_simulation.py`**

```python
import subprocess
import logging

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("API Simulation started")

    out = subprocess.run(
        ["echo", "API OK"],
        capture_output=True,
        text=True
    )

    if out.returncode != 0:
        logging.error("API call failed")
    else:
        logging.info(f"API Response: {out.stdout.strip()}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")

finally:
    logging.info("API Simulation completed")
```

---

# 🔥 **Mini Project — Disk Monitoring Script**

**File: `monitor_disk.py`**

```python
import subprocess
import logging

logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_disk_usage():
    try:
        cmd = "df -h / | tail -1 | awk '{print $5}' | sed 's/%//'"
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if out.returncode != 0:
            logging.error("Failed to execute df command")
            return None

        return int(out.stdout.strip())

    except Exception as e:
        logging.error(f"Error parsing disk usage: {e}")
        return None

usage = get_disk_usage()

if usage is not None:
    logging.info(f"Disk usage: {usage}%")

    if usage > 80:
        logging.warning(f"High disk usage detected: {usage}%")
else:
    logging.error("Disk usage could not be determined")
```

---


