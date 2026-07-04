
# this is version 1.0

import socket

# Create a socket object
scanner = socket.socket()

# Get user input
ip = input("Enter IPv4 Address: ")
port = int(input("Enter Port Number: "))

# Try connecting to the target
result = scanner.connect_ex((ip, port))

# Display result
if result == 0:
    print(f"[+] Port {port} is OPEN")
else:
    print(f"[-] Port {port} is CLOSED")

# Close the socket
scanner.close()

