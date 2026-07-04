"""
============================================================
Project      : TCP Port Scanner
Version      : 4.0
Author       : Rahul Yadav
Language     : Python 3

Description:
A basic TCP Connect Port Scanner that scans a user-defined
TCP port range on a target IPv4 address and reports whether
each port is OPEN or CLOSED.

Features:
✔ Scan a user-defined TCP port range
✔ Create a new TCP socket for every connection attempt
✔ 5-second socket timeout
✔ Human-readable output
✔ Proper socket resource management

Version History:
------------------------------------------------------------
v1.0
- Scan a single TCP port
- User enters target IPv4 address and target port
- Display OPEN/CLOSED status

v2.0
- Scan ports 1-100
- Create a new socket for each port
- Improved output formatting
- Better variable names

v3.0
- Added 5-second socket timeout
- Faster scanning on filtered or unresponsive ports
- Improved scan reliability

v4.0
- Allow users to define a custom start port
- Allow users to define a custom end port
- Scan a user-defined TCP port range

Next Version (v5.0)
- Display only OPEN ports (optional mode)
============================================================
"""

import socket

# -----------------------------
# Get User Input
# -----------------------------
target_ip = input("Enter Target IPv4 Address : ")
start_port = int(input("Enter Start Port        : "))
end_port = int(input("Enter End Port          : "))

print("\n===================================")
print("        TCP PORT SCANNER")
print("===================================")
print(f"Target IP      : {target_ip}")
print(f"Port Range     : {start_port} - {end_port}")
print("Timeout        : 5 Seconds")
print("===================================\n")

# -----------------------------
# Scan Target Ports
# -----------------------------
for port in range(start_port, end_port + 1):

    # Create a new TCP socket
    scanner = socket.socket()

    # Configure socket timeout
    scanner.settimeout(5)

    # Attempt connection
    result = scanner.connect_ex((target_ip, port))

    # Display result
    if result == 0:
        print(f"[+] Port {port} OPEN")
    else:
        print(f"[-] Port {port} CLOSED")

    # Release system resources
    scanner.close()

print("\n===================================")
print("Scan Completed Successfully!")
print("===================================")