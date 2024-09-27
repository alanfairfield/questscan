#!/bin/bash

# ASCII art for visual appeal
echo "              /|"
echo "             / |"
echo "            /  |"
echo "           /___|___"
echo "          //\"\"\"\"\"\"\"\\\\"
echo "         //         \\\\"
echo "        //           \\\\"
echo "       //             \\\\"
echo "      //               \\\\"
echo "     //                 \\\\"
echo "    //                   \\\\"
echo "   //                     \\\\"
echo "  //_______________________\\\\"
echo "  \\_________________________/"
echo "                           O"
echo "                           |"
echo "                           |"
echo "                           |"
echo "                           |"
echo "                          / \\"
echo "                         /   \\"
echo "                        /     \\"

# ASCII art to separate commands
echo "####################################"

# Initiate Firewall
echo -e "\033[0;32mInitiating Firewall...\033[0m"
sudo ufw status
echo -e "\033[0;32mFirewall initiated!\033[0m"
echo "----------------------------"

# ASCII art to separate commands
echo "####################################"

# Check self for open ports
echo -e "\033[0;32mChecking for open ports...\033[0m"
sudo nmap -p0-65535 127.0.0.1
echo -e "\033[0;32mOpen ports check complete!\033[0m"
echo "----------------------------"

# ASCII art to separate commands
echo "####################################"

# Run logwatch
echo -e "\033[0;32mRunning logwatch...\033[0m"
sudo logwatch
echo -e "\033[0;32mLogwatch complete!\033[0m"
echo "----------------------------"

# ASCII art to separate commands
echo "####################################"

# Monitor important system logs
echo -e "\033[0;32mMonitoring important system logs...\033[0m"
echo -e "\033[0;32mSSH Login attempts:\033[0m"
sudo tail -n 50 /var/log/auth.log | grep 'sshd'
echo "----------------------------"
echo -e "\033[0;32mFailed SSH login attempts:\033[0m"
sudo tail -n 50 /var/log/auth.log | grep 'sshd.*Failed'
echo "----------------------------"
echo -e "\033[0;32mLast 10 system reboots:\033[0m"
last -x | head
echo -e "\033[0;32mDisk usage:\033[0m"
df -h | grep -v tmpfs
echo -e "\033[0;32mDisk errors:\033[0m"
sudo tail -n 50 /var/log/syslog | grep -i 'error\|fail\|fatal'
echo -e "\033[0;32mLogs monitoring complete!\033[0m"
echo "----------------------------"

# ASCII art to separate commands
echo "####################################"

# Prompt user to initiate virus scan
read -p "Do you want to initiate a virus scan? (Y/n)" choice
case "$choice" in 
  [yY] | "" )
    # Run virus scan
    echo -e "\033[0;32mScanning for malware...\033[0m"
    sudo freshclam && sudo clamscan -r /home
    ;;
  [nN] )
    # Don't run virus scan
    echo -e "\033[0;32mSkipping virus scan.\033[0m"
    ;;
  * )
    # Invalid input
    echo -e "\033[0;31mInvalid input, skipping virus scan.\033[0m"
    ;;
esac
