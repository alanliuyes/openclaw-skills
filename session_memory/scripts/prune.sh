#!/bin/bash
# Prune - Remove old memories

MEMORY_DIR="${HOME}/.openclaw/memory"

prune_memories() {
    local days="${1:-30}"
    
    # Remove memories older than N days
    find "$MEMORY_DIR" -name "*.json" -mtime +$days -delete
    
    echo "Pruned memories older than $days days"
}

# Main
case "$1" in
    prune)
        prune_memories "$2"
        ;;
    *)
        echo "Usage: $0 prune [days]"
        exit 1
        ;;
esac