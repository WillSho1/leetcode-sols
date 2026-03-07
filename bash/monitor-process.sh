#!/bin/bash
# Category: Bash/Process Management
# Task: Monitor a process by name. If it's not running, start it. Log the event.

PROCESS_NAME=$1
LOG_FILE="/tmp/process_monitor.log"

if [ -z "$PROCESS_NAME" ]; then
    echo "Usage: $0 <process_name>"
    exit 1
fi

if pgrep "$PROCESS_NAME" > /dev/null; then
    echo "$(date): $PROCESS_NAME is running." >> "$LOG_FILE"
else
    echo "$(date): $PROCESS_NAME is NOT running. Attempting to restart..." >> "$LOG_FILE"
    # Example: systemctl start "$PROCESS_NAME"
    # For drill purposes, we just log the intent.
    echo "$(date): Restart triggered for $PROCESS_NAME" >> "$LOG_FILE"
fi
