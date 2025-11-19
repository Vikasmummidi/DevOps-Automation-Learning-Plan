#!/usr/bin/env python3
#task-3

import logging

logging.basicConfig(
        filename = "run.log",
        level = logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )
logging.info("script started")

try:
    with open("sample.txt") as f:
        data=f.read()
    logging.info("file read successfully")

except Exception as e:
    logging.error(f"Error reading file {e}")
finally:
    logging.info("script completed")
