#!/bin/bash
#CPU Monitor script
set -euo pipefail

THRESHOLD=80
LOGFILE="/tmp/cpu_monitor_$(date '+%F').log"

echo "=== CPU Monitor started at $(date) ===" | tee -a "$LOGFILE"
cpu_idle=$(top -bn1 | grep "Cpu(s)" | sed 's/,/ /g' | awk '{for(i=1;i<=NF;i++) if($i ~ /id/) print $(i-1)}')
cpu_used=$(echo "scale=1; 100 - $cpu_idle" | bc)

echo "Current cpu usage: ${cpu_used}%" | tee -a "$LOGFILE"

echo "Top 5 cpu consuming porcesses:" | tee -a "$LOGFILE"
ps -eo pid,comm,%cpu --sort=-%cpu | head -6 | tee -a "$LOGFILE"

cpu_used_int=${cpu_used%.*}

if [[ $cpu_used_int -gt $THRESHOLD ]]; then
	echo "[ALERT] cpu usage  above threshold ($THRESHOLD%)" | tee -a "$LOGFILE"
	exit 1
else
	echo "[OK] cpu usage below threshold ($THRESHOLD%)" | tee -a "$LOGFILE"
	exit 0
fi
if [[ $cpu_used_int -lt $THRESHOLD ]]; then
    echo "CPU alert: $cpu_used%" | mail -v -s "High CPU Alert" vikasmummidi@gmail.com
fi
