#!/bin/bash

echo "Removing secret files"
sudo rm -rf /etc/default/btcdca/

echo "Removing log files"
sudo rm -rf /var/log/bitcoindca/

echo "Removing script file"
sudo rm -f /usr/local/bin/dca_operation.py

echo "Removing crontab file"
sudo rm -f /etc/cron.d/bitcoin.*

echo "Removing virtual env python"
sudo rm -rf /opt/bitcoind-dca/