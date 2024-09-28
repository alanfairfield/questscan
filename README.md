**questscan**

This project is a set of security detection automations I compiled while on my journey to becoming a security engineer. As I delved into penetration testing TTPs, and also spent a year working at Cengage on their Blue Team, I wanted to create a project that would streamline the process of doing individually quick, but cumulatively arduous checks; the status of the firewall, the contents of critical log files, hardware integrity, changes to sensitive configuration files, etc. 

questscan is a program that finds its context on a linux server or workstation. There are some specific tools, like UFW, nmap, and logwatch, that are available through the apt package manager, and this project is a way to invoke those tools and produce a report.

**Languages Used**

I initially created this program in BASH, and ported it over to Python for interoperability.

**Key Features**

1. Check status of firewall(s)

2. Host scan to reveal open ports, especially for services that were started on an ad-hoc basis, and should be stopped, like FTP or SSH

3. Condensed output from logwatch

4. Checks attempts to connect to the machine over SSH

5. Checks for basic IOCs, like modifications to /etc/passwd