#!/bin/bash
# Memory - Core memory operations

MEMORY_DIR="${HOME}/.openclaw/memory"

# Ensure directory exists
mkdir -p "$MEMORY_DIR"

# Function to save memory
save_memory() {
    local content="$1"
    local key=$(echo "$content" | md5sum | cut -d' ' -f1)
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local file="$MEMORY_DIR/$key.json"
    
    cat > "$file" <<EOF
{
  "content": "$content",
  "timestamp": "$timestamp",
  "key": "$key"
}
EOF
    echo "Memory saved: $key"
}

# Function to list memories
list_memories() {
    ls -1 "$MEMORY_DIR" | while read file; do
        cat "$MEMORY_DIR/$file"
    done
}

# Main command handler
case "$1" in
    save)
        save_memory "$2"
        ;;
    list)
        list_memories
        ;;
    *)
        echo "Usage: $0 {save|list} [content]"
        exit 1
        ;;
esac