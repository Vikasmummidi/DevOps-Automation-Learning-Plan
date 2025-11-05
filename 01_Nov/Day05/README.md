💥 **Day-5 — Shell Scripting for DevOps**
**Focus Area:** Functions, Error Handling, Logging, Script Structure
**Goal:** Write production-style scripts like in CI/CD pipelines

---

## 🎯 **Learning Goals**

By end of Day-5 you will be able to:

✅ Write **functions** in bash
✅ Handle **errors & exit codes** like CI pipelines
✅ Add **logging** (info, warn, error)
✅ Understand **script structure & best practices**
✅ Use `trap` to handle cleanup on exit
✅ Build a **real DevOps automation script**

---

## ⏱️ **2-Hour Study & Practice Plan**

| Time       | Topic             | Focus                              |   |                  |
| ---------- | ----------------- | ---------------------------------- | - | ---------------- |
| 00-15 min  | Script structure  | shebang, comments, usage function  |   |                  |
| 15-35 min  | Functions in Bash | function syntax, return values     |   |                  |
| 35-60 min  | Error handling    | `set -e`, traps, `                 |   | `, safe patterns |
| 60-80 min  | Logging           | `logger`, custom log levels        |   |                  |
| 80-120 min | Mini-Project      | Service health check + log + alert |   |                  |

---

## 📘 **Mini-Theory Before Practice**

### **Functions**

```bash
my_func() {
  echo "Hello from function"
}
my_func
```

With parameters:

```bash
greet() {
  echo "Hello $1"
}
greet "Vikas"
```

---

### **Error Handling Best Practices**

```bash
set -euo pipefail
# -e exit on error
# -u unset variable error
# -o pipefail fail pipeline on error
```

Safe execution:

```bash
command || { echo "Command failed"; exit 1; }
```

---

### **Traps (clean exit)**

```bash
trap "echo 'Script interrupted. Cleaning up...'" SIGINT EXIT
```

---

### **Logging**

```bash
log_info()  { echo "[INFO]  $*"; }
log_warn()  { echo "[WARN]  $*"; }
log_error() { echo "[ERROR] $*" >&2; }
```

---

## 📝 **Practice Worksheet**

### ✅ **Block-1: Script Template**

Create `template.sh`

```bash
#!/bin/bash
set -euo pipefail

usage() {
  echo "Usage: $0 <arg>"
  exit 1
}

[[ $# -lt 1 ]] && usage
echo "Arg: $1"
```

---

### ✅ **Block-2: Functions**

```bash
sum() {
  echo $(( $1 + $2 ))
}
sum 4 6
```

---

### ✅ **Block-3: Trap Demo**

```bash
trap "echo 'Cleaning up before exit 🚀'" EXIT
echo "Running..."
sleep 2
```

---

### ✅ **Block-4 DevOps Mini-Project**

### 🧩 Script: **service_monitor.sh**

> Monitors service + logs + exit on failure

```bash
#!/bin/bash
set -euo pipefail

service=$1
logfile="service.log"

log() { echo "$(date) | $1" | tee -a "$logfile"; }

check_service() {
  if systemctl is-active --quiet "$service"; then
    log "$service running ✅"
  else
    log "$service down ❌"
    exit 1
  fi
}

trap "log 'Script exited.'" EXIT
check_service
```

Run:

```bash
chmod +x service_monitor.sh
./service_monitor.sh nginx
```

---

## 🧠 **Interview Focus for Day-5**

Questions you must master:

* Difference between `return` vs `exit` in bash?
* Why use `set -euo pipefail`?
* How to catch signals (`trap`)?
* How to log errors properly in scripts?
* What is `PIPESTATUS` in bash pipelines?

---

## 🎁 Deliverables by end of Day-5

✔️ 1 reusable script template
✔️ Logging functions library
✔️ Service monitoring script
✔️ Notes on traps & error handling
✔️ ShellCheck validation

---

