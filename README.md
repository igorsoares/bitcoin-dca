<div align="center">

[![Python](https://img.shields.io/badge/Python-3.14.2-blue)]([https://www.oracle.com/java/](https://www.python.org/downloads/release/python-3142/))
[![Shell Script](https://img.shields.io/badge/Shell%20Script-green)]()

</div>

# bitcoin-dca
Bitcoin Dollar Cost Averaging script

# Requirements
- Python 3.14.2
- Linux environment
- Cron service

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

