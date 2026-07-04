"""
============================================================
Project      : TCP Port Scanner
Version      : 1.0
Author       : Golu Yadav
Language     : Python 3

Description:
A basic TCP Connect Port Scanner that scans a single TCP
port on a target IPv4 address and reports whether the
port is OPEN or CLOSED.

Features:
✔ Scan a single TCP port
✔ Human-readable output
✔ Proper socket resource management

Version History:
------------------------------------------------------------
v1.0
- Scan a single TCP port
- User enters target IPv4 address
- User enters target port
- Display OPEN/CLOSED status

Next Version (v2.0)
- Scan multiple ports (1-100)
- Create a new socket for each connection
============================================================
"""

import socket

# Get user input
target_ip = input("Enter Target IPv4 Address: ")
target_port = int(input("Enter Target Port Number: "))

# Create a TCP socket
scanner = socket.socket()

# Attempt to connect to the target
result = scanner.connect_ex((target_ip, target_port))

# Display scan result
if result == 0:
    print(f"\n[+] Port {target_port} is OPEN")
else:
    print(f"\n[-] Port {target_port} is CLOSED")

# Close the socket
scanner.close()

print("\nScan Completed.")
