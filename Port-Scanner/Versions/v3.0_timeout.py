"""
============================================================
Project      : TCP Port Scanner
Version      : 3.0
Author       : Golu Yadav
Language     : Python 3

Description:
A basic TCP Connect Port Scanner that scans TCP ports
1-100 on a target IPv4 address.

Features:
✔ Scan multiple TCP ports (1-100)
✔ Create a new socket for every connection
✔ Socket timeout (1 second)
✔ Human-readable output
✔ Proper socket resource management

Version History:
------------------------------------------------------------
v1.0
- Scan a single TCP port
- User enters target IPv4 address and port
- Display OPEN/CLOSED status

v2.0
- Scan ports 1-100
- Create a new socket for each port
- Improved output formatting
- Better variable names

v3.0
- Added 1-second socket timeout
- Faster scanning on filtered/unresponsive ports
- Improved scan reliability

Next Version (v4.0)
- Allow custom port range
============================================================
"""

import socket

# Get target IP address
target_ip = input("Enter Target IPv4 Address: ")

print("\n===================================")
print(f"Scanning Target : {target_ip}")
print("Port Range      : 1 - 100")
print("Timeout         : 1 Second")
print("===================================\n")

# Scan ports 1 to 100
for port in range(1, 101):

    # Create a new TCP socket
    scanner = socket.socket()

    # Wait at most 1 second for a response
    scanner.settimeout(5)

    # Attempt connection
    result = scanner.connect_ex((target_ip, port))

    # Display result
    if result == 0:
        print(f"[+] Port {port:<5} OPEN")
    else:
        print(f"[-] Port {port:<5} CLOSED")

    # Close socket
    scanner.close()

print("\n===================================")
print("Scan Completed Successfully!")
print("===================================")