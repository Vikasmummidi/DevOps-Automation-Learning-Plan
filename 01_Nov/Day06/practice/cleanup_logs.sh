#!/bin/bash
#cleanup_logs.sh
#Delete log files older than 7days


LOG_DIR="/var/log"
DAYS=7
DATE=$(date '+%F')
LOG_FILE="/tmp/log_cleanup_$DATE.log"

echo "Starting cleanup: $(date)" > "$LOG_FILE"
find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -print -delete >> "$LOG_FILE" 2>&1
echo "Cleanup completed on $(date)" >> "$LOG_FILE"
