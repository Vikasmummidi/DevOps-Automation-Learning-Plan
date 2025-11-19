#!/bin/bash
# API simulation

import subprocess
import logging

logging.basicConfig(
        filename="api.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
        )
try:
    logging.info("api simulation started")


    out=subprocess.run(
            ["echo","API OK"],
            capture_output=True,
            text=True
            )
    if out.returncode != 0:
        logging.error("API call failed")
    else:
        logging.info(f"API Response: {out.stdout.strip()}")

except Exception as e:
    logging.error(f"Unexpeted error:{e}")

finally:
    logging.info("API simulation completed")
