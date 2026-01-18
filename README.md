<div align="center">

[![Python](https://img.shields.io/badge/Python-3.14.2-blue)]([https://www.oracle.com/java/](https://www.python.org/downloads/release/python-3142/))
[![Shell Script](https://img.shields.io/badge/Shell%20Script-green)]()

</div>

<div align="center">

[Description](#description) ·
[Requirements](#requirements) ·
[Motivation](#motivation) ·
[Roadmap](#roadmap) ·
[Installation](#installation) ·
[Uninstall](#how-to-uninstall) ·
[Contribute](#contribute)
</div>

<img width="1616" height="856" alt="image" src="https://github.com/user-attachments/assets/76f59e00-ae6e-4780-a693-20d0fdc5d884" />


# bitcoin-dca
Bitcoin Dollar Cost Averaging Script

# Description

This script has been built using Shell Script and Python. The main goal is to automate the process of buying this asset on Binance through the `cron` service , which is typically a native service on Linux-based systems.

# Requirements
- Python 3.14.2 && python3.12-venv
- Linux environment
- Cron service

# Motivation

This script was built primarily to run on a Linux-based system alongside the cron service, such as a VPS, Raspberry Pi, or server, where it can run continuously.

## Why Python and Shell Script ?

- Simplicity
- Low resource consumption
- Ideal for VPSs and Raspberry Pi devices
- More flexibility and control over your orders and logs

# Roadmap

Below are the upcoming planned features:

- **Implement a Telegram bot**: This bot will notify the user of the current operation status when the script runs.
- **Update the API authentication method**: Migrate from HMAC (current method) to __Ed25519__ , which provides a more secure communication mechanism.

It's possible to track this roadmap in the `issues` tab.

# Installation

Before running `setup.sh`, ensure that the cron service is installed and enabled on your system.

## Debian / Ubuntu (apt)

```bash
sudo apt update -y && \
sudo apt install cron && \
sudo systemctl enable cron && \
sudo systemctl start cron
```

## Fedora (dnf)

```bash
sudo dnf update -y && \
sudo dnf install cronie -y && \
sudo systemctl enable crond && \
sudo systemctl start crond
```

## Arch (pacman)
```bash
sudo pacman -Syu --noconfirm && \
sudo pacman -S cronie --noconfirm && \
sudo systemctl enable cronie && \
sudo systemctl start cronie
```

## How to execute

1- Execution permission for setup.sh
```bash
chmod +x ./setup.sh
```

2- Execute the setup shell script

```bash
sudo ./setup.sh
```

# How to uninstall

```
chmod +x ./uninstall.sh && sudo ./uninstall.sh
```

# Contribute

If you wish to contribute to this script, you're more than welcome. 

Before you start it is __mandatory__ that you understand how the project structure works.

Below are the main directories and files you must be familiar with:

- `/etc/cron.d/`: Directory repsonsible for storing all schedules jobs.
- `/var/log/bitcoindca/`: Directory responsible for storing execution logs of this script, including all operations and their statuses.
- `/etc/default/bitcoindca/`: Directory responsible for storing the Binance API secrets.
    - __The secret file is stored with `600` permissions and is acessible only by the root user.__


