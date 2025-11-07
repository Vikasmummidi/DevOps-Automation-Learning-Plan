Perfect 👏 — it’s **Day-6 (06-Nov-2025)** and your focus is **“Automate Tasks: Log Cleanup & Backups”** — a *real DevOps daily responsibility.*

Let’s make today’s **2-hour worksheet** simple, practical, and cron-ready.

---

# 🧭 **Day-6 Practice Worksheet**

**Focus Area:** Shell Automation
**Topic:** Log Cleanup & Backups
**Goal:** Write cron-friendly scripts for rotation and backup

---

## ⏱️ **2-Hour Study & Practice Plan**

| Time       | Topic                      | Key Concepts                         | Hands-on                 |
| ---------- | -------------------------- | ------------------------------------ | ------------------------ |
| 0–20 min   | Understanding log rotation | Log aging, backup naming             | Explore `/var/log`       |
| 20–50 min  | Log cleanup script         | `find`, `rm`, `xargs`                | Cleanup old logs         |
| 50–80 min  | Backup automation          | Archive, compress, timestamp         | `tar`, `gzip`            |
| 80–120 min | Cron-friendly automation   | Scheduling, silent mode, email alert | Write & test full script |

---

## 📘 **Concept Quick Reference**

### 🧩 1️⃣ Log Rotation Basics

* Old logs are rotated to save disk space.
* Typically, older files get:

  * Renamed with dates (`app.log.1`, `app.log.2`)
  * Archived or deleted
* Use **`find`** for cleanup and **`tar/gzip`** for backup.

---

### 🧩 2️⃣ Common Tools

| Command                              | Use                              |
| ------------------------------------ | -------------------------------- |
| `find /path -name "*.log" -mtime +7` | Find files older than 7 days     |
| `rm`, `xargs rm`                     | Delete found files               |
| `tar -czf`                           | Create compressed tarball        |
| `date +%F`                           | Generate date stamp (YYYY-MM-DD) |
| `crontab -e`                         | Edit cron schedule               |
| `shellcheck script.sh`               | Lint for syntax errors           |

---

## 🧪 **Hands-On Practice Blocks**

---

### ✅ **Block-1: Explore Logs (10 min)**

Check where logs live:

```bash
cd /var/log
ls -lh
du -sh *
```

See file sizes and identify which ones grow often.

---

### ✅ **Block-2: Log Cleanup Script (30 min)**

Create `cleanup_logs.sh`:

```bash
#!/bin/bash
# cleanup_logs.sh
# Deletes log files older than 7 days

LOG_DIR="/var/log"
DAYS=7
DATE=$(date '+%F')
LOG_FILE="/tmp/log_cleanup_$DATE.log"

echo "Starting cleanup: $(date)" > "$LOG_FILE"

find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -print -delete >> "$LOG_FILE" 2>&1

echo "Cleanup completed on $(date)" >> "$LOG_FILE"
```

Run:

```bash
chmod +x cleanup_logs.sh
./cleanup_logs.sh
cat /tmp/log_cleanup_$(date +%F).log
```

✅ This script:

* Finds `.log` files older than 7 days
* Deletes them
* Logs results to `/tmp`

---

### ✅ **Block-3: Backup Script (30 min)**

Create `backup_logs.sh`:

```bash
#!/bin/bash
# backup_logs.sh
# Compresses recent logs into a backup file

SOURCE_DIR="/var/log"
BACKUP_DIR="/backup"
DATE=$(date '+%F')
BACKUP_FILE="$BACKUP_DIR/logs_backup_$DATE.tar.gz"

mkdir -p "$BACKUP_DIR"

echo "Starting backup at $(date)"
tar -czf "$BACKUP_FILE" "$SOURCE_DIR"/*.log 2>/dev/null
echo "Backup complete: $BACKUP_FILE"
```

Run:

```bash
chmod +x backup_logs.sh
sudo ./backup_logs.sh
```

✅ Output:

```
Starting backup at Thu Nov 06 12:25:31 IST 2025
Backup complete: /backup/logs_backup_2025-11-06.tar.gz
```

---

### ✅ **Block-4: Cron Integration (20 min)**

#### Step 1: Open crontab

```bash
crontab -e
```

#### Step 2: Add these lines

```bash
# Log cleanup every day at midnight
0 0 * * * /home/ubuntu/scripts/cleanup_logs.sh > /dev/null 2>&1

# Backup logs every Sunday at 1 AM
0 1 * * 0 /home/ubuntu/scripts/backup_logs.sh > /dev/null 2>&1
```

✅ This:

* Runs automatically
* Redirects all output to `/dev/null` (cron best practice)
* Keeps your server clean and logs backed up weekly

---

### ✅ **Block-5: Validate with ShellCheck (10 min)**

Visit → [https://www.shellcheck.net](https://www.shellcheck.net)
Paste your scripts and fix warnings.

Common issues to fix:

* Quote your variables → `"${var}"`
* Use `#!/bin/bash` not `/bin/sh`
* Handle unset variables with `set -u`

---

## 🧠 **DevOps Reality Connection**

| Real-world scenario         | You now can automate |
| --------------------------- | -------------------- |
| Application logs rotation   | ✅ Yes                |
| Disk cleanup jobs           | ✅ Yes                |
| Backup management           | ✅ Yes                |
| Scheduled tasks via cron    | ✅ Yes                |
| Safe scripting with logging | ✅ Yes                |

You’re learning the **exact daily scripting tasks** a DevOps engineer handles on Linux servers.

---

## 🎯 **Day-6 Deliverables**

✔ `cleanup_logs.sh`
✔ `backup_logs.sh`
✔ `cron` configuration
✔ ShellCheck validation
✔ Understanding log lifecycle automation

---


