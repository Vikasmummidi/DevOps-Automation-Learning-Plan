#!/bin/bash
# CPU Monitor script
set -euo pipefail

THRESHOLD=80
LOGFILE="/tmp/cpu_monitor_$(date '+%F').log"

# Function: reliably get CPU idle percentage (supports different top formats)
get_cpu_idle() {
  top -bn1 | grep "Cpu(s)" \
    | awk 'match($0, /([0-9]+(\.[0-9]+)?) *id/, a) { print a[1]; exit }'
}

echo "=== CPU Monitor started at $(date) ===" | tee -a "$LOGFILE"

cpu_idle=$(get_cpu_idle)
if [[ -z "${cpu_idle:-}" ]]; then
  echo "[ERROR] Could not determine cpu_idle" | tee -a "$LOGFILE"
  exit 2
fi

cpu_used=$(echo "scale=1; 100 - $cpu_idle" | bc)

echo "Current CPU usage: ${cpu_used}%" | tee -a "$LOGFILE"

echo "Top 5 CPU-consuming processes:" | tee -a "$LOGFILE"
ps -eo pid,comm,%cpu --sort=-%cpu | head -6 | tee -a "$LOGFILE"

cpu_used_int=${cpu_used%.*}

# 🔽 Trigger when CPU usage is BELOW the threshold
if (( cpu_used_int < THRESHOLD )); then
    echo "[ALERT] CPU usage below threshold (${THRESHOLD}%) - ${cpu_used}%" | tee -a "$LOGFILE"

    echo "NOTICE: CPU usage is ${cpu_used}% on $(hostname) at $(date)" \
      | mail -s "ℹ️ LOW CPU ALERT on $(hostname) - ${cpu_used}% used" vikasmummidi@gmail.com

    exit 1
else
    echo "[OK] CPU usage above threshold (${THRESHOLD}%) - ${cpu_used}%" | tee -a "$LOGFILE"
    exit 0
fi

