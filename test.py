import subprocess

def get_mac_address(ip_address):
    cmd = f"arp -n {ip_address}"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    lines = output.split("\n")
    for line in lines:
        if ip_address in line:
            mac_address = line.split()[2]
            return mac_address

mac_address = get_mac_address("192.168.1.229")
print("MAC Address:", mac_address)