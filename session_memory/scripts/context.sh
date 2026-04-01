#!/bin/bash
# Context - Load session context

MEMORY_DIR="${HOME}/.openclaw/memory"

load_context() {
    local session="$1"
    # Load context for session
    cat "$MEMORY_DIR/$session.json" 2>/dev/null || echo "No context found"
}

# Main
case "$1" in
    load)
        load_context "$2"
        ;;
    *)
        echo "Usage: $0 load [session_id]"
        exit 1
        ;;
esac