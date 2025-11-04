#!/bin/bash

LOG=${1:-cpu.log} #default file cpu.log
echo "Logging top 5 cpu porcesses to $LOG"
echo "-----$(date)-----" >> "$LOG"

count=0
for pid in $(ps -eo pid,%cpu --sort=-%cpu | awk 'NR>1 {print $1}' | head -5)
do
	((count++))
	cpu=$(ps -p "$pid" -o %cpu=)
	name=$(ps -p "$pid" -o comm=)
	echo "$count PID: $pid | Process: $name | CPU: $cpu%" >> "$LOG"
done
echo "Done ✅"
