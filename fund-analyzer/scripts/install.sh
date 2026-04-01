#!/bin/bash
# Fund Analyzer Setup Script

echo "Setting up Fund Analyzer..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed."
    exit 1
fi

# Install dependencies
pip3 install requests

echo "Fund Analyzer setup complete!"