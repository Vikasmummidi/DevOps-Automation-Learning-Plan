

---

# 🧭 **Day-3 Interview Questions & Answers**

---

## 🧩 **Section 1: Redirection**

### **Q1. What is output redirection in Linux?**

**A:** Output redirection (`>`, `>>`) sends the standard output of a command to a file instead of displaying it on the screen.

* `>` overwrites the file.
* `>>` appends to the file.
  **Example:**

```bash
echo "Log entry" > app.log      # overwrite
echo "New entry" >> app.log     # append
```

---

### **Q2. What’s the difference between `>` and `2>`?**

**A:**

* `>` redirects **stdout (file descriptor 1)**
* `2>` redirects **stderr (file descriptor 2)**
  Example:

```bash
ls /no/path 2> error.log
```

This captures only the error message, not the normal output.

---

### **Q3. How can you redirect both stdout and stderr to the same file?**

**A:**
Either of the following:

```bash
command &> output.log
# or
command > output.log 2>&1
```

---

### **Q4. What is `/dev/null` and why is it used?**

**A:**
`/dev/null` is a **special device file** that discards all data written to it (like a black hole).
Used to suppress unwanted output.
Example:

```bash
command > /dev/null 2>&1
```

✅ Common in automation scripts or cron jobs to keep logs clean.

---

### **Q5. How do you redirect input from a file?**

**A:**
Use `<` to feed input from a file to a command.

```bash
sort < data.txt
```

---

## 🧩 **Section 2: Pipes and Chaining**

### **Q6. What is the difference between a pipe (`|`) and redirection (`>`)?**

**A:**

* A **pipe** sends the **output of one command directly as input to another command**.
* **Redirection** sends output to a **file**.
  Example:

```bash
ls | grep .sh     # pipe
ls > files.txt    # redirection
```

---

### **Q7. How does `grep` work with pipes? Why does `grep` sometimes show itself in the output?**

**A:**
`grep` filters text from another command’s output.
When using `ps aux | grep bash`, the `grep bash` process itself appears in the result because its command line contains “bash.”
✅ To fix:

```bash
ps aux | grep [b]ash
# or
ps aux | grep bash | grep -v grep
```

---

### **Q8. How is the `tee` command different from a pipe?**

**A:**
`tee` writes output **to both a file and the terminal simultaneously**.

```bash
ls | tee list.txt
df -h | tee -a disk_usage.txt
```

---

### **Q9. Explain `;`, `&&`, and `||` in command chaining.**

**A:**

| Operator | Meaning                                 | Example               |                                      |         |   |                |
| -------- | --------------------------------------- | --------------------- | ------------------------------------ | ------- | - | -------------- |
| `;`      | Run commands sequentially               | `mkdir dir; cd dir`   |                                      |         |   |                |
| `&&`     | Run next **only if previous succeeded** | `mkdir dir && cd dir` |                                      |         |   |                |
| `        |                                         | `                     | Run next **only if previous failed** | `cd dir |   | echo "Failed"` |

---

### **Q10. Write a one-liner to check if a file exists, and print a message accordingly.**

**A:**

```bash
[ -f file.txt ] && echo "Exists" || echo "Not found"
```

---

## 🧩 **Section 3: Exit Codes**

### **Q11. What is an exit code?**

**A:**
An exit code (stored in `$?`) is a numeric value returned by a command — `0` for success, non-zero for failure.

Example:

```bash
ls /etc
echo $?   # 0 → success

ls /fake
echo $?   # non-zero → failure
```

---

### **Q12. How do you use exit codes in shell scripts for error handling?**

**A:**

```bash
if command; then
  echo "Success"
else
  echo "Failed"
fi
```

or

```bash
command || { echo "Command failed"; exit 1; }
```

---

### **Q13. What does `set -e` do in bash scripts?**

**A:**
`set -e` causes the script to **exit immediately** if any command fails (non-zero exit code).
Commonly used in CI/CD scripts for reliability.

---

### **Q14. How do you check the last executed command’s status?**

**A:**
By echoing `$?`

```bash
echo $?
```

---

### **Q15. Give a real DevOps example where exit codes are important.**

**A:**
In Jenkins or CI/CD pipelines:

```bash
terraform plan || exit 1
ansible-playbook deploy.yml && echo "Deployment successful"
```

✅ Ensures next step runs only if previous one succeeded.

---

## 🧩 **Section 4: Scenario-Based Questions**

### **Q16. Write a command that logs only the failed commands’ error messages to `error.log`.**

**A:**

```bash
command 2> error.log
```

---

### **Q17. You want to run a backup command silently (no output, no errors). How?**

**A:**

```bash
backup.sh &> /dev/null
```

---

### **Q18. How would you print the top 5 CPU processes and log them to a file?**

**A:**

```bash
ps -eo pid,comm,%cpu --sort=-%cpu | head -6 > top_cpu.log
```

---

### **Q19. Why is proper use of exit codes critical in DevOps automation?**

**A:**
Because automation tools (like Jenkins, Ansible, Terraform) depend on **exit codes** to decide whether to stop, retry, or proceed.
Without correct exit handling, pipelines can appear “successful” even when something failed silently.

---

### **Q20. What’s the difference between `$?`, `$0`, `$1`, and `$$` in shell?**

| Variable | Meaning                         |
| -------- | ------------------------------- |
| `$?`     | Exit status of last command     |
| `$0`     | Name of the script              |
| `$1`     | First argument passed to script |
| `$$`     | Process ID of current shell     |

---


