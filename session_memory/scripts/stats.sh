#!/bin/bash
# Stats - Memory statistics

MEMORY_DIR="${HOME}/.openclaw/memory"

show_stats() {
    local total=$(ls -1 "$MEMORY_DIR"/*.json 2>/dev/null | wc -l)
    local size=$(du -sh "$MEMORY_DIR" 2>/dev/null | cut -f1)
    
    echo "Memory Statistics:"
    echo "  Total entries: $total"
    echo "  Total size: $size"
}

# Main
show_stats