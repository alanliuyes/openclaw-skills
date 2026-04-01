#!/bin/bash
# Export - Export memories

MEMORY_DIR="${HOME}/.openclaw/memory"

export_memories() {
    local format="${1:-json}"
    local output="${2:-export}"
    
    if [ "$format" = "json" ]; then
        # Export as JSON
        cat "$MEMORY_DIR"/*.json > "$output.json"
    fi
    
    echo "Exported to $output.$format"
}

# Main
case "$1" in
    export)
        export_memories "$2" "$3"
        ;;
    *)
        echo "Usage: $0 export [format] [filename]"
        exit 1
        ;;
esac