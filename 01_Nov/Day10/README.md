welcome to **Day-10 (10-Nov-2025)**!
Now you’re stepping into a **core DevOps skill**: running system commands safely and efficiently using **Python’s `subprocess` module**.

This topic connects directly to your shell scripting background — but now from a **Python automation** and **CI/CD orchestration** perspective.

Let’s make this **a 2-hour, hands-on DevOps-focused worksheet** — with concepts, real-world examples, and exercises you can practice today.

---

# 🧭 **Day-10 Practice Worksheet**

**Focus Area:** Python for DevOps
**Topic:** Running System Commands — `subprocess`
**Goal:** Automate shell tasks, capture outputs, handle errors programmatically.

---

## ⏱️ **2-Hour Study Plan**

| Time       | Topic                           | Focus                                          |
| ---------- | ------------------------------- | ---------------------------------------------- |
| 0–20 min   | Subprocess fundamentals         | Run commands like `ls`, `df`, `docker ps`      |
| 20–50 min  | Capturing output & return codes | stdout, stderr, exit codes                     |
| 50–90 min  | Real-world DevOps use cases     | Monitoring, log cleanup, deployment            |
| 90–120 min | Error handling & best practices | Exceptions, timeouts, secure command execution |

---

## 📘 **Concept Quick Notes**

### 🔹 Why use `subprocess`?

In DevOps, you often need to:

* Run Linux commands (like `ls`, `df -h`, `kubectl get pods`)
* Integrate shell tools in CI/CD Python scripts
* Capture command outputs
* Handle errors gracefully

Instead of:

```python
os.system("ls -l")
```

You should use:

```python
subprocess.run(["ls", "-l"])
```

✅ safer, modern, and gives you full control.

---

## 🧩 **1️⃣ Basics — Running a Command**

### Example

```python
import subprocess

subprocess.run(["ls", "-l"])
```

**Explanation:**

* Runs `ls -l`
* Waits for completion
* Prints output directly to console

---

### DevOps Example

List all `.log` files under `/var/log`:

```python
subprocess.run(["find", "/var/log", "-name", "*.log"])
```

---

## 🧩 **2️⃣ Capture Output**

You often need the **output** in your script (for parsing, alerting, etc.)

### Example

```python
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(result.stdout)
```

| Attribute    | Description             |
| ------------ | ----------------------- |
| `stdout`     | Standard output         |
| `stderr`     | Error output            |
| `returncode` | Exit code (0 = success) |

---

### DevOps Example — Check Disk Space

```python
import subprocess

result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
usage = result.stdout.splitlines()[1].split()[4]  # e.g. '72%'
print(f"Disk Usage: {usage}")
```

✅ Extracts only the percentage of root partition usage.

---

## 🧩 **3️⃣ Capture and Handle Errors**

### Example:

```python
result = subprocess.run(["ls", "/nonexistent"], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Exit Code:", result.returncode)
```

**Output:**

```
STDOUT:
STDERR: ls: cannot access '/nonexistent': No such file or directory
Exit Code: 2
```

---

### DevOps Example — Check if a service is running

```python
result = subprocess.run(["systemctl", "is-active", "nginx"], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ NGINX is running")
else:
    print("❌ NGINX not active:", result.stdout.strip())
```

---

## 🧩 **4️⃣ Raising Exceptions Automatically**

To make Python fail fast (like `set -e` in shell):

```python
subprocess.run(["false"], check=True)
```

Output:

```
subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.
```

✅ Use `check=True` in production scripts — ensures failed commands raise exceptions immediately.

---

## 🧩 **5️⃣ Combining Commands with Pipes**

### Example

Equivalent of:

```bash
df -h | grep /dev
```

In Python:

```python
cmd1 = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(["grep", "/dev"], stdin=cmd1.stdout, stdout=subprocess.PIPE, text=True)
output, _ = cmd2.communicate()
print(output)
```

✅ Use `Popen` when chaining or streaming multiple commands.

---

### DevOps Example — Find Top 3 CPU Processes

```python
cmd1 = subprocess.Popen(["ps", "-eo", "pid,comm,%cpu", "--sort=-%cpu"], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(["head", "-n", "4"], stdin=cmd1.stdout, stdout=subprocess.PIPE, text=True)
output, _ = cmd2.communicate()
print(output)
```

---

## 🧩 **6️⃣ Timeout Handling**

To prevent hanging scripts:

```python
try:
    subprocess.run(["sleep", "5"], timeout=2)
except subprocess.TimeoutExpired:
    print("Command timed out")
```

✅ Great for network or long-running deployment steps.

---

## 🧩 **7️⃣ Handling Both Success & Failure Gracefully**

```python
result = subprocess.run(["ls", "/tmp"], capture_output=True, text=True)
if result.returncode == 0:
    print("Command succeeded")
else:
    print(f"Command failed with: {result.stderr}")
```

---

## 🧩 **8️⃣ Real-World DevOps Scenarios**

| Use Case                    | Example                                                                   |
| --------------------------- | ------------------------------------------------------------------------- |
| Check Kubernetes pod status | `subprocess.run(["kubectl", "get", "pods"])`                              |
| Trigger Jenkins job via CLI | `subprocess.run(["java", "-jar", "jenkins-cli.jar", "build", "jobname"])` |
| Clean up Docker containers  | `subprocess.run(["docker", "system", "prune", "-f"])`                     |
| Monitor CPU or disk         | Use `top`, `df`, `free` commands from Python                              |
| Collect logs                | `subprocess.run(["grep", "ERROR", "/var/log/syslog"])`                    |

---

## 🧩 **9️⃣ Writing a Mini Project: System Health Check Script**

### 🧰 `health_check.py`

```python
#!/usr/bin/env python3
import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.returncode

def check_disk():
    output, _ = run_cmd(["df", "-h", "/"])
    print("=== Disk Info ===\n", output)

def check_cpu():
    output, _ = run_cmd(["top", "-bn1"])
    print("=== CPU Info ===\n", output.splitlines()[2])

def check_service(service):
    _, code = run_cmd(["systemctl", "is-active", service])
    print(f"{service}: {'Running ✅' if code == 0 else 'Not Running ❌'}")

if __name__ == "__main__":
    check_disk()
    check_cpu()
    check_service("nginx")
```

✅ Integrates `subprocess` with DevOps monitoring logic.

---

## 🧩 **10️⃣ Validate with ShellCheck Equivalent**

While ShellCheck validates shell scripts, Python provides **linting & formatting tools** like:

```bash
pylint health_check.py
black health_check.py
```

to ensure your script follows best practices.

---

## 🧠 **Key Takeaways**

| Concept               | Description                       | Example                             |
| --------------------- | --------------------------------- | ----------------------------------- |
| `subprocess.run()`    | Run commands safely               | `subprocess.run(["ls", "-l"])`      |
| `capture_output=True` | Capture stdout & stderr           | `result.stdout`                     |
| `check=True`          | Raise error on non-zero exit      | `subprocess.run([...], check=True)` |
| `timeout`             | Prevent hangs                     | `timeout=5`                         |
| `Popen()`             | Use for pipes or background tasks | `Popen(["df", "-h"], stdout=PIPE)`  |

---

## ⚙️ **DevOps Reality Check**

| Problem                  | Traditional Way            | Pythonic Way                                 |
| ------------------------ | -------------------------- | -------------------------------------------- |
| Run command & log output | `bash script.sh > log.txt` | `subprocess.run([...], capture_output=True)` |
| Parse metrics            | `grep`, `awk`              | Split strings and parse stdout               |
| Handle errors            | `set -e`                   | `check=True`, exceptions                     |
| Integrate in CI/CD       | Shell script steps         | Python orchestration layer                   |

---

## 🧩 **Bonus Challenge**

Write a Python script that:

1. Checks CPU usage (via `top -bn1`)
2. If usage > 80%, prints an alert
3. Otherwise, logs status to `/tmp/health_report.log`
4. Use `subprocess` with `check=True` and `capture_output=True`

---



