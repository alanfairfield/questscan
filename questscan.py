#!/usr/bin/env python3

import subprocess
import requests
import ipaddress

def print_ascii_art():
    ascii_art = '''
                      _
  __ _ _   _  ___ ___| |_ ___  ___ __ _ _ __
 / _` | | | |/ _ / __| __/ __|/ __/ _` | '_ \\
| (_| | |_| |  __\\__ | |_\\__ | (_| (_| | | | |
 \\__, |\\__,_|\\___|___/\\__|___/\\___\\__,_|_| |_|
    | |
    \\_\\
    '''
    print(ascii_art)

def execute_command(command, message, success_message, no_data_message=None):
    print("\033[0;32m" + message + "\033[0m")
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
        if result:
            if "No such file or directory" in result and no_data_message:
                print("\033[0;32m" + no_data_message + "\033[0m")
            else:
                print(result)
        else:
            print("\033[0;32m" + success_message + "\033[0m")
    except subprocess.CalledProcessError as e:
        if no_data_message:
            print("\033[0;32m" + no_data_message + "\033[0m")
        else:
            print(e.output.decode("utf-8"))
    print("----------------------------")

def is_ipv6(ip_str):
    try:
        ipaddress.IPv6Address(ip_str)
        return True
    except ipaddress.AddressValueError:
        return False

print_ascii_art()

execute_command('sudo ufw status', "Initiating Firewall...", "Firewall initiated!")

try:
    ip_address = requests.get('https://ifconfig.me').text

    # Determine if the IP is IPv6 or IPv4 and adjust the nmap command accordingly
    nmap_command = f'sudo nmap -p0-65535 {ip_address}'
    if is_ipv6(ip_address):
        nmap_command = f'sudo nmap -6 -p0-65535 {ip_address}'

    execute_command(nmap_command, "Checking for open ports...", "Open ports check complete!")

except requests.RequestException:
    print("\033[0;31mFailed to retrieve public IP address.\033[0m")

# Running logwatch
execute_command('sudo logwatch', "Running logwatch...", "Logwatch complete!", "No noteworthy logs from logwatch.")

# Monitoring important system logs
print("\033[0;32mMonitoring important system logs...\033[0m")
execute_command("sudo tail -n 50 /var/log/auth.log | grep 'sshd:.*session opened'", "SSH Login attempts:", "SSH Login attempts checked.", "No SSH login attempts found.")
execute_command("sudo tail -n 50 /var/log/auth.log | grep 'sshd:.*Failed password'", "Failed SSH login attempts:", "SSH Login attempts checked.", "No failed SSH login attempts.")
execute_command("sudo tail -n 50 /var/log/syslog | egrep -i 'error|fail|fatal'", "System errors:", "System errors checked.", "No system errors found.")
print("\033[0;32mLogs monitoring complete!\033[0m")
print("----------------------------")

# Virus scan
choice = input("Do you want to initiate a virus scan? (Y/n) ")

if choice.lower() in ["y", ""]:
    execute_command('sudo freshclam && sudo clamscan -r /home', "Scanning for malware...", "Malware scan complete!")
elif choice.lower() == "n":
    print("\033[0;32mSkipping virus scan.\033[0m")
else:
    print("\033[0;31mInvalid input, skipping virus scan.\033[0m")
