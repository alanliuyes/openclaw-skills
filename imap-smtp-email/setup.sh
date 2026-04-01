#!/bin/bash
# Setup script for imap-smtp-email skill

echo "Setting up IMAP/SMTP Email Skill..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Install dependencies
cd "$(dirname "$0")/.."
npm install imap mailparser nodemailer

echo "Setup complete!"