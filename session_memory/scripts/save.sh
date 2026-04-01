#!/bin/bash
# Save - Save context to memory

MEMORY_DIR="${HOME}/.openclaw/memory"
mkdir -p "$MEMORY_DIR"

save_context() {
    local context="$1"
    local importance="${2:-normal}"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local hash=$(echo "$context" | md5sum | cut -d' ' -f1)
    local file="$MEMORY_DIR/$hash.json"
    
    cat > "$file" <<EOF
{
  "context": "$context",
  "importance": "$importance",
  "timestamp": "$timestamp",
  "hash": "$hash"
}
EOF
    echo "Context saved: $hash"
}

# Main
case "$1" in
    save)
        save_context "$2" "$3"
        ;;
    *)
        echo "Usage: $0 save [context] [importance]"
        exit 1
        ;;
esac