Below are **DevOps-focused interview questions & answers** for **Day-4 topics: Variables, Loops, Conditionals in Bash**.
These are asked frequently in **Linux / Shell / DevOps / SRE interviews**.

---

# ✅ **Bash Scripting — Interview Q&A**

---

## ⭐ **Variables & Parameters**

### **Q1. How do you declare a variable in Bash?**

**A:**

```bash
name="Vikas"
echo $name
```

> No spaces around `=`.

---

### **Q2. Difference between `$*` and `$@`?**

| Variable | Meaning                               |
| -------- | ------------------------------------- |
| `$*`     | All arguments as a **single string**  |
| `$@`     | All arguments as **separate strings** |

Example:

```bash
for arg in "$*"; do echo "$arg"; done   # 1 iteration
for arg in "$@"; do echo "$arg"; done   # n iterations
```

---

### **Q3. What does `$#` return?**

**A:** Number of arguments passed to script.

```bash
echo "Args count: $#"
```

---

### **Q4. What is `${var}` vs `$var`?**

**A:** Braces avoid ambiguity and enable expansion:

```bash
name="Dev"
echo "Hello $name"
echo "Hello ${name}Ops"   # ✅
```

---

### **Q5. Default value syntax in Bash?**

**A:** Use `${var:-default}`

```bash
file=${1:-output.log}
```

---

### **Q6. Difference between `export VAR=value` and `VAR=value`?**

| Type               | Scope                            |
| ------------------ | -------------------------------- |
| `VAR=value`        | Shell only                       |
| `export VAR=value` | Available to **child processes** |

---

## ⭐ **User Input & Arguments**

### **Q7. How to accept user input?**

```bash
read -p "Enter name: " name
echo "Hello $name"
```

---

### **Q8. How do you pass arguments to a script?**

`$1, $2 … $@`

```bash
#!/bin/bash
echo "User: $1"
```

Run:

```bash
./script.sh Vikas
```

---

## ⭐ **Conditionals**

### **Q9. Syntax of `if-else` in Bash?**

```bash
if [[ condition ]]; then
  commands
elif [[ another ]]; then
  commands
else
  commands
fi
```

---

### **Q10. File test operators?**

| Purpose          | Condition |
| ---------------- | --------- |
| Exists           | `-e file` |
| Regular file     | `-f file` |
| Directory        | `-d dir`  |
| Non-empty string | `-n`      |
| Empty string     | `-z`      |

Example:

```bash
if [[ -f "$file" ]]; then ...
```

---

### **Q11. Numeric vs string comparison in Bash?**

| Numeric         | String     |
| --------------- | ---------- |
| `-eq, -gt, -lt` | `==`, `!=` |

---

### **Q12. Why use `[[ ]]` instead of `[ ]`?**

**A:** `[[ ]]` is Bash enhanced test:
✅ regex support
✅ no word splitting issues
✅ safer for variables with spaces

---

## ⭐ **Loops**

### **Q13. For loop example**

```bash
for i in {1..5}; do
  echo "Run $i"
done
```

---

### **Q14. Loop through files**

```bash
for file in *.log; do
  echo "$file"
done
```

---

### **Q15. While loop example**

```bash
count=1
while [[ $count -le 5 ]]; do
  echo $count
  ((count++))
done
```

---

### **Q16. How to break & continue loops?**

```bash
for i in {1..5}; do
  [[ $i -eq 3 ]] && continue
  [[ $i -eq 5 ]] && break
  echo $i
done
```

---

## ⭐ **Real DevOps Scenarios**

### **Q17. Script to check service status**

```bash
service=$1
if systemctl is-active --quiet "$service"; then
  echo "$service running"
else
  echo "$service not running"
fi
```

---

### **Q18. Script to delete logs older than 7 days**

```bash
for file in /var/log/*.log; do
  if [[ $(find "$file" -mtime +7) ]]; then
    rm "$file"
  fi
done
```

---

### **Q19. Script to loop through servers & run command**

```bash
servers="srv1 srv2 srv3"
for s in $servers; do
  ssh "$s" "uptime"
done
```

---

### **Q20. Script to monitor high CPU processes**

```bash
for pid in $(ps -eo pid,%cpu --sort=-%cpu | awk 'NR>1 {print $1}' | head -5); do
  name=$(ps -p $pid -o comm=)
  cpu=$(ps -p $pid -o %cpu=)
  echo "$name $cpu%"
done
```

---

## 🎤 **Bonus HR-style Question**

### **Q: Why do DevOps engineers need Bash scripting?**

**A:**
Bash scripting enables:

* Automating deployments & builds
* Handling system checks & monitoring
* CI/CD task automation
* Log analysis
* Provisioning & server maintenance without manual effort

> “In DevOps, Bash is a must — to automate and orchestrate OS-level tasks efficiently.”

---
Perfect — here are the **solutions for all 20 Day-4 Bash exercises** ✅
Each script is clean, production-style, and uses DevOps-recommended patterns.

---

# ✅ **Day-4 Exercise Solutions**

---

## 1) Greeting with variable & argument

```bash
#!/bin/bash
name=${1:-User}
echo "Hello $name 👋"
```

---

## 2) Script name & arguments

```bash
#!/bin/bash
echo "Script: $0"
echo "Args count: $#"
echo "Args: $@"
```

---

## 3) Read user input

```bash
#!/bin/bash
read -p "Enter your name: " name
echo "Welcome, $name"
```

---

## 4) Store command output in variable

```bash
#!/bin/bash
TODAY=$(date)
echo "Today is $TODAY"
```

---

## 5) Default value for variable

```bash
#!/bin/bash
file=${1:-default.txt}
echo "Using file: $file"
```

---

## 6) Check filename passed or exit

```bash
#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

echo "File argument supplied: $1"
```

---

## 7) File/directory check

```bash
#!/bin/bash
item=$1

if [[ -f "$item" ]]; then
  echo "$item is a file"
elif [[ -d "$item" ]]; then
  echo "$item is a directory"
else
  echo "$item does not exist"
fi
```

---

## 8) Compare two numbers

```bash
#!/bin/bash

if [[ $1 -gt $2 ]]; then
  echo "$1 is greater"
else
  echo "$2 is greater"
fi
```

---

## 9) Check if service running

```bash
#!/bin/bash

service=$1

if systemctl is-active --quiet "$service"; then
  echo "$service is running ✅"
else
  echo "$service is NOT running ❌"
fi
```

---

## 10) Age validation

```bash
#!/bin/bash
read -p "Enter age: " age

if [[ $age -ge 18 ]]; then
  echo "Eligible ✅"
else
  echo "Not eligible ❌"
fi
```

---

## 11) Print numbers 1-10

```bash
#!/bin/bash
for i in {1..10}; do echo $i; done
```

---

## 12) Countdown 5-1

```bash
#!/bin/bash
count=5

while [[ $count -ge 1 ]]; do
  echo $count
  ((count--))
done
```

---

## 13) Loop through arguments

```bash
#!/bin/bash
for arg in "$@"; do echo "$arg"; done
```

---

## 14) List `.log` files with size

```bash
#!/bin/bash
for file in *.log; do
  [[ -e "$file" ]] || continue
  size=$(du -sh "$file" | awk '{print $1}')
  echo "$file — $size"
done
```

---

## 15) Read file line-by-line

```bash
#!/bin/bash
while read line; do
  echo "$line"
done < "$1"
```

---

## 16) Ping server list

```bash
#!/bin/bash

for server in $(cat servers.txt); do
  if ping -c1 -W1 "$server" &> /dev/null; then
    echo "$server reachable ✅"
  else
    echo "$server unreachable ❌"
  fi
done
```

---

## 17) Delete tmp files older than 2 days

```bash
#!/bin/bash
find /tmp -name "*.tmp" -mtime +2 -exec rm {} \;
echo "Old tmp files deleted ✅"
```

---

## 18) CPU alert > 80%

```bash
#!/bin/bash
cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d. -f1)

if [[ $cpu -gt 80 ]]; then
  echo "High CPU Alert: $cpu%"
else
  echo "CPU OK: $cpu%"
fi
```

---

## 19) Disk usage alert

```bash
#!/bin/bash
usage=$(df / | awk 'NR==2 {gsub("%",""); print $5}')

if [[ $usage -gt 80 ]]; then
  echo "Disk usage high: $usage%"
else
  echo "Disk usage normal: $usage%"
fi
```

---

## 20) Top CPU process log loop

```bash
#!/bin/bash

log="cpu.log"
echo "--- $(date) ---" >> "$log"

for pid in $(ps -eo pid --sort=-%cpu | awk 'NR>1' | head -5); do
  cpu=$(ps -p "$pid" -o %cpu=)
  cmd=$(ps -p "$pid" -o comm=)
  echo "PID: $pid | CPU: $cpu | CMD: $cmd" >> "$log"
done

echo "Logged ✅"
```

---

