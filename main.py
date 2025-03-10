import socket
import threading

def spoof_service(port, service_name, service_version):
    """Spoof a service on the specified port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(5)
    print(f"[+] Listening on port {port} for {service_name}...")

    while True:
        client_socket, addr = sock.accept()
        print(f"[+] Accepted connection from {addr}")

        # Determine response based on service name and version
        if service_name.lower() == 'ssh':
            response = f"SSH-2.0-OpenSSH_{service_version}\r\n".encode('utf-8')
        elif service_name.lower() == 'ftp':
            response = f"220 (vsFTPd {service_version})\r\n".encode('utf-8')
        elif service_name.lower() == 'http':
            response = (
                "HTTP/1.1 200 OK\r\n"
                f"Server: Apache/{service_version} (Ubuntu)\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Content-Length: 48\r\n"
                "\r\n"
                "<html><body>Hello, world!</body></html>"
            ).encode('utf-8')
        elif service_name.lower() == 'https':
            response = (
                "HTTP/1.1 200 OK\r\n"
                f"Server: nginx/{service_version}\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Content-Length: 48\r\n"
                "\r\n"
                "<html><body>Hello, HTTPS world!</body></html>"
            ).encode('utf-8')
        elif service_name.lower() == 'smtp':
            response = b"220 my-smtp.example.com ESMTP Postfix (Ubuntu)\r\n"
        elif service_name.lower() == 'pop3':
            response = b"+OK POP3 server ready\r\n"
        else:
            response = b"Unknown service\r\n"

        # Send the response
        client_socket.sendall(response)
        client_socket.close()

def main():
    print("\n" + "=" * 40)  # Line above
    # Centering the name "P_SPOOFER" with increased size
    name = "\033[1mP_SPOOFER\033[0m"
    width = 50  # Total width for centering
    print(name.center(width))  # Centered name
    print("=" * 40 + "\n")  # Line below

    try:
        # User input for port
        port = int(input("Enter the port number to spoof (21,22,80,443,25,110): "))
        if not (1 <= port <= 500):
            raise ValueError("Port must be between 1 and 500.")

        # Service name and version input
        service_name = input("Enter the service name (SSH, HTTP, FTP, HTTPS, SMTP, POP3): ")
        service_version = input(f"Enter the version of {service_name} (e.g., OpenSSH_8.0): ")

        # Start the service in a new thread
        thread = threading.Thread(target=spoof_service, args=(port, service_name, service_version))
        thread.daemon = True
        thread.start()

        # Keep the main thread alive
        thread.join()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

