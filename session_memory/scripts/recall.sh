#!/bin/bash
# Recall - Recall memories with relevance scoring

MEMORY_DIR="${HOME}/.openclaw/memory"

recall_memory() {
    local query="$1"
    local results=()
    
    # Simple relevance matching
    for file in "$MEMORY_DIR"/*.json; do
        if [ -f "$file" ]; then
            if grep -q "$query" "$file" 2>/dev/null; then
                results+=("$file")
            fi
        fi
    done
    
    # Output results
    for file in "${results[@]}"; do
        cat "$file"
        echo "---"
    done
}

# Main
case "$1" in
    search)
        recall_memory "$2"
        ;;
    *)
        echo "Usage: $0 search [query]"
        exit 1
        ;;
esac