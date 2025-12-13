#!/bin/bash

# Create a venv
sudo python3 -m venv /opt/bitcoind-dca/venv

# Install dependencies
sudo /opt/bitcoind-dca/venv/bin/pip install -r ./requirements.txt

# cron-setup permission
chmod +x ./cron_setup.py

# Run cron_setup
sudo ./cron_setup.py