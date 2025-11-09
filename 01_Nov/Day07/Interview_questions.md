

> **Functions, arguments, error handling, logging, CPU monitoring, cron jobs, email alerts, and basic networking tools.**

---

# 🧭 **Day-07 – DevOps Interview Questions & Answers**

---

## 🧩 **1️⃣ Shell Functions and Arguments**

### Q1. What is a function in Bash and how is it useful?

**Answer:**
A function is a reusable block of code inside a shell script. It avoids repetition and improves readability.

```bash
greet() {
  echo "Hello, $1"
}
greet "Vikas"
```

➡️ Functions help modularize scripts, especially for monitoring or automation tasks.

---

### Q2. How can you pass and access arguments inside a function?

**Answer:**
Arguments passed to a function can be accessed like script arguments:

* `$1`, `$2` → positional parameters
* `$@` → all arguments

```bash
sum() {
  echo "Sum = $(($1 + $2))"
}
sum 10 20
```

---

### Q3. What does `$?` represent?

**Answer:**
It stores the **exit status** of the last executed command.

* `0` → success
* non-zero → error
  Example:

```bash
cp file1 file2
echo $?
```

---

### Q4. How do you make your Bash script exit when a command fails?

**Answer:**
Use:

```bash
set -e
```

✅ This stops the script immediately on any error (useful in production).

---

### Q5. What does `set -euo pipefail` do?

**Answer:**
It enables safe scripting:

* `-e`: Exit on command failure
* `-u`: Error on undefined variables
* `-o pipefail`: Return exit status of first failed command in a pipeline
  Used in CI/CD or automation scripts to avoid silent failures.

---

## ⚙️ **2️⃣ Error Handling and Logging**

### Q6. How can you log both standard output and error output to a file?

**Answer:**

```bash
command >> logfile 2>&1
```

Redirects both stdout (`1`) and stderr (`2`) to the same file.

---

### Q7. How do you trap signals in Bash for cleanup?

**Answer:**
Using the `trap` command:

```bash
trap 'echo "Cleaning up..."; rm -f /tmp/tempfile' EXIT
```

Runs cleanup code when the script exits (gracefully or via Ctrl+C).

---

### Q8. How can you debug a script line by line?

**Answer:**
Use the `-x` flag:

```bash
bash -x script.sh
```

or inside the script:

```bash
set -x
# commands
set +x
```

---

### Q9. What is the purpose of the `exit` command?

**Answer:**
It terminates the script and returns a status code:

* `exit 0` → success
* `exit 1` → generic error

---

### Q10. How do you timestamp log entries in a script?

**Answer:**

```bash
echo "$(date '+%F %T') - CPU Usage: 80%" >> /var/log/monitor.log
```

---

## 📊 **3️⃣ CPU & System Monitoring**

### Q11. How do you check CPU usage from the terminal?

**Answer:**

```bash
top -bn1 | grep "Cpu(s)"
```

or

```bash
top -bn1 | awk '/Cpu/ {print 100 - $8"% used"}'
```

Here `$8` is the idle percentage; subtracting it gives used CPU.

---

### Q12. How to find top CPU-consuming processes?

**Answer:**

```bash
ps -eo pid,comm,%cpu --sort=-%cpu | head -6
```

---

### Q13. How can you find memory usage in Linux?

**Answer:**

```bash
free -m
```

Shows total, used, and free memory in MB.

---

### Q14. What is a “load average”?

**Answer:**
Load average shows the average number of processes waiting for CPU time over 1, 5, and 15 minutes.

---

### Q15. How to continuously monitor system performance?

**Answer:**

```bash
vmstat 2
```

Displays CPU, memory, and I/O stats every 2 seconds.

---

## 🕒 **4️⃣ Cron Jobs and Scheduling**

### Q16. How to list all cron jobs for the current user?

**Answer:**

```bash
crontab -l
```

---

### Q17. How to schedule a script every 5 minutes?

**Answer:**

```
*/5 * * * * /home/ec2-user/cpu_monitor.sh
```

---

### Q18. How to run a job at every reboot?

**Answer:**

```
@reboot /home/ec2-user/startup_script.sh
```

---

### Q19. Why might a cron job fail even though it runs fine manually?

**Answer:**
Cron has a limited environment:

* Missing `PATH` variables
* Relative paths don’t work
  ✅ Fix → use absolute paths and export required environment variables.

---

### Q20. How can you redirect cron output to a log file?

**Answer:**

```
*/10 * * * * /path/script.sh >> /var/log/script.log 2>&1
```

---

## 📧 **5️⃣ Email Alerts (`mailx` / Notifications)**

### Q21. How do you send an email using `mailx` in a script?

**Answer:**

```bash
echo "CPU alert" | mail -s "High CPU Usage" admin@example.com
```

---

### Q22. Where does `mailx` read its SMTP configuration from?

**Answer:**
`~/.mailrc`

---

### Q23. How do you configure `mailx` for Gmail SMTP?

**Answer:**
In `~/.mailrc`:

```bash
set nss-config-dir=/etc/pki/nssdb
set smtp-use-starttls
set smtp=smtp://smtp.gmail.com:587
set smtp-auth=login
set smtp-auth-user=youremail@gmail.com
set smtp-auth-password=your_app_password
set from="youremail@gmail.com (EC2 CPU Monitor)"
set ssl-verify=ignore
```

---

### Q24. How do you send an email with command output as the body?

**Answer:**

```bash
top -bn1 | head -10 | mail -s "Top Processes" you@example.com
```

---

### Q25. How do you send an attachment using `mailx`?

**Answer:**

```bash
echo "Log file attached" | mail -s "Server Logs" -a /tmp/app.log you@example.com
```

---

## 🌐 **6️⃣ Basic Networking & Connectivity**

### Q26. How to check if a host is reachable?

**Answer:**

```bash
ping -c 4 google.com
```

---

### Q27. How to check if port 587 is open for SMTP?

**Answer:**

```bash
nc -zv smtp.gmail.com 587
```

---

### Q28. How to list all listening ports and services?

**Answer:**

```bash
ss -tuln
# or
netstat -tuln
```

---

### Q29. How to resolve a domain name manually?

**Answer:**

```bash
dig example.com +short
# or
nslookup example.com
```

---

### Q30. How do you test a website’s response headers?

**Answer:**

```bash
curl -I https://www.google.com
```

Shows status code and headers — useful for debugging web health checks.

---

## 🧠 **7️⃣ Real-World Scenarios**

### Q31. Write a function that checks CPU usage and emails an alert if it’s below 80%.

**Answer:**

```bash
check_cpu() {
  cpu_idle=$(top -bn1 | awk '/Cpu/ {print $8}')
  cpu_used=$(echo "scale=1; 100 - $cpu_idle" | bc)
  cpu_used_int=${cpu_used%.*}

  if (( cpu_used_int < 80 )); then
    echo "CPU usage is ${cpu_used}% on $(hostname)" \
    | mail -s "ℹ️ Low CPU Alert" youremail@gmail.com
  fi
}
check_cpu
```

---

### Q32. How do you log script activity with timestamps?

**Answer:**

```bash
echo "$(date '+%F %T') - CPU=${cpu_used}%" >> /tmp/cpu_monitor.log
```

---

### Q33. How can you debug a cron job that doesn’t send an email?

**Answer:**

* Add `-v` to the `mail` command for verbose logging.
* Check `/var/log/maillog` or `/var/log/messages`.
* Ensure `~/.mailrc` permissions are `600`.

---

### Q34. How to automatically clean up logs older than 7 days?

**Answer:**

```bash
find /var/log -type f -name "*.log" -mtime +7 -delete
```

---

### Q35. How can you check network latency or routing path?

**Answer:**

```bash
traceroute google.com
```

---

✅ **End of Day-07 Topics**

By the end of Day-7, you should:

* Write modular, error-handled Bash scripts
* Automate system checks via cron
* Send email alerts (using `mailx`)
* Debug network and resource issues efficiently

---


