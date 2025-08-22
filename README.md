### Network Scanning and Port Discovery Tool (Python)

This repository hosts a simple but functional network scanning and port discovery tool developed using the Python programming language. The main goal of the project is to identify open TCP ports on a target IP address or domain name and provide basic information about those ports. This tool is an ideal starting point for anyone interested in cybersecurity, students who want to learn about network protocols, or those looking for a simple network discovery tool.

**Project Purpose and Importance**

Modern network infrastructures, servers, and services communicate over various ports. Open ports show which services a server (for example, a web server, an SSH server, or a database) is offering to the outside world. This tool allows a system administrator or a security analyst to check if devices on their network are leaving unexpected ports open. Malware often creates backdoors by opening hidden ports. This tool can help in the rapid detection of such potential security vulnerabilities.

**Key Features**

* **Flexible Target Selection:** The user can enter an IP address (e.g., `192.168.1.1`) or a domain name (e.g., `example.com`) for the scan. The program automatically converts the domain name to an IP address.
* **Customizable Port Range:** It defaults to scanning well-known ports from 1-1024, but this range can be easily changed and extended.
* **Multi-Connection Check:** It uses the `socket` module to attempt a separate connection for each port.
* **Effective Timeout Management:** It includes a timeout mechanism to prevent delays during connection attempts, so the scan doesn't hang and completes efficiently.
* **Clear Reporting:** It reports open ports and their associated services (e.g., `Port 80 open [HTTP]`) in an easy-to-understand format.
* **Error Handling:** It provides user-friendly error messages for situations like an invalid target input or network connection issues.

**Technical Details**

This project leverages the power of Python's standard `socket` module. It's built on the fundamental principles of the TCP/IP protocol and socket programming. The code has a clean and understandable structure, making it easy for both beginners and experienced developers to read and modify.

By using this tool, you can perform network discovery, identify potential security vulnerabilities, and get hands-on practice with basic network communication principles. Contributions to further develop the project and add new features are always welcome.
