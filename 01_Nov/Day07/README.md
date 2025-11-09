Perfect 🚀 — welcome to **Day-7 
Today’s focus area will **bridge your shell scripting with DevOps automation** — you’ll create a **mini-project** that monitors CPU usage and integrates smoothly into a **Jenkins pipeline step**.

Let’s plan the next **2 hours** efficiently 👇

---

# 🧭 **Day-7 Practice Worksheet**

**Focus Area:** Shell
**Topic:** Mini-project — CPU Monitor + Jenkins Integration
**Goal:** Build a production-style script that checks CPU usage, logs it, and exits cleanly (to pass/fail a Jenkins stage).

---

## ⏱️ **2-Hour Study Plan**

| Time       | Topic                              | Focus                                |
| ---------- | ---------------------------------- | ------------------------------------ |
| 0–20 min   | CPU monitoring basics              | `top`, `ps`, `awk`, `grep` usage     |
| 20–45 min  | Parse CPU data in bash             | Extract percentage, process list     |
| 45–90 min  | Write & test CPU monitoring script | Logging + exit code logic            |
| 90–120 min | Jenkins integration                | Use in pipeline step + notifications |

---

## 📘 **Concept Quick Notes**

### 🔹 CPU Monitoring Commands

| Command                            | Use                          |                   |
| ---------------------------------- | ---------------------------- | ----------------- |
| `top -bn1`                         | Snapshot of CPU/memory usage |                   |
| `ps -eo pid,comm,%cpu --sort=-%cpu | head`                        | Top CPU processes |
| `grep "Cpu(s)" /proc/stat`         | Kernel CPU info (advanced)   |                   |

### 🔹 Key Tools Used

* **`awk`** → to extract specific fields
* **`date`** → timestamp logs
* **`tee`** → to write to log and show on screen
* **`exit`** → control success/failure in Jenkins

---

## 🧪 **Hands-on Practice Tasks**

---

### ✅ **Block-1: Get CPU Stats**

Run manually to see current CPU usage:

```bash
top -bn1 | grep "Cpu(s)"
```

Typical output:

```
%Cpu(s):  5.2 us,  1.0 sy,  0.0 ni, 93.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
```

Now extract the **used CPU** (100 – idle):

```bash
cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}' | cut -d. -f1)
cpu_used=$((100 - cpu_idle))
echo "CPU usage: $cpu_used%"
```

---

### ✅ **Block-2: Log Top 5 Processes**

```bash
ps -eo pid,comm,%cpu --sort=-%cpu | head -6
```

Output:

```
  PID COMMAND %CPU
 1234 java     48.3
 4567 nginx    22.1
```

You’ll log this inside your script later.

---

### ✅ **Block-3: Write the Full Script**

**File:** `cpu_monitor.sh`

```bash
#!/bin/bash
# CPU Monitor Script
set -euo pipefail

THRESHOLD=80
LOGFILE="/tmp/cpu_monitor_$(date '+%F').log"

echo "=== CPU Monitor started at $(date) ===" | tee -a "$LOGFILE"

cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}' | cut -d. -f1)
cpu_used=$((100 - cpu_idle))

echo "Current CPU usage: ${cpu_used}%" | tee -a "$LOGFILE"

echo "Top 5 CPU consuming processes:" | tee -a "$LOGFILE"
ps -eo pid,comm,%cpu --sort=-%cpu | head -6 | tee -a "$LOGFILE"

if [[ $cpu_used -gt $THRESHOLD ]]; then
    echo "[ALERT] CPU usage above threshold ($THRESHOLD%)" | tee -a "$LOGFILE"
    exit 1   # Jenkins will mark this as FAILURE
else
    echo "[OK] CPU usage under control." | tee -a "$LOGFILE"
    exit 0   # Jenkins will mark this stage as SUCCESS
fi
```

---

### ✅ **Block-4: Test Locally**

```bash
chmod +x cpu_monitor.sh
./cpu_monitor.sh
```

✅ Output sample:

```
=== CPU Monitor started at Fri Nov  7 12:15:45 UTC 2025 ===
Current CPU usage: 42%
Top 5 CPU consuming processes:
  PID COMMAND %CPU
  231 java     30.2
  567 nginx    12.3
[OK] CPU usage under control.
```

---

### ✅ **Block-5: Jenkins Integration**

Add as a **pipeline step** inside a Jenkinsfile:

```groovy
stage('CPU Health Check') {
    steps {
        sh 'bash /home/ubuntu/scripts/cpu_monitor.sh'
    }
}
```

Jenkins will automatically:

* ✅ Pass if exit code = 0
* ❌ Fail the stage if exit code ≠ 0 (e.g., high CPU)

---

### ✅ **Block-6: Optional Email Notification**

You can extend your script:

```bash
if [[ $cpu_used -gt $THRESHOLD ]]; then
    echo "CPU alert: $cpu_used%" | mail -s "High CPU Alert" admin@example.com
fi
```

---

### ✅ **Block-7: Validate with ShellCheck**

Go to [https://www.shellcheck.net/](https://www.shellcheck.net/)
Paste your script — fix warnings like:

* Quoting variables: `"${cpu_used}"`
* Safe redirection usage

---

## 🧠 **Key Interview Takeaways**

| Question                                      | Answer                                     |
| --------------------------------------------- | ------------------------------------------ |
| How to check CPU usage in Linux?              | `top`, `mpstat`, `ps`                      |
| How to parse command output in Bash?          | Use `awk`, `grep`, `cut`                   |
| How can a Jenkins stage fail on script error? | By using `exit 1`                          |
| Why use `set -euo pipefail`?                  | Stops script on error, ensures reliability |
| How to timestamp log filenames?               | `$(date '+%F')`                            |

---

## 🎯 **Day-7 Deliverables**

✔ `cpu_monitor.sh` script
✔ Log file in `/tmp`
✔ Jenkins pipeline integration
✔ Linted script (ShellCheck)
✔ Understanding of exit codes in CI/CD

---



