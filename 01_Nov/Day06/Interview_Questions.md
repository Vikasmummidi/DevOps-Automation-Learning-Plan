**interview-style Q&A** for **Day-6 Topics: Shell Automation, Log Cleanup, Backups, and Cron Jobs**.
These are *real DevOps interview questions* — mixing fundamentals, scripting logic, and real-world problem-solving.

---

# 🧠 **Day-6 DevOps Interview Q&A**

---

## 🔹 **Section 1: Log Management & Cleanup**

### **Q1. Why do we rotate or clean up logs in servers?**

**A:**
Because logs grow continuously and can quickly consume disk space.
Log rotation or cleanup ensures:

* Disk space is available for critical processes
* Better performance and stability
* Compliance with retention policies

> In DevOps, automated log cleanup prevents **server outages due to full disks**.

---

### **Q2. How do you find and delete log files older than 7 days?**

**A:**

```bash
find /var/log -type f -name "*.log" -mtime +7 -delete
```

* `-type f` → only files
* `-mtime +7` → modified more than 7 days ago
* `-delete` → delete them

**Tip:** Always test first with `-print` before deleting.

---

### **Q3. What does this mean?**

```bash
find /var/log -name "*.log" -mtime +7 -print -delete
```

**A:**
It prints the names of `.log` files older than 7 days and then deletes them — a safe way to verify before deletion.

---

### **Q4. What happens if you run your cleanup script without `sudo`?**

**A:**
You may get `Permission denied` errors for system-owned log directories (e.g. `/var/log/nginx`, `/var/log/audit`).
Fix by:

* Running as root (`sudo ./script.sh`)
* Or excluding protected directories.

---

### **Q5. Why is `2>/dev/null` used in find commands?**

**A:**
It redirects **error messages** (stderr) to `/dev/null` — a “black hole.”
Example:

```bash
find /var/log -type f -mtime +7 -delete 2>/dev/null
```

✅ Cleans logs silently, without printing permission errors.

---

## 🔹 **Section 2: Backups and Archiving**

### **Q6. What is the use of `tar -zcvf`?**

**A:**
It creates a compressed archive file.

```bash
tar -zcvf backup.tar.gz /path/to/data
```

* `-z` → gzip compression
* `-c` → create archive
* `-v` → verbose (show files)
* `-f` → specify filename

---

### **Q7. How to extract a `.tar.gz` file?**

**A:**

```bash
tar -zxvf backup.tar.gz
```

* `-x` → extract

---

### **Q8. How to add a date stamp to a backup file in Bash?**

**A:**

```bash
tar -zcvf backup_$(date '+%F').tar.gz /var/log
```

→ Creates file like `backup_2025-11-07.tar.gz`.

---

### **Q9. Why is `$(date '+%F')` used in scripts?**

**A:**
`$(...)` runs a command and replaces it with the output.
`date '+%F'` prints the date in ISO format (`YYYY-MM-DD`).
It’s used for naming log or backup files uniquely by date.

---

### **Q10. What’s the difference between `/tmp`, `/var/log`, and `/opt` directories?**

| Directory  | Purpose                           |
| ---------- | --------------------------------- |
| `/tmp`     | Temporary files cleared on reboot |
| `/var/log` | System and service log files      |
| `/opt`     | Optional software installations   |

---

## 🔹 **Section 3: Cron Automation**

### **Q11. What is a cron job?**

**A:**
A **scheduled task** that runs automatically at specific intervals using the `cron` daemon.
Used for automation — e.g., backups, monitoring, cleanup.

---

### **Q12. Cron syntax breakdown**

```
* * * * * command
│ │ │ │ │
│ │ │ │ └── Day of week (0–7)
│ │ │ └──── Month (1–12)
│ │ └────── Day of month (1–31)
│ └──────── Hour (0–23)
└────────── Minute (0–59)
```

---

### **Q13. Write a cron job to run cleanup every midnight**

**A:**

```bash
0 0 * * * /home/ubuntu/scripts/cleanup_logs.sh > /dev/null 2>&1
```

Runs daily at 12:00 AM.
Redirects all output to `/dev/null`.

---

### **Q14. How to schedule a weekly backup every Sunday at 1 AM?**

**A:**

```bash
0 1 * * 0 /home/ubuntu/scripts/backup_logs.sh > /dev/null 2>&1
```

---

### **Q15. What does this mean?**

```bash
*/10 * * * * /scripts/monitor.sh
```

**A:**
Runs `monitor.sh` every **10 minutes**.

---

### **Q16. What is the difference between user cron and system cron?**

| Type                                        | Description                          |
| ------------------------------------------- | ------------------------------------ |
| User cron (`crontab -e`)                    | Runs under that user’s permissions   |
| System cron (`/etc/crontab`, `/etc/cron.*`) | Managed by system (root-level tasks) |

---

### **Q17. What does `@reboot` mean in cron?**

**A:**
Runs the command **once after every system restart**.
Example:

```bash
@reboot /home/ubuntu/startup.sh
```

---

### **Q18. Why use absolute paths in cron jobs?**

**A:**
Because cron runs in a minimal environment and doesn’t load your `.bashrc` or PATH.
Always specify full paths:

```bash
/usr/bin/python3 /home/ubuntu/script.py
```

---

### **Q19. How do you check if a cron job ran successfully?**

**A:**

* Check `/var/log/syslog` or `/var/log/cron`

  ```bash
  grep CRON /var/log/syslog
  ```
* Add logging inside your script.
* Redirect output in cron to a log file.

---

### **Q20. Why redirect output in cron jobs to `/dev/null`?**

**A:**
To prevent unwanted emails or log spam from cron’s default output.
Example:

```bash
0 0 * * * /script.sh > /dev/null 2>&1
```

✅ Runs silently unless an error occurs.

---

## 🔹 **Section 4: Real DevOps Scenarios**

### **Q21. How do you automate log cleanup + backup together?**

**A:**
Chain both scripts:

```bash
#!/bin/bash
/home/ubuntu/scripts/cleanup_logs.sh
/home/ubuntu/scripts/backup_logs.sh
```

Schedule:

```bash
0 0 * * * /home/ubuntu/scripts/maintenance.sh > /dev/null 2>&1
```

---

### **Q22. What happens if two cron jobs overlap (run at same time)?**

**A:**
They’ll run in parallel — which can cause conflicts.
Use file locks or `flock` to prevent overlap:

```bash
flock -n /tmp/cleanup.lock /scripts/cleanup.sh
```

---

### **Q23. How do you monitor cron jobs in production?**

**A:**

* Redirect outputs to log files
* Configure mail alerts (`MAILTO=user@example.com`)
* Use system monitoring tools like **Grafana / Prometheus / Datadog**

---

### **Q24. How do you test cron scripts manually?**

**A:**
Run them directly using bash:

```bash
bash /path/to/script.sh
```

Then check logs to ensure no permission/path issues.

---

### **Q25. What are common mistakes in cron automation?**

**A:**

* Using relative paths instead of full paths
* Missing environment variables (PATH, HOME)
* Forgetting execution permissions (`chmod +x`)
* Not redirecting output → filling mail logs
* Overlapping cron runs

---

## 🧠 **Quick Recap Table**

| Topic           | Must-know Commands                             |
| --------------- | ---------------------------------------------- |
| Log cleanup     | `find /var/log -mtime +7 -delete`              |
| Backup          | `tar -zcvf backup_$(date +%F).tar.gz /var/log` |
| Scheduling      | `crontab -e`, `crontab -l`                     |
| Log redirection | `> /dev/null 2>&1`                             |
| Extract backups | `tar -zxvf file.tar.gz`                        |

---

## 🎯 **DevOps-Level Tip**

In production, combine everything with notifications:

```bash
if ./cleanup_logs.sh && ./backup_logs.sh; then
  echo "Maintenance OK" | mail -s "Server Maintenance Report" admin@example.com
else
  echo "Error during maintenance" | mail -s "Server Error Alert" admin@example.com
fi
```

---


