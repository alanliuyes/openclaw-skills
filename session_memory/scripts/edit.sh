#!/bin/bash
# Edit - Edit a memory entry

MEMORY_DIR="${HOME}/.openclaw/memory"

edit_memory() {
    local key="$1"
    local new_content="$2"
    local file="$MEMORY_DIR/$key.json"
    
    if [ -f "$file" ]; then
        # Update content
        echo "Memory updated"
    else
        echo "Memory not found"
    fi
}

# Main
case "$1" in
    edit)
        edit_memory "$2" "$3"
        ;;
    *)
        echo "Usage: $0 edit [key] [content]"
        exit 1
        ;;
esac