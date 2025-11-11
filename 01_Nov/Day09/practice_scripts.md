### 🛠 Practice Programs

**Program A – File Read/Write & Counting**
Write a script that:

1. Opens (or creates) `logs.txt`.
2. Writes 10 lines of sample text (some containing the word `"ERROR"`).
3. Reads the file, counts how many lines contain `"ERROR"`.
4. Prints: `"Total ERROR lines: X"`.
5. Appends a summary line at end: `"Summary: X error lines found."`.

**Program B – Directory Management**
Write a script that:

1. Checks if folder `backup/` exists in current directory; if not, creates it.
2. Copies `logs.txt` into `backup/logs_backup_TIMESTAMP.txt` (use e.g., `datetime.now()` in filename).
3. Lists all files in `backup/` and prints them.
4. If there are more than 5 backup files, deletes oldest ones until only 5 remain.

**Program C – Automation: Disk Usage Alert**
Write a script that:

1. Defines function `get_disk_usage(mount_point)` that uses `subprocess.run(['df', '-h', mount_point], capture_output=True, text=True)` to get usage.
2. Parses output lines, extracts the `%` usage value.
3. If usage percent > 80, logs a warning: `"ALERT: {filesystem} on {mount_point} is {usage}% full"` to a file `alerts.log`.
4. Also, prints the alert to console.
5. Optionally, sends the alert by email or writes to syslog (just describe or stub for now).

---

### ✅ Self-Quiz (last 15 mins)

1. What is the difference between `open('file.txt','r+')` and `open('file.txt','w')`?
2. Why should you use `with open(...) as f:` instead of manual `open()` + `close()`?
3. When would you use `shutil.disk_usage()` vs using `subprocess.run(['df','-h'])`?
4. How do you safely delete a directory tree in Python? (which module and function)
5. Write a one-liner to count lines in a file that contain `"WARN"` (no full script needed).
6. Explain how `subprocess.run()` works with `capture_output=True` and `text=True`.

---
