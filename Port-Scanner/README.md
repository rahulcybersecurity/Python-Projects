# TCP Port Scanner

A professional TCP Port Scanner built from scratch in **Python** using the `socket` module. This project was developed step by step to understand socket programming, TCP communication, service detection, banner grabbing, and basic HTTP enumeration.

---

## Features

* Scan TCP ports on a target IPv4 address
* Scan a custom port range
* Detect common TCP services
* Banner grabbing for supported services (FTP, SSH, etc.)
* Basic HTTP server detection
* Save scan results to a text file
* Configurable socket timeout
* Clean and readable output

---

## Technologies Used

* Python 3
* Socket Programming
* TCP Networking

---

## Project Structure

```text
Port-Scanner/
│
├── port_scanner.py          # Latest stable version
├── README.md
│
└── Versions/
    ├── v1.0_single_port_scanner.py
    ├── v2.0_multiple_port_scanner.py
    ├── v3.0_socket_timeout.py
    ├── v4.0_custom_port_range.py
    ├── v5.0_service_detection.py
    ├── v6.0_banner_grabbing.py
    ├── v7.0_http_server_detection.py
    └── v8.0_save_scan_results.py
```

---

## Version History

### v1.0

* Scan a single TCP port
* Display OPEN/CLOSED status

### v2.0

* Scan multiple TCP ports (1–100)
* Create a new socket for every connection

### v3.0

* Added socket timeout
* Improved scan reliability

### v4.0

* Added custom port range

### v5.0

* Service detection using `socket.getservbyport()`
* Display only open ports
* Exception handling

### v6.0

* Banner grabbing
* Decode received banner data

### v7.0

* HTTP GET request
* HTTP server detection
* Basic HTTP response parsing

### v8.0

* Save scan results to a text report

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/<your-username>/Python-Projects.git
```

Go to the project directory:

```bash
cd Python-Projects/Port-Scanner
```

Run the scanner:

```bash
python3 port_scanner.py
```

---

## Example Output

```text
===================================
        TCP PORT SCANNER
===================================
Target IP      : 119.18.58.80
Port Range     : 20 - 100
Timeout        : 5 Seconds
===================================

[+] Port 21 OPEN (FTP)
    Banner : Pure-FTPd

[+] Port 22 OPEN (SSH)
    Banner : SSH-2.0-OpenSSH_7.4

[+] Port 80 OPEN (HTTP)
    Banner : Server: Apache

===================================
Scan Completed Successfully!
===================================
```

---

## Skills Demonstrated

* Python Programming
* Socket Programming
* TCP Networking
* Service Enumeration
* Banner Grabbing
* HTTP Communication
* Exception Handling
* File Handling
* Git & GitHub Version Control

---

## Future Improvements

* HTTPS (SSL/TLS) Support
* Multithreaded Scanning
* Export Results to CSV/JSON
* Command-Line Arguments
* IPv6 Support
* Improved Error Handling

---

## Disclaimer

This project is intended for educational purposes and for scanning systems that you own or have explicit permission to test. Always follow applicable laws, organizational policies, and ethical guidelines when performing network scanning.

---

## Author

**Rahul Yadav**

Cybersecurity & Python Enthusiast
