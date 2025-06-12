import socket

def scan_ports(target, ports):
    print(f"\nScanning {target} for ports: {ports}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is open")
            s.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    ports = [21, 22, 23, 25, 53, 80, 443, 8080]  # Common ports
    scan_ports(target, ports)
