"""
============================================================
Project      : TCP Port Scanner
Version      : 6.0
Author       : Rahul Yadav
Language     : Python 3

Description:
A TCP Connect Port Scanner that scans a user-defined
TCP port range, identifies common TCP services,
and performs banner grabbing on services that
automatically send banners.

Features:
✔ Scan a user-defined TCP port range
✔ Display only OPEN ports
✔ Detect common TCP services
✔ Perform banner grabbing
✔ 5-second socket timeout
✔ Exception handling for unknown services
✔ Proper socket resource management

Version History:
------------------------------------------------------------
v1.0
- Scan a single TCP port
- Display OPEN/CLOSED status

v2.0
- Scan ports 1-100
- Create a new socket for every port

v3.0
- Added socket timeout
- Improved scan reliability

v4.0
- Added custom port range

v5.0
- Display only OPEN ports
- Detect common TCP services
- Added exception handling

v6.0
- Added banner grabbing
- Decode received banner data
- Display service banners

Next Version (v7.0)
- Send HTTP requests
- Detect HTTP server versions
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

    # Create TCP socket
    scanner = socket.socket()

    # Configure timeout
    scanner.settimeout(5)

    # Attempt connection
    result = scanner.connect_ex((target_ip, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        try:
            banner = scanner.recv(1024).decode().strip()
        except:
            banner = "Not Available"

        print(f"[+] Port {port:<5} OPEN ({service.upper()})")
        print(f"    Banner : {banner}\n")

    # Release socket resources
    scanner.close()

print("===================================")
print("Scan Completed Successfully!")
print("===================================")