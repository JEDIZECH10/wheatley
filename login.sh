#!/bin/bash
clear
echo -e "\e[1;37mAPERTURE SCIENCE BIOS (C) 1982\e[0m"
sleep 0.5
echo "MEM TEST: 640K OK"
echo "BOOTING FROM CLOUD_SERVER..."
sleep 1

echo -n "LOGIN: "
read username
echo -n "PASSWORD: "
read -s password
echo -e "\n\n\e[1;36mCONNECTED TO APERTURE MAIN-FRAME\e[0m"
echo "--------------------------------"
echo "1. ACTIVATE GLaDOS"
echo "2. ACTIVATE WHEATLEY"
echo -n "SELECTION: "
read choice

if [ "$choice" == "2" ]; then
    echo -e "\n\e[1;34m[WHEATLEY CORE LOADED]\e[0m"
    echo "Stuttering initialized..."
    sleep 1
    python wheatley.py
else
    echo -e "\n\e[1;33m[GLaDOS CORE LOADED]\e[0m"
    echo "Testing will begin shortly."
fi
