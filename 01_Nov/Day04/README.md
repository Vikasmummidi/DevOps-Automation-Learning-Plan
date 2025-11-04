
---

## 🎯 **Learning Goals for Day-4**

By end of session you should be able to:

✅ Declare & use **variables**
✅ Accept **arguments** and use `$#, $@, $1 ...`
✅ Write **if-else** conditions & test operators
✅ Use loops: `for`, `while`
✅ Make **reusable scripts** with parameters
✅ Lint scripts using ShellCheck
✅ Build a real-world automation script

Time required: **~2 hours**

---

## ⏱️ **2-Hour Plan Breakdown**

| Time       | Topic                 | Concepts                                                 | Hands-on                          |
| ---------- | --------------------- | -------------------------------------------------------- | --------------------------------- |
| 0–20 min   | Variables + arguments | `VAR=`, `$1`, `$@`, `$#`, `read`                         | Print variables, script with args |
| 20–50 min  | Conditionals          | `if..else`, `[[ ]]`, operators (`-eq`, `==`, `-f`, `-d`) | File check script                 |
| 50–80 min  | Loops                 | `for`, `while`, `break`, `continue`                      | Loop examples on files/processes  |
| 80–120 min | Project               | Script with params + loops + conditions                  | CPU top script (enhanced)         |
| Bonus      | Linting               | ShellCheck                                               | Fix warnings                      |

---

## 📘 **Mini-Theory Before Practicing**

### **Variables**

```bash
name="Vikas"
echo "Hello $name"
```

### **Command line args**

```bash
echo "Script name: $0"
echo "First arg: $1"
echo "All args: $@"
echo "Arg count: $#"
```

### **Conditionals**

```bash
if [[ $num -gt 10 ]]; then
  echo "Greater than 10"
else
  echo "Less or equal"
fi
```

Common test flags:

| Purpose        | Operator                      |
| -------------- | ----------------------------- |
| int comparison | `-eq -ne -gt -lt -ge -le`     |
| file exists    | `-e`                          |
| file check     | `-f` (file), `-d` (directory) |
| string         | `==`, `!=`, `-z`, `-n`        |

### **Loops**

```bash
for i in {1..5}; do echo $i; done
```

```bash
while true; do echo "Running"; sleep 1; done
```

---

## 📝 **Day-4 Practice Worksheet**

### ✅ **Block-1 (0–20min): Variables & Arguments**

#### Create file `vars.sh`

```bash
#!/bin/bash

name="Vikas"
echo "Hello $name"

echo "Script Name: $0"
echo "First Arg: $1"
echo "All Args: $@"
echo "Count: $#"
```

Run:

```bash
chmod +x vars.sh
./vars.sh DevOps India
```

---

### ✅ **Block-2 (20–50min): Conditions Practice**

#### Script: `check_file.sh`

```bash
#!/bin/bash

FILE=$1

if [[ -f "$FILE" ]]; then
    echo "$FILE is a file"
elif [[ -d "$FILE" ]]; then
    echo "$FILE is a directory"
else
    echo "File not found"
fi
```

Run:

```bash
./check_file.sh /etc/passwd
./check_file.sh /etc
./check_file.sh dummy
```

---

### ✅ **Block-3 (50–80min): Loops**

#### For loop

```bash
for i in {1..5}; do echo "Counter: $i"; done
```

#### Loop through files

```bash
for file in *.sh; do echo "Script: $file"; done
```

#### While loop

```bash
count=1
while [[ $count -le 3 ]]; do
  echo "Run #$count"
  ((count++))
done
```

---

### ✅ **Block-4 (80–120min): Automation Project**

**Goal:** Script with parameters, condition, loop, log

#### File: `top_cpu_v2.sh`

```bash
#!/bin/bash

LOG=${1:-cpu.log}   # default file cpu.log if not passed

echo "Logging top 5 CPU processes to $LOG"
echo "---- $(date) ----" >> "$LOG"

count=0
for pid in $(ps -eo pid,%cpu --sort=-%cpu | awk 'NR>1 {print $1}' | head -5)
do
  ((count++))
  cpu=$(ps -p "$pid" -o %cpu=)
  name=$(ps -p "$pid" -o comm=)
  echo "$count) PID: $pid | Process: $name | CPU: $cpu%" >> "$LOG"
done

echo "Done ✅"
```

Run:

```bash
chmod +x top_cpu_v2.sh
./top_cpu_v2.sh system_cpu.log
cat system_cpu.log
```

---

### ✅ **ShellCheck Lint**

Visit: **[https://www.shellcheck.net/](https://www.shellcheck.net/)**
Paste script → fix warnings

---

## 🎯 **Today's Output**

By completing today you will have:

* Learned real-world bash scripting skills
* Written 3 automation scripts
* Learned params, loops, conditions
* Followed industry patterns
* Prepared for DevOps interviews

---


