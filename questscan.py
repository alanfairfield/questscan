#!/bin/bash

print_ascii_art() {
    cat << "EOF"
                      _
  __ _ _   _  ___ ___| |_ ___  ___ __ _ _ __
 / _` | | | |/ _ / __| __/ __|/ __/ _` | '_ \
| (_| | |_| |  __\__ | |_\__ | (_| (_| | | | |
 \__, |\__,_|\___|___/\__|___/\___\__,_|_| |_|
    | |
    \_\
EOF
}

is_ipv6() {
    if [[ $1 =~ .*:.* ]]; then
        return 0 # is IPv6
    else
        return 1 # is not IPv6
    fi
}

execute_command() {
    echo -e "\033[0;32m$1\033[0m"
    result=$(eval "$2" 2>&1)
    if [[ $? -ne 0 ]]; then
        if [[ $result == *"No such file or directory"* ]]; then
            echo -e "\033[0;32m$4\033[0m"
        else
            echo -e "\033[0;31mError: $result\033[0m"
        fi
    else
        if [[ -z "$result" ]]; then
            echo -e "\033[0;32m$4\033[0m"
        else
            echo "$result"
            echo -e "\033[0;32m$3\033[0m"
        fi
    fi
    echo "----------------------------"
}

print_ascii_art
execute_command "Initiating Firewall..." "sudo ufw status" "Firewall initiated!" "Firewall status not available."

ip_address=$(curl -s https://ifconfig.me)
if [[ $? -ne 0 ]]; then
    echo -e "\033[0;31mFailed to retrieve public IP address.\033[0m"
else
    if is_ipv6 "$ip_address"; then
        execute_command "Checking for open ports on IPv6 address..." "sudo nmap -6 -p0-65535 $ip_address" "Open ports check complete!" "No open ports found on the IPv6 address."
    else
        execute_command "Checking for open ports..." "sudo nmap -p0-65535 $ip_address" "Open ports check complete!" "No open ports found on the IPv4 address."
    fi
fi

execute_command "Running logwatch..." "sudo logwatch" "Logwatch complete!" "No logwatch data available."

echo -e "\033[0;32mMonitoring important system logs...\033[0m"
execute_command "SSH Login attempts:" "sudo tail -n 50 /var/log/auth.log | grep 'sshd:.*session opened'" "SSH Login attempts found." "No SSH login attempts found."
execute_command "Failed SSH login attempts:" "sudo tail -n 50 /var/log/auth.log | grep 'sshd:.*Failed password'" "Failed SSH login attempts found." "No failed SSH login attempts."
execute_command "System errors:" "sudo tail -n 50 /var/log/syslog | grep -E 'error|fail|fatal'" "System errors found." "No system errors found."
echo "----------------------------"

read -p "Do you want to initiate a virus scan? (Y/n) " choice
case $choice in
    [Yy]|"")
        execute_command "Scanning for malware..." "sudo freshclam && sudo clamscan -ir /home" "Malware scan complete!" "No malware found."
        ;;
    [Nn])
        echo -e "\033[0;32mSkipping virus scan.\033[0m"
        ;;
    *)
        echo -e "\033[0;31mInvalid input, skipping virus scan.\033[0m"
        ;;
esac
