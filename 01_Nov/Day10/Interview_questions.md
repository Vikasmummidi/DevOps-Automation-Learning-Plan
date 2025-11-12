Perfect 👏 — let’s continue Day-10 with **interview-style Q&A** focused on the `subprocess` module, error handling, and **DevOps-grade automation tasks**.
These are exactly the kind of questions senior DevOps interviewers ask to test both your **Python scripting depth** and **system-level understanding**.

---

# 🧠 **Day-10 Interview Q&A: Python `subprocess` for DevOps**

---

## 🔹 **Section 1: Fundamentals**

### **Q1. What is the `subprocess` module in Python?**

**A:**
`subprocess` allows Python to **run system commands**, interact with shell tools, and control input/output/error streams.
It replaces older modules like `os.system`, `popen2`, and `commands` with a single, powerful API.

**Example:**

```python
import subprocess
subprocess.run(["ls", "-l"])
```

---

### **Q2. Why is `subprocess` preferred over `os.system()`?**

**A:**

| Feature        | `os.system()`          | `subprocess`                                        |
| -------------- | ---------------------- | --------------------------------------------------- |
| Output capture | ❌ No                   | ✅ Yes (`capture_output=True`)                       |
| Error handling | ❌ No                   | ✅ Yes (`check=True`, `stderr`)                      |
| Security       | ❌ Shell injection risk | ✅ Safer when `shell=False`                          |
| Control        | Limited                | Full (pipes, environment, stdin/stdout redirection) |

---

### **Q3. What does `capture_output=True` do?**

**A:**
It captures both **stdout** and **stderr** instead of printing them to the console.

**Example:**

```python
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(result.stdout)
```

---

### **Q4. What is the purpose of `text=True` (or `universal_newlines=True`)?**

**A:**
It converts the output from bytes → string.
Without it, you’d have to decode manually.

**Example:**

```python
result = subprocess.run(["echo", "DevOps"], capture_output=True)
print(result.stdout)         # b'DevOps\n'
print(result.stdout.decode()) # DevOps
```

With `text=True`, you get plain strings automatically.

---

### **Q5. How can you get the exit code of a command?**

**A:**

```python
result = subprocess.run(["ls"], capture_output=True)
print(result.returncode)
```

✅ `0` → success
❌ Non-zero → failure

---

## 🔹 **Section 2: Real-World DevOps Scenarios**

### **Q6. How do you check if a Linux service is active using Python?**

**A:**

```python
result = subprocess.run(["systemctl", "is-active", "nginx"], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ Nginx is running")
else:
    print("❌ Nginx not active")
```

---

### **Q7. How do you chain commands like `df -h | grep /dev` in Python?**

**A:**

```python
import subprocess

cmd1 = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(["grep", "/dev"], stdin=cmd1.stdout, stdout=subprocess.PIPE, text=True)
output, _ = cmd2.communicate()
print(output)
```

✅ Equivalent of shell piping but programmatic and safe.

---

### **Q8. How do you handle command errors gracefully?**

**A:**

```python
try:
    subprocess.run(["cat", "/nonexistent"], check=True)
except subprocess.CalledProcessError as e:
    print("Error:", e)
```

✅ Automatically raises an exception if return code ≠ 0.

---

### **Q9. How to handle commands that hang (e.g., long-running SSH)?**

**A:**

```python
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("Command timed out")
```

---

### **Q10. How would you redirect output to a file (like `> logfile.txt`)?**

**A:**

```python
with open("output.log", "w") as f:
    subprocess.run(["ls", "-l"], stdout=f)
```

✅ Writes command output directly to a file.

---

## 🔹 **Section 3: Advanced Concepts**

### **Q11. Explain `Popen` vs. `run`.**

| Method               | Use Case                                                        |
| -------------------- | --------------------------------------------------------------- |
| `subprocess.run()`   | Simpler, runs command and waits for it to finish                |
| `subprocess.Popen()` | More advanced: allows continuous interaction, streaming, piping |

**Example:**

```python
process = subprocess.Popen(["ping", "-c", "3", "google.com"], stdout=subprocess.PIPE)
for line in process.stdout:
    print(line.decode().strip())
```

---

### **Q12. How can you send input to a command?**

**A:**

```python
result = subprocess.run(["grep", "DevOps"], input="I love DevOps!\n", text=True, capture_output=True)
print(result.stdout)
```

✅ Feeds text to command’s stdin.

---

### **Q13. How do you run a command using the shell (e.g., `ls | grep .sh`)?**

**A:**

```python
subprocess.run("ls | grep .sh", shell=True)
```

⚠️ **Note:** Use `shell=True` only when necessary — otherwise, it’s vulnerable to shell injection.
Safer alternative:

```python
subprocess.run(["bash", "-c", "ls | grep .sh"])
```

---

### **Q14. What happens if a subprocess command fails when `check=True`?**

**A:**
It raises `subprocess.CalledProcessError`.

**Example:**

```python
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with:", e.returncode)
```

---

### **Q15. How can you suppress command output?**

**A:**

```python
subprocess.run(["apt-get", "update"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
```

✅ Equivalent to redirecting output to `/dev/null`.

---

## 🔹 **Section 4: DevOps-Specific Examples**

### **Q16. How do you clean up old Docker images via Python?**

**A:**

```python
subprocess.run(["docker", "image", "prune", "-f"], check=True)
```

---

### **Q17. Write Python code to check top 3 CPU consuming processes.**

**A:**

```python
cmd1 = subprocess.Popen(["ps", "-eo", "pid,comm,%cpu", "--sort=-%cpu"], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(["head", "-n", "4"], stdin=cmd1.stdout, stdout=subprocess.PIPE, text=True)
output, _ = cmd2.communicate()
print(output)
```

---

### **Q18. How do you integrate `subprocess` in Jenkins?**

**A:**
You can add a **Python build step**:

```groovy
stage('Health Check') {
    steps {
        sh 'python3 scripts/system_check.py'
    }
}
```

Then inside `system_check.py`:

```python
subprocess.run(["df", "-h"], check=True)
```

✅ Jenkins will mark the stage as failed if Python exits non-zero.

---

### **Q19. How do you send output from a Python subprocess to a monitoring tool like Prometheus or Grafana?**

**A:**

* Run system command with `capture_output=True`
* Parse stdout
* Push metric to a file or API endpoint

**Example:**

```python
result = subprocess.run(["top", "-bn1"], capture_output=True, text=True)
cpu_usage = 100 - float(result.stdout.split("id,")[0].split(",")[-1])
print(f"metric_cpu_usage {cpu_usage}")
```

---

### **Q20. How do you secure subprocess usage when commands include user input?**

**A:**
✅ Always pass commands as **lists**, never as concatenated strings.
❌ Unsafe:

```python
cmd = "ls " + user_input
subprocess.run(cmd, shell=True)
```

✅ Safe:

```python
subprocess.run(["ls", user_input])
```

This prevents shell-injection vulnerabilities.

---

## 🔹 **Section 5: Error & Logging Patterns**

### **Q21. How do you log all subprocess output to a file and console simultaneously?**

**A:**

```python
import subprocess, sys

proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE, text=True)
for line in proc.stdout:
    sys.stdout.write(line)
    with open("/tmp/sys_health.log", "a") as f:
        f.write(line)
```

✅ Useful for **streaming logs in real time** in pipelines.

---

### **Q22. How can you handle multiple command executions efficiently?**

**A:**
Use a helper function:

```python
def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip(), result.returncode
```

✅ Clean, reusable, production-friendly.

---

### **Q23. What is a common mistake beginners make with subprocess?**

**A:**

* Using `shell=True` unnecessarily
* Forgetting to handle errors or return codes
* Ignoring `stderr` (missing critical failure info)
* Not adding timeouts for network commands

---

### **Q24. How do you stop subprocesses gracefully?**

**A:**

```python
p = subprocess.Popen(["sleep", "60"])
p.terminate()
```

Or force kill:

```python
p.kill()
```

---

### **Q25. How would you combine subprocess with Python’s logging module?**

**A:**

```python
import logging, subprocess

logging.basicConfig(filename='syscheck.log', level=logging.INFO)
result = subprocess.run(["uptime"], capture_output=True, text=True)
logging.info(result.stdout)
```

✅ Combines command output into centralized logs — real DevOps best practice.

---

## 🧠 **Summary Table**

| Concept               | Example                                   |
| --------------------- | ----------------------------------------- |
| Run command           | `subprocess.run(["ls"])`                  |
| Capture output        | `capture_output=True`                     |
| Check errors          | `check=True`                              |
| Handle timeouts       | `timeout=5`                               |
| Chain commands        | `Popen` + `PIPE`                          |
| Redirect output       | `stdout=DEVNULL`                          |
| Safe vs. unsafe input | Always pass list args, avoid `shell=True` |

---

## 🎯 **DevOps Takeaway**

`subprocess` is your **bridge between Python and Linux**, giving you:

* Fine-grained control of shell commands
* Error-safe automation
* Jenkins-ready scripting
* A foundation for writing production-ready monitoring, deployment, and cleanup tools.

---


