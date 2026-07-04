"""
============================================================
Project      : TCP Port Scanner
Version      : 2.0
Author       : Rahul Yadav
Language     : Python 3

Description:
A basic TCP Connect Port Scanner that scans ports 1-100
on a target IPv4 address and reports whether each port
is OPEN or CLOSED.

Features:
✔ Scan multiple TCP ports (1-100)
✔ New socket created for every connection
✔ Human-readable output
✔ Proper resource management

Version History:
------------------------------------------------------------
v1.0
- Scan a single TCP port
- Display OPEN/CLOSED status

v2.0
- Scan ports 1-100
- Create a new socket for each port
- Improved output formatting
- Better variable names
- Scan completion message

Next Version (v3.0)
- Add socket timeout
============================================================
"""

import socket

# Get target IP address
target_ip = input("Enter Target IPv4 Address: ")

print("\n==============================")
print(f"Scanning Target: {target_ip}")
print("Port Range     : 1 - 100")
print("==============================\n")

# Scan ports 1 to 100
for port in range(1, 101):

    # Create a new socket for this connection
    scanner = socket.socket()

    # Attempt connection
    result = scanner.connect_ex((target_ip, port))

    # Display result
    if result == 0:
        print(f"[+] Port {port:<5} OPEN")
    else:
        print(f"[-] Port {port:<5} CLOSED")

    # Close socket
    scanner.close()

print("\n==============================")
print("Scan Completed Successfully!")
print("==============================")
