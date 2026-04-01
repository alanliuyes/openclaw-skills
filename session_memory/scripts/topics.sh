#!/bin/bash
# Topics - Extract topics from memory

MEMORY_DIR="${HOME}/.openclaw/memory"

extract_topics() {
    # Simple keyword extraction
    grep -oE '[A-Z]{2,}' "$MEMORY_DIR"/*.json 2>/dev/null | sort | uniq -c | sort -rn | head -20
}

# Main
extract_topics