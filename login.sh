#!/bin/bash
clear
# Colors
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

echo -e "${WHITE}APERTURE SCIENCE MULTI-CORE BOOTLOADER v2.0.4${NC}"
echo "--------------------------------------------------"

# Hardware Scan Animation
tasks=("INITIALIZING RAM" "CHECKING CORE RAILS" "VULNERABILITY SCAN" "CALIBRATING PERSONALITY DRIVERS")
for task in "${tasks[@]}"; do
    echo -ne " > $task... "
    sleep 0.4
    echo -e "${CYAN}[OK]${NC}"
done

# Progress Bar
echo -ne "\nLOADING APERTURE OS: [                    ] 0%"
for i in {1..20}; do
    sleep 0.1
    echo -ne "\rLOADING APERTURE OS: ["
    for j in $(seq 1 $i); do echo -ne "#"; done
    for j in $(seq $i 19); do echo -ne " "; done
    echo -ne "] $((i * 5))%"
done
echo -e "\n\n${WHITE}BOOT COMPLETE.${NC}"
sleep 0.5

# Login
echo -e "--- SECURITY CHECK ---"
read -p "APERTURE ID: " user
if [ "$user" != "chell" ]; then
    echo -e "\n\033[0;31m[!] WARNING: UNAUTHORIZED USER DETECTED.\033[0m"
    echo -e "\033[0;31mRecording biometric data for testing records...\033[0m\n"
    sleep 1
fi

# Pass control to the OS Shell
python3 /workspaces/wheatley/aperture_os.py
