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
sudo apt install figlet
figlet -e big "     SETUP"
#install 
#$1 apt or sudo
sudo apt install apache2
sudo apt install php
sudo apt install python3-pip
pip3 install colorama
pip3 install requests
pip3 install shutil
chmod +x main.py
echo "setup completed!"
sleep 2 
figlet -f big "YAF"
sleep 1 
clear;
