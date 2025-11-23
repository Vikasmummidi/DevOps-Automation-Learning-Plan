

# Solution files

---

## `config.json` (single-path)

```json
{
  "path": "/",
  "threshold": 70,
  "email_alert": false,
  "report_file": "report.json",
  "log_file": "monitor.log"
}
```

---

## `config_multi.json` (multiple paths)

```json
{
  "paths": [
    { "path": "/", "threshold": 70 },
    { "path": "/var", "threshold": 80 }
  ],
  "email_alert": false,
  "report_file": "report_multi.json",
  "log_file": "monitor_multi.log"
}
```

---

## `disk_monitor.py` (complete solution)

```python
#!/usr/bin/env python3
"""
disk_monitor.py

- Loads JSON config safely
- Validates keys
- Checks disk usage using shutil.disk_usage()
- Optionally runs `df -h` and parses output using subprocess
- Writes a JSON report and logs events
"""

import json
import os
import sys
import shutil
import logging
import argparse
import subprocess
from typing import Dict, Any, List, Optional

# -------------------------
# Utilities: JSON + config
# -------------------------
def load_config(file_path: str, required_keys: Optional[List[str]] = None) -> Optional[Dict[str, Any]]:
    """Safely load JSON config file and validate required keys (if provided)."""
    if not os.path.exists(file_path):
        logging.error("Config file not found: %s", file_path)
        return None

    try:
        with open(file_path, "r") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        logging.error("Invalid JSON in %s: %s", file_path, e)
        return None
    except Exception as e:
        logging.error("Could not read config %s: %s", file_path, e)
        return None

    if required_keys:
        for k in required_keys:
            # For multi-path config, required top-level key might be 'paths' OR 'path'
            if k not in config:
                logging.error("Missing required key '%s' in config", k)
                return None

    return config

# -------------------------
# Disk usage helpers
# -------------------------
def check_disk_usage(path: str) -> float:
    """
    Returns percentage of used disk space for the file system containing `path`.
    Result is a float between 0-100.
    """
    usage = shutil.disk_usage(path)
    total, used = usage.total, usage.used
    if total == 0:
        return 0.0
    percent_used = (used / total) * 100.0
    return round(percent_used, 2)

# -------------------------
# Subprocess helper (optional)
# -------------------------
def df_line_for_path(path: str) -> Optional[str]:
    """
    Runs `df -h` and returns the full line for the mount that contains `path`.
    Returns None on error.
    """
    try:
        result = subprocess.run(["df", "-h", path], capture_output=True, text=True, check=True)
        # The output usually has header + one line for the path
        lines = [line for line in result.stdout.splitlines() if line.strip()]
        if len(lines) >= 2:
            return lines[1].strip()
        elif len(lines) == 1:
            return lines[0].strip()
        return None
    except subprocess.CalledProcessError as e:
        logging.debug("df command failed: %s", e)
        return None
    except FileNotFoundError:
        # df not found on some systems (very rare). Ignore gracefully.
        logging.debug("df command not available on this system.")
        return None

# -------------------------
# Core logic
# -------------------------
def build_report_for_single(config: Dict[str, Any]) -> Dict[str, Any]:
    path = config.get("path", "/")
    threshold = float(config.get("threshold", 80))
    percent_used = check_disk_usage(path)

    status = "OK" if percent_used < threshold else "ALERT"
    df_line = df_line_for_path(path)

    report = {
        "path": path,
        "threshold": threshold,
        "current_usage_percent": percent_used,
        "status": status,
        "df_line": df_line
    }
    return report

def build_report_for_multiple(config: Dict[str, Any]) -> Dict[str, Any]:
    report_list = []
    paths = config.get("paths", [])
    for entry in paths:
        p = entry.get("path", "/")
        thr = float(entry.get("threshold", 80))
        used = check_disk_usage(p)
        status = "OK" if used < thr else "ALERT"
        report_list.append({
            "path": p,
            "threshold": thr,
            "current_usage_percent": used,
            "status": status,
            "df_line": df_line_for_path(p)
        })
    return {"results": report_list}

# -------------------------
# Logging and output
# -------------------------
def setup_logging(log_file: Optional[str] = None):
    if log_file:
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s",
                            handlers=[logging.FileHandler(log_file), logging.StreamHandler()])
    else:
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")

def write_report(report: Dict[str, Any], path: str):
    try:
        with open(path, "w") as f:
            json.dump(report, f, indent=2)
        logging.info("Report written to %s", path)
    except Exception as e:
        logging.error("Failed to write report to %s: %s", path, e)

# -------------------------
# CLI / main
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="Disk Usage Checker & JSON Parser")
    parser.add_argument("-c", "--config", default="config.json", help="Path to config JSON")
    args = parser.parse_args()

    # Minimal top-level required key(s) - accept either single 'path' or 'paths' for multi.
    # We'll validate presence in code below.
    config = load_config(args.config)
    if config is None:
        print("Configuration load failed. Exiting.")
        sys.exit(1)

    # Setup logging file if present in config
    log_file = config.get("log_file")
    setup_logging(log_file)

    # Determine single vs multiple
    if "paths" in config:
        # Multi-path mode
        logging.info("Running in multi-path mode")
        report = build_report_for_multiple(config)
        report_file = config.get("report_file", "report_multi.json")
    elif "path" in config:
        # Single-path mode
        logging.info("Running in single-path mode")
        # Basic validation of required keys
        if "threshold" not in config:
            logging.error("Required key 'threshold' missing in single-path config.")
            sys.exit(1)
        report = build_report_for_single(config)
        report_file = config.get("report_file", "report.json")
    else:
        logging.error("Config must contain either 'path' or 'paths'.")
        sys.exit(1)

    # Log results and write report
    logging.info("Report summary: %s", json.dumps(report, indent=2))
    write_report(report, report_file)

    # Set exit code: 0 if all OK, 2 if any ALERT (custom convention)
    any_alert = False
    if "results" in report:
        any_alert = any(r.get("status") == "ALERT" for r in report["results"])
    else:
        any_alert = report.get("status") == "ALERT"

    if any_alert:
        logging.warning("One or more paths exceeded threshold.")
        sys.exit(2)
    else:
        logging.info("All paths are within thresholds.")
        sys.exit(0)

if __name__ == "__main__":
    main()
```

---

# How to run & expected behavior

1. Put `disk_monitor.py` + `config.json` in the same folder.
2. Make the script executable:

```bash
chmod +x disk_monitor.py
```

3. Run:

```bash
./disk_monitor.py -c config.json
```

**Exit codes used:**

* `0` → everything OK
* `2` → at least one path exceeded threshold (custom choice, different from `1` used for config errors)
* `1` → config load/validation error

**Sample log lines:**

```
2025-11-20 09:12:01,123 - INFO - Running in single-path mode
2025-11-20 09:12:01,124 - INFO - Report summary: {
  "path": "/",
  "threshold": 70.0,
  "current_usage_percent": 63.21,
  "status": "OK",
  "df_line": "Filesystem      Size  Used Avail Use% Mounted on"
}
2025-11-20 09:12:01,125 - INFO - Report written to report.json
```

**report.json sample (single):**

```json
{
  "path": "/",
  "threshold": 70.0,
  "current_usage_percent": 63.21,
  "status": "OK",
  "df_line": "..."
}
```

**report_multi.json sample:**

```json
{
  "results": [
    {"path": "/", "threshold": 70.0, "current_usage_percent": 63.21, "status": "OK", "df_line": "..."},
    {"path": "/var", "threshold": 80.0, "current_usage_percent": 82.12, "status": "ALERT", "df_line": "..."}
  ]
}
```

---

# Notes & improvements you can try (stretch)

* Replace `logging.FileHandler` with `RotatingFileHandler` for large logs.
* Add email alerting (using `smtplib` or system `mail`) when `email_alert` is true.
* Add retry/backoff when reading network-mounted filesystems (NFS) that may intermittently fail.
* Add unit tests for `check_disk_usage()` using `unittest.mock` to fake `shutil.disk_usage`.
* Add Prometheus exporter or a simple HTTP endpoint that returns JSON report for integration with monitoring systems.

---
