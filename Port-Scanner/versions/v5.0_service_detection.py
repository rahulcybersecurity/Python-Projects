"""
============================================================
Project      : TCP Port Scanner
Version      : 5.0
Author       : Rahul Yadav
Language     : Python 3

Description:
A basic TCP Connect Port Scanner that scans a user-defined
TCP port range on a target IPv4 address. The scanner
displays only OPEN ports and attempts to identify the
associated TCP service.

Features:
✔ Scan a user-defined TCP port range
✔ Display only OPEN ports
✔ Detect common TCP services
✔ 5-second socket timeout
✔ Handle unknown services gracefully
✔ Proper socket resource management

Version History:
------------------------------------------------------------
v1.0
- Scan a single TCP port
- Display OPEN/CLOSED status

v2.0
- Scan ports 1-100
- Create a new socket for each port

v3.0
- Added socket timeout
- Improved scan reliability

v4.0
- Added custom port range

v5.0
- Display only OPEN ports
- Detect common TCP services
- Handle unknown service names using try/except

Next Version (v6.0)
- Banner Grabbing
============================================================
"""

import socket

# ----------------------------------------
# Get User Input
# ----------------------------------------
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

# ----------------------------------------
# Scan Target Ports
# ----------------------------------------
for port in range(start_port, end_port + 1):

    # Create a new TCP socket
    scanner = socket.socket()

    # Configure socket timeout
    scanner.settimeout(5)

    # Attempt connection
    result = scanner.connect_ex((target_ip, port))

    # Display only OPEN ports
    if result == 0:

        # Try to identify the service
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"[+] Port {port:<5} OPEN ({service.upper()})")

    # Release system resources
    scanner.close()

print("\n===================================")
print("Scan Completed Successfully!")
print("===================================")