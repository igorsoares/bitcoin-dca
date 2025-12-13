# bitcoin-dca
Bitcoin DCA via Binance API

# Requirements
- Python3
- Linux environment
- Cron service (apt install cron)

If you're on a Debian / Ubuntu based: 

```
sudo apt update -y && \
sudo apt install cron && \
sudo systemctl enable cron && \
sudo systemctl start cron
```

# Structure

<img width="1349" height="722" alt="Imagem colada (2)" src="https://github.com/user-attachments/assets/0956a61c-b3d1-4584-a224-a327c250cd87" />

# How to execute

First give a execution permission for setup.sh
```
chmod +x ./setup.sh
```

Then execute the setup shell script
``` 
sudo ./setup.sh
```

<img width="935" height="461" alt="Imagem colada" src="https://github.com/user-attachments/assets/00ab08a4-a437-49eb-96d8-4a526eb8f5ef" />


# How to uninstall

```
chmod +x ./uninstall.sh && sudo ./uninstall.sh
```

