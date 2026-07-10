"""
============================================================
Project      : TCP Port Scanner
Author       : Rahul Yadav
Language     : Python 3

Description:
A TCP Connect Port Scanner capable of:
- Port Scanning
- Service Detection
- Banner Grabbing
- HTTP Server Detection
- Saving scan results to a text report

Features:
✔ Custom Port Range
✔ Banner Grabbing
✔ HTTP Enumeration
✔ Save Results to File
✔ Clean Report Generation

============================================================
"""

import socket

# ----------------------------------------
# Get User Input
# ----------------------------------------

target_ip = input("Enter Target IPv4 Address : ")
start_port = int(input("Enter Start Port        : "))
end_port = int(input("Enter End Port          : "))

filename = f"scan_{target_ip}.txt"

report = open(filename, "w")

report.write("=" * 60 + "\n")
report.write("TCP PORT SCANNER REPORT\n")
report.write("=" * 60 + "\n")
report.write(f"Target IP  : {target_ip}\n")
report.write(f"Port Range : {start_port}-{end_port}\n\n")

print("\n===================================")
print("        TCP PORT SCANNER")
print("===================================")
print(f"Target IP      : {target_ip}")
print(f"Port Range     : {start_port}-{end_port}")
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
        # HTTP Detection
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
        # Banner Grab
        # ----------------------------
        else:

            try:
                banner = scanner.recv(1024).decode(errors="ignore").strip()

                if banner == "":
                    banner = "Not Available"

            except:
                banner = "Not Available"

        output = (
            f"[+] Port {port:<5} OPEN ({service})\n"
            f"    Banner : {banner}\n"
        )

        print(output)

        report.write(output + "\n")

    scanner.close()

report.write("=" * 60 + "\n")
report.write("Scan Completed Successfully!\n")
report.close()

print("===================================")
print("Scan Completed Successfully!")
print("===================================")
print(f"\nResults saved to: {filename}")
