#!/bin/bash
set -e

# Ensure pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Installing pip..."
    apt-get update -qq && apt-get install -y -qq python3-pip > /dev/null
fi

# Install dependencies (using --break-system-packages for Docker container)
echo "Installing Python dependencies..."
pip3 install --break-system-packages -q -r requirements.txt

# Run pytest with all provided arguments
echo "Running tests..."
exec python3 -m pytest "$@"
