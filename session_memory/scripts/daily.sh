#!/bin/bash
# Daily - Daily memory operations

MEMORY_DIR="${HOME}/.openclaw/memory"

daily_report() {
    local today=$(date +%Y-%m-%d)
    echo "Daily Report for $today:"
    
    # Count today's memories
    find "$MEMORY_DIR" -name "*.json" -newermt "$today" | wc -l
}

# Main
daily_report