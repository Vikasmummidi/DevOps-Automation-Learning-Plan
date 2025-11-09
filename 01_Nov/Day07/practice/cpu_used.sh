#!/bin/bash

cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}' | cut -d. -f1)
cpu_used=$((100 - $cpu_idle))
echo "CPU Usage: $cpu_used%"
