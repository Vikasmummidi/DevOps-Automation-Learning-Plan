
---

# 🧭 **Day-3 Shell Practice Worksheet**

**Focus:** Redirection, Pipes, Exit Codes
**Goal:** Learn to chain commands and handle success/failure for automation

---

## ⏱ **Block-1 (0–30 min): Redirection Basics**

### 1️⃣ Output Redirection

```bash
echo "Hello DevOps" > output.txt      # writes (overwrites) output.txt
cat output.txt

echo "Appending line" >> output.txt    # appends
cat output.txt
```

✅ *Notice the second line is appended, not replaced.*

---

### 2️⃣ Input Redirection

```bash
sort < output.txt
```

✅ *Reads content from file instead of keyboard input.*

---

### 3️⃣ Error Redirection

```bash
ls /not/here 2> error.log
cat error.log
```

✅ *The error message gets stored in error.log, not shown on screen.*

---

### 4️⃣ Redirect both stdout + stderr

```bash
ls /root /not/here &> all_output.log
cat all_output.log
```

✅ *Both success and error messages go to the same file.*

---

## ⏱ **Block-2 (30–60 min): Pipes and Chaining**

### 1️⃣ Using a Pipe

```bash
ps aux | head -5
```

✅ *Passes `ps` output into `head`, showing only top 5 lines.*

---

### 2️⃣ Combine Filters

```bash
ps aux | grep bash | awk '{print $2, $11}'
```

✅ *Finds bash processes and prints PID + Command.*

---

### 3️⃣ Use `tee` for Logging

```bash
echo "Disk Usage Report:" | tee report.txt
df -h | tee -a report.txt
```

✅ *Writes to screen **and** file simultaneously.*

---

### 4️⃣ Command Chaining

```bash
mkdir logs; cd logs
pwd && echo "Inside logs directory"
cd /fakepath || echo "Failed to enter directory"
```

✅ *`;` runs sequentially, `&&` runs next only if success, `||` only if fail.*

---

## ⏱ **Block-3 (60–90 min): Exit Codes**

### 1️⃣ Check Exit Code

```bash
ls /etc > /dev/null
echo $?   # should print 0

ls /no/such/path > /dev/null
echo $?   # should print non-zero
```

---

### 2️⃣ Conditional Using Exit Code

```bash
ls /etc > /dev/null
if [ $? -eq 0 ]; then
  echo "Command succeeded"
else
  echo "Command failed"
fi
```

---

### 3️⃣ Using `set -e`

```bash
set -e
echo "Starting..."
ls /fake/path   # script stops here on error
echo "This will not run"
```

✅ *Good for automation: stops when something fails.*

---

## ⏱ **Block-4 (90–120 min): Mini Project + ShellCheck**

### 🧩 Script: `top_cpu.sh`

```bash
#!/bin/bash
# top_cpu.sh
# Logs top 5 CPU-consuming processes

LOGFILE="cpu_top5.log"
echo "Collecting CPU info..."

ps -eo pid,comm,%cpu --sort=-%cpu | head -6 > "$LOGFILE"

if [ $? -eq 0 ]; then
  echo "Top 5 CPU-consuming processes saved to $LOGFILE"
else
  echo "Failed to collect data" >&2
fi
```

### 🧠 Run it

```bash
chmod +x top_cpu.sh
./top_cpu.sh
cat cpu_top5.log
```

### 🧩 Lint it (ShellCheck)

Go to 👉 [https://www.shellcheck.net](https://www.shellcheck.net), paste your script, and fix warnings.

---

## ✅ **Wrap-up Summary**

| Concept            | Symbol     | Example              |     |                         |
| ------------------ | ---------- | -------------------- | --- | ----------------------- |
| Output redirection | `>` `>>`   | `echo hi > file.txt` |     |                         |
| Input redirection  | `<`        | `sort < file.txt`    |     |                         |
| Error redirection  | `2>` `&>`  | `cmd 2> err.log`     |     |                         |
| Pipe               | `          | `                    | `ls | grep txt`               |
| Chain              | `;` `&&` ` |                      | `   | `mkdir logs && cd logs` |
| Exit code          | `$?`       | `echo $?`            |     |                         |

---


