#!/bin/bash

set -euo pipefail

service=$1
logfile="service.log"

log() 
{
	echo "$(date) | $1" | tee -a "$logfile";
}

check_service(){	
	if systemctl is-active --quiet "$service"; then
		log "$service running"
	else
		log "$service down"
		exit 1
	fi


}
trap "log 'Script exited.'" EXIT
check_service

