#!/bin/bash
# top_cpu.sh
# Logs top 5 cpu-consuming processes

LOGFILE="cpu_top5.log"
echo "collecting cpu usage info..."

ps -eo pid,comm,%cpu --sort=-%cpu | head -6 > "$LOGFILE"

if [ $? -eq 0 ]; then
	echo "top-5 cpu consuming processes saved to $LOGFILE"
else
	echo "Failed to collect data" >&2
fi
