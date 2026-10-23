#!/bin/bash
# Start the Skype-Matrix Bridge

set -e

echo "⌬ Skype-Matrix Bridge"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo "Installing required Python packages..."
python3 -m pip install --quiet matrix-nio aiohttp websockets

echo ""
echo "Checking Matrix homeserver configuration..."
echo ""

# Prompt for Matrix configuration if not provided
if [ -z "$MATRIX_HOMESERVER" ]; then
    read -p "Matrix homeserver URL (e.g., https://matrix.org): " MATRIX_HOMESERVER
fi

if [ -z "$MATRIX_USER" ]; then
    read -p "Matrix username (e.g., @user:matrix.org): " MATRIX_USER
fi

if [ -z "$MATRIX_PASSWORD" ]; then
    read -s -p "Matrix password: " MATRIX_PASSWORD
    echo ""
fi

echo ""
echo "Starting bridge on http://127.0.0.1:8080"
echo "Matrix homeserver: $MATRIX_HOMESERVER"
echo "Matrix user: $MATRIX_USER"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Start the bridge
python3 bridge.py \
    --matrix-homeserver "$MATRIX_HOMESERVER" \
    --matrix-user "$MATRIX_USER" \
    --matrix-password "$MATRIX_PASSWORD" \
    --port 8080
