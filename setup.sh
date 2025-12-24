#!/bin/bash

VENV_PATH="/opt/bitcoind-dca/venv"

# Create a venv
sudo python3 -m venv "$VENV_PATH" || {
    echo "[ERROR] Creating venv failed. Fix the issue and try again.";
    exit 1;
}

# Install dependencies
"$VENV_PATH/bin/pip" install -r ./requirements.txt || {
    echo "[ERROR] Installing dependencies failed. Fix the issue and try again.";
    exit 1;
}

# Run the configuration setup (Monthly, weekly, and the amount to invest)
sudo "$VENV_PATH/bin/python" ./cron_setup.py || {
    echo "[ERROR] Running cron_setup.py failed. Fix the issue and try again."
    exit 1;
}

echo "[INFO] Setup completed successfully.";