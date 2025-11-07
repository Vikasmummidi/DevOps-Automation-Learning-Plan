#!/bin/bash
#backup_logs.sh
#compress recent logs into a backup file.



SOURCE_DIR="/var/log"
BACKUP_DIR="/backup"	
DATE=$(date '+%F')
BACKUP_FILE="$BACKUP_DIR/logs_backup_$DATE.tar.gz"

mkdir -p "$BACKUP_DIR"


echo "starting backup at $(date)"
tar -zcf "$BACKUP_FILE" "$SOURCE_DIR"/*.log 2>/dev/null
echo "Backup complete: $BACKUP_FILE"
