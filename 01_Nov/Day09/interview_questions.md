## 🎤 Interview Questions & Answers (for ~4 yrs DevOps Engineer)

Here are **10 targeted questions** with suggested answer points. Use these to prep for your DevOps-interview when Python + automation + file handling skills are expected.

### Q1. How do you make a Python script executable on a Unix/Linux system?

**Answer:**

* Add shebang line at top, e.g.: `#!/usr/bin/env python3`
* Give execute permission: `chmod +x script.py`
* Ensure first line uses correct path or environment.
* Then you can run `./script.py` (if in PATH or specifying path).

### Q2. What file open modes are available in Python? When to use each (r, w, a, r+, w+)?

**Answer:**

* `'r'`: read only, file must exist.
* `'w'`: write only, creates/overwrites file (truncates).
* `'a'`: append only, writes at end (creates if not exist).
* `'r+'`: read/write, file must exist, does not truncate.
* `'w+'`: read/write, creates/overwrites file (truncates).
* Use `'a'` for logs, `'w'` for full overwrite, `'r+'` when modifying in-place etc.

### Q3. Why should you use a context manager (`with open(...) as f:`) for file handling?

**Answer:**

* Ensures file is properly closed even if exceptions occur.
* Cleaner syntax, avoids forgetting `f.close()`.
* Handles resource cleanup automatically — good for reliability in automation.

### Q4. What are some common functions in the `os` and `shutil` modules you’ve used for file system automation?

**Answer:**

* `os.path.exists()`, `os.listdir()`, `os.remove()`, `os.mkdir()`, `os.rename()`
* `shutil.copy()`, `shutil.move()`, `shutil.rmtree()`, `shutil.disk_usage()`
* Use cases: backup files, rotate logs, delete temp dirs, monitor disk space.

### Q5. Explain how you would monitor disk usage and trigger alerts via Python.

**Answer:**

* Use `shutil.disk_usage('/')` to get (total, used, free) in bytes.
* Or call system command via `subprocess.run(['df','-h'], capture_output=True, text=True)` and parse output.
* Check usage percentage, if > threshold (e.g., 80 %), write to alert log, send email, call external monitoring API.
* Wrap logic in a function, schedule via cron or Jenkins job for periodic check.

### Q6. How do you safely handle modifying a file’s content in-place in Python (say you want to replace certain strings)?

**Answer:**

* Option A: Read entire file into memory (`readlines()`), open file for write (`'w'`) which truncates, write modified lines back.
* Option B: Open with `'r+'`, read lines, `seek(0)`, `truncate(0)`, write back lines.
* Always account for file pointer, existing content, ensure no data loss.
* Use exception handling for robustness (FileNotFoundError, PermissionError).

### Q7. What are some challenges when handling large files in Python and how do you address them?

**Answer:**

* Memory usage: reading entire file may exhaust memory. Use streaming (`for line in f:`), chunk processing.
* File locking or concurrent writes: ensure locks or atomically write to temp file then replace.
* Performance: minimize I/O, use buffered operations, avoid unnecessary rewrites.
* Error handling: handle partial writes, restore backups, use logging.

### Q8. How do you choose between using Python built-in modules vs shell commands (via subprocess) in automation scripts?

**Answer:**

* Use built-ins when reliable, cross-platform, no shell dependency. E.g., `os`, `shutil`.
* Use `subprocess` when you need system-level commands not exposed in Python or tools only available in shell (e.g., `df`, `tar`, `grep`).
* Consider portability, error handling (shell may fail differently), security implications (shell injection).
* In DevOps context, often mix both: Python orchestration + shell utilities.

### Q9. What is the difference between `subprocess.run()` and `os.system()`?

**Answer:**

* `os.system()` runs command in shell, returns exit code, but no captured output easily and less control.
* `subprocess.run()` gives more control: you can capture output (`stdout`, `stderr`), set timeout, avoid shell injection, pass arguments as list, raise exceptions on failure (`check=True`).
* Recommended for production automation scripts for reliability.

### Q10. Provide a sample Python function that deletes files older than N days in a directory.

**Answer (example):**

```python
import os
import time

def cleanup_old_files(dir_path, days=7):
    cutoff = time.time() - (days * 86400)
    for fname in os.listdir(dir_path):
        fpath = os.path.join(dir_path, fname)
        if os.path.isfile(fpath):
            mtime = os.path.getmtime(fpath)
            if mtime < cutoff:
                os.remove(fpath)
                print(f"Deleted old file: {fpath}")
```

* Explanation: compute cutoff time, list files, check modification time (`os.path.getmtime()`), compare, delete accordingly.
* Use this in log rotation/cleanup jobs in DevOps pipelines.

---

### ✅ Tips for Interview Day

* Be ready to **explain code pieces** you write: what mode you chose (`'r'` vs `'w'` vs `'r+'`), why you used `seek()` + `truncate()`, how you handle errors.
* Relate your answers to **DevOps context**: automation scripts, CI/CD pipelines, log management, monitoring, troubleshooting.
* Show you understand both **Pythonic solutions** (built-in modules) and **practical scripting needs** (shell commands via subprocess).
* Use concise examples, but emphasize reliability, error-handling, scalability (e.g., large files, concurrency).

---
