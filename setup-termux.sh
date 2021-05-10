#!/bin/sh
echo "
                        ▄██   ▄      ▄████████    ▄████████ 
                        ███   ██▄   ███    ███   ███    ███ 
                        ███▄▄▄███   ███    ███   ███    █▀  
                        ▀▀▀▀▀▀███   ███    ███  ▄███▄▄▄     
                        ▄██   ███ ▀███████████ ▀▀███▀▀▀     
                        ███   ███   ███    ███   ███        
                        ███   ███   ███    ███   ███        
                         ▀█████▀    ███    █▀    ███ 
"
sleep 2
clear
figlet -f big "     SETUP"
#install 

pkg install apache2
pkg install php
pkg install python
pip install colorama
pip install bs4
pip install requests
pip install shutil
chmod +x main.py
echo "setup completed!"
sleep 2 
figlet -f big "YAF"
sleep 1 
clear;
python main.py
