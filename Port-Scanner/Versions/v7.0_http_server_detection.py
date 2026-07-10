"""
============================================================
Project      : TCP Port Scanner
Version      : 7.0
Author       : Rahul Yadav
Language     : Python 3

Description:
A TCP Connect Port Scanner that scans a user-defined
TCP port range, detects common TCP services, grabs
service banners, and performs basic HTTP server
enumeration.

Features:
✔ Scan custom TCP port range
✔ Display only OPEN ports
✔ Detect common TCP services
✔ Banner grabbing (FTP, SSH, etc.)
✔ HTTP GET request
✔ Extract HTTP Server header
✔ 5-second socket timeout
✔ Proper exception handling
✔ Clean output

Version History:
------------------------------------------------------------
v1.0
- Single Port Scanner

v2.0
- Multiple Port Scanner

v3.0
- Socket Timeout

v4.0
- Custom Port Range

v5.0
- Service Detection

v6.0
- Banner Grabbing

v7.0
- HTTP Request
- HTTP Server Detection

Next Version (Ideas)
- HTTPS Support
- Multithreading
- Save Results to File
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
# Scan Ports
# ----------------------------------------

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(5)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:

        # ----------------------------
        # Detect Service
        # ----------------------------
        try:
            service = socket.getservbyport(port).upper()
        except:
            service = "UNKNOWN"

        banner = "Not Available"

        # ----------------------------
        # HTTP Enumeration
        # ----------------------------
        if service == "HTTP":

            try:

                request = (
                    f"GET / HTTP/1.1\r\n"
                    f"Host: {target_ip}\r\n"
                    f"Connection: close\r\n\r\n"
                )

                scanner.sendall(request.encode())

                response = scanner.recv(4096).decode(errors="ignore")

                for line in response.splitlines():
                    if line.lower().startswith("server:"):
                        banner = line
                        break

            except:
                banner = "Server Header Not Found"

        # ----------------------------
        # Banner Grabbing
        # ----------------------------
        else:

            try:
                banner = scanner.recv(1024).decode(errors="ignore").strip()

                if banner == "":
                    banner = "Not Available"

            except:
                banner = "Not Available"

        # ----------------------------
        # Display Result
        # ----------------------------
        print(f"[+] Port {port:<5} OPEN ({service})")
        print(f"    Banner : {banner}\n")

    scanner.close()

print("===================================")
print("Scan Completed Successfully!")
print("===================================")