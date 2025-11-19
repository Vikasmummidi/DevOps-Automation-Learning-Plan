#!/usr/bin/env python3
#monitor_disk.py

import subprocess
import logging

logging.basicconfig(
        filename = "monitor.log",
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s"
        )

def get_disk_usage():
    try:
        cmd = "df -h / | tail -1 | awk '{print $5}' | sed 's/%//'"
        out = subprocess.run(cmd, capture_output=True, text = True)

        If out.returncode != 0:
            logging.error("Failed to execute df command")
            return None
        return int(out.stdout.strip())

    except Exception as e:
        logging.error(f"Error parsing disk usage: {e}")
        return None

usage = get_disk_usage()

if usage is not None:
    logging.info(f"Disk usage: {usage}%")

    if usage>80:
        logging.warning(f"High disk usage is detected: {usage}%"}

else:
    logging.error("Disk usage couldn't be determined")

