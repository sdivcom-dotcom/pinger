import socket

ip = "192.168.1.10"
port_range = range(1, 65536)

for port in port_range:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} open")