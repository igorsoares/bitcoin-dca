#!/bin/bash

echo "Removing secret files"
sudo rm -rf /etc/default/bitcoindca/

echo "Removing log files"
sudo rm -rf /var/log/bitcoindca/

echo "Removing Bitcoin DCA folder"
sudo rm -rf /opt/bitcoindca/

echo "Removing crontab file"
sudo rm -f /etc/cron.d/bitcoin

echo "Bitcoin DCA was successfully removed."