#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
  echo "You must run as sudo"
  exit 1
fi

set -e 

APP_DESCRIPTION="Bitcoin DCA"
APP_NAME="bitcoindca"
OPT_DIR="/opt/$APP_NAME"
VENV_PATH="$OPT_DIR/venv"
LOG_DIR="/var/log/$APP_NAME"
SECRETS_DIR="/etc/default/$APP_NAME"

echo "Installing $APP_DESCRIPTION..."

# Create directories
mkdir -p "$OPT_DIR"
mkdir -p "$LOG_DIR"
mkdir -p "$SECRETS_DIR"

# Copy all scripts to the /opt
cp -r schedule/ "$OPT_DIR"
cp requirements.txt "$OPT_DIR"
cp uninstall.sh "$OPT_DIR"
cp settings.yaml "$OPT_DIR"

# Create a venv
python3 -m venv "$VENV_PATH" || {
    echo "[ERROR] Creating venv failed. Fix the issue and try again.";
    exit 1;
}

# Install dependencies
"$VENV_PATH/bin/pip" install -r "$OPT_DIR/requirements.txt" || {
    echo "[ERROR] Installing dependencies failed. Fix the issue and try again.";
    exit 1;
}

cd "$OPT_DIR" && ./venv/bin/python -m schedule.service.cron_setup || {
    echo "[ERROR] Running cron_setup.py failed. Fix the issue and try again."
    exit 1
}

exit 0