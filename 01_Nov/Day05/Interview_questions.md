

> **Bash Functions, Error Handling, Logging, Traps, Script Design**

These are **DevOps / SRE-focused** and common in interviews (AWS, SRE, DevOps engineer, Production Ops).

---

# ✅ **Day-5: Bash Interview Q&A**

---

## 🧾 **Functions in Bash**

### **Q1. How do you define a function in Bash?**

**A:**

```bash
my_func() {
  echo "Hello"
}
my_func
```

Alternate syntax:

```bash
function my_func { ... }
```

---

### **Q2. How do you pass arguments to functions?**

```bash
add() {
  echo $(( $1 + $2 ))
}
add 10 20
```

---

### **Q3. `return` vs `exit` in Bash?**

| Keyword  | Meaning                                       |
| -------- | --------------------------------------------- |
| `return` | End function & return exit code **to script** |
| `exit`   | Terminates entire script                      |

---

### **Q4. How do you return values from a function?**

Bash functions **do not return strings**, only exit codes.

Use `echo` to output values:

```bash
greet() { echo "Hello"; }
msg=$(greet)
```

---

## ⚠️ **Error Handling / Safety**

### **Q5. What does `set -euo pipefail` mean?**

| Flag          | Meaning                         |
| ------------- | ------------------------------- |
| `-e`          | exit if command fails           |
| `-u`          | error on undefined variable     |
| `-o pipefail` | fail pipeline if any step fails |

Used in **production scripts & CI/CD pipelines**.

---

### **Q6. Why is `set -e` dangerous in loops sometimes?**

If any loop command fails → entire script exits.
Solution: use `|| true` inside loops safely.

---

### **Q7. How do you check command exit status?**

```bash
if command; then
  echo "Success"
else
  echo "Failed"
fi
```

Or explicitly:

```bash
command
if [[ $? -ne 0 ]]; then ...
```

---

### **Q8. How do you prevent a script from exiting on error?**

```bash
command || echo "Command failed but continuing"
```

---

## 🧯 **Traps & Cleanup**

### **Q9. What is `trap` used for?**

To **run code on interrupt or exit** — cleanup logs, kill background jobs, rollback deployments.

Example:

```bash
trap "echo cleanup; rm /tmp/lock" EXIT
```

---

### **Q10. How do you trap Ctrl+C (SIGINT)?**

```bash
trap "echo Interrupted; exit" SIGINT
```

---

### **Q11. When do you use `trap ERR`?**

To catch **errors inside scripts** and take action (alert/rollback).

```bash
trap "echo error" ERR
```

---

### **Q12. Common signals in Linux scripting**

| Signal  | Meaning                  |
| ------- | ------------------------ |
| SIGINT  | Ctrl+C interrupt         |
| SIGTERM | Graceful stop request    |
| EXIT    | Script termination event |
| ERR     | Error occurred           |

---

## 🧾 **Logging**

### **Q13. How do you log with timestamps in Bash?**

```bash
log() { echo "$(date) | $1" >> app.log; }
log "Service started"
```

---

### **Q14. Log levels example**

```bash
info()  { echo "[INFO] $*"; }
error() { echo "[ERROR] $*" >&2; }
```

---

### **Q15. How to log both stdout and stderr to a file?**

```bash
./script.sh &> logfile.log
```

---

## 🏗 **Script Design / Structure**

### **Q16. What does a production-grade Bash script include?**

✅ Shebang
✅ `set -euo pipefail`
✅ functions
✅ argument validation
✅ logging
✅ error handling
✅ cleanup traps
✅ ShellCheck compliant

---

### **Q17. Shebang meaning & example**

**A:** Tells OS which interpreter to use.

```bash
#!/bin/bash
```

---

### **Q18. Script usage/help function**

```bash
usage() {
  echo "Usage: $0 <arg>"
  exit 1
}
```

---

### **Q19. Why do DevOps engineers use shell functions instead of writing long sequential scripts?**

* Reusability
* Readability
* Modular error control
* Easier debugging and testing

---

### **Q20. When do you use Python instead of Bash?**

Use **Python** for:

| Bash              | Python                     |
| ----------------- | -------------------------- |
| Simple automation | Complex logic & APIs       |
| OS tasks          | Data processing            |
| Fast CLI tasks    | Cloud SDKs (boto3)         |
| Package installs  | Infra automation scripting |

---

## ⭐ **Scenario-Based Questions**

### **Q21. Your script fails silently in Jenkins. What do you add?**

```bash
set -euo pipefail
trap 'echo "Error at line $LINENO"' ERR
```

---

### **Q22. A deployment fails mid-way. What should script do?**

* Notify error
* Rollback changes
* Exit with failure code

Use:

```bash
trap rollback ERR
```

---

### **Q23. How to retry a command 5 times?**

```bash
for i in {1..5}; do
  command && break || sleep 2
done
```

---

### **Q24. Monitor a service & auto-restart**

```bash
systemctl is-active --quiet nginx || systemctl restart nginx
```

---

### **Q25. Kill child process on exit**

```bash
trap 'kill $pid' EXIT
some_process & pid=$!
```

---

## 🎯 **Key Interview Takeaways**

| Concept           | Why matters in DevOps   |
| ----------------- | ----------------------- |
| Functions         | modular scripts         |
| set -euo pipefail | safe pipelines          |
| trap              | rollback & cleanup      |
| logging           | debugging in automation |
| exit codes        | CI/CD decisions         |

---


