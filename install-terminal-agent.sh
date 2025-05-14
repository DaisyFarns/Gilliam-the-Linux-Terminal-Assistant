#!/bin/bash

# Disable history expansion in Bash
set +H

AGENT_NAME="terminal-agent"
INSTALL_DIR="$HOME/.config/$AGENT_NAME"
SCRIPT_PATH="$INSTALL_DIR/$AGENT_NAME.py"
SYMLINK_PATH="/usr/local/bin/$AGENT_NAME"

function install_agent() {
    echo "[*] Installing $AGENT_NAME..."

    # Step 1: Create hidden install directory
    mkdir -p "$INSTALL_DIR"

    # Step 2: Copy the python file to the install directory
    cp "terminal-agent.py" "$SCRIPT_PATH"

    # There's some cleaver stuff with Python's virtual environments
    # that could be done here.

    chmod +x "$SCRIPT_PATH"

    # Step 3: Symlink to /usr/local/bin
    if [ -L "$SYMLINK_PATH" ]; then
        echo "[*] Removing existing symlink..."
        sudo rm "$SYMLINK_PATH"
    fi

    echo "[*] Creating symlink..."
    sudo ln -s "$SCRIPT_PATH" "$SYMLINK_PATH"

    echo "[✓] Installation complete! You can now run it using:"
    echo "    $AGENT_NAME"
}

# Auto-detect if not already running from saved file
if [[ "$(basename "$0")" != "install-terminal-agent.sh" ]]; then
    TMP_SCRIPT="/tmp/install-terminal-agent.sh"
    tail -n +1 "$0" > "$TMP_SCRIPT" # Write this file to another file...
    chmod +x "$TMP_SCRIPT"
    exec "$TMP_SCRIPT"  # Execute this new file, which is also the old file?
    # Not sure what this achieves :3
else
    install_agent
