
# 🚀 Port-Spoofer

**P_Spoofer** is a lightweight **network service spoofing tool** that allows you to emulate various services  on different ports. It can be useful for **honeypots, penetration testing, or security research**.

---

## ✨ Features
- **Multiple Service Spoofing:** SSH, HTTP, HTTPS, FTP, SMTP, POP3
- **Customizable Settings:** Specify port number and service version
- **Lightweight:** Runs in the background with minimal resource usage
- **User-Friendly:** Simple Python script for easy setup

---

## 🛠️ Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/P_Spoofer.git
cd P_Spoofer
```

### 2. Install Python
#### Linux/macOS:
```sh
sudo apt install python3
```

#### Windows:
Download Python from the [official website](https://www.python.org/downloads/) and install it.

### 3. Run the Script
```sh
python3 p_spoofer.py
```

---

## 🚦 Usage
1. Run the script.
2. Enter the port number (e.g., 22 for SSH, 80 for HTTP).
3. Enter the service name (SSH, HTTP, FTP, etc.).
4. Enter the version of the service (e.g., OpenSSH_8.0).
5. The tool will start listening on the selected port and spoof the specified service.

---

## 🔧 Example Session
```sh
Enter the port number to spoof (21,22,80,443,25,110): 22
Enter the service name (SSH, HTTP, FTP, HTTPS, SMTP, POP3): SSH
Enter the version of SSH (e.g., OpenSSH_8.0): OpenSSH_8.0
```

The tool will now emulate SSH on port 22 and return a fake version string when a client connects.

---

## ⚠️ Disclaimer
This tool is intended for **educational and security research purposes only**. Do not use it for malicious activities. The developer is **not responsible** for any misuse.

---

## 🤝 Contributing
Pull requests are welcome! Feel free to improve the script or add new service spoofing capabilities.

---





