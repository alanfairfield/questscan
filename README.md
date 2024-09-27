**questscan**

This project is a set of security detections automations I compiled while on my journey to becoming a security engineer. As I delved into penetration testing TTPs, and also spent a year working at Cengage on their Blue Team, I wanted to create a project that would streamline the process of doing simple but repetitive checks; status of the firewall, contents of critical log files, hardware integrity, etc. 

questscan is a program that has a context, which is on a debian-based linux server or workstation. There are some specific tools, like UFW, nmap, and logwatch, that are available through the apt package manager, and this project is a way to invoke those tools and produce a report.

**Languages Used**

I initially created this program in BASH, and ported it over to Python for more interoperability, and as a way to practice automation skills in Python

**Key Features**

1. Check status of firewall(s)

2. 