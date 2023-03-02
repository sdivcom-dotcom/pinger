import os
import socket
import subprocess
import argparse
import socket
import urllib.request

url = "https://api.macvendors.com/"
version_programm = "0.5"
nmap = 'sudo nmap '
inter_flag = ' -I '
ports_max = "10480"
ping_const = "ping -c 1 -w 1 "


def get_network_interfaces():
    interfaces = []
    for interface in socket.if_nameindex():
        interface_name = interface[1]
        interfaces.append(interface_name)
    return interfaces


network_interfaces = get_network_interfaces()
network_interfaces = str(network_interfaces)
print("network interfaces = " + network_interfaces)

parser = argparse.ArgumentParser(description="Write ip addders \
                                              without the last octet \
                                              example python3 \
                                              main.py \
                                              -a 192.168.1 \
                                              -s 0 \
                                              -ra 255" + network_interfaces)

parser.add_argument('-a', '--adress_zone',
                    dest='a',
                    help='Enter the address \
                    without the last octet and period',
                    default="192.168.1",
                    type=str)

parser.add_argument('-s', '--start_address',
                    dest='s',
                    help='Enter the address you \
                    want to start scanning',
                    default=0,
                    type=int)

parser.add_argument('-ra', '--range',
                    dest='ra',
                    help='Enter the last address to be scanned ',
                    default=12,
                    type=int)

parser.add_argument('-inter', '--interface',
                    dest='inter',
                    help='Optionally, if you want the scan to be on \
                    the specified \
                    interface only, specify 1 ' + network_interfaces,
                    default=0,
                    type=int)

parser.add_argument('-inter_name', '--interface_name',
                    dest='inter_name',
                    help='Optionally, enter the interface \
                    from which you \
                    want to scan ' + network_interfaces,
                    default='lo',
                    type=str)

parser.add_argument('-mac', '--mac',
                    dest='mac',
                    help='Optionally, if you want the mac address \
                    of all detected devices to be displayed',
                    default=0,
                    type=int)

parser.add_argument('-ports', '--ports',
                    dest='ports',
                    help='Optionally, displays all open \
                    ports of the found devices',
                    default=0,
                    type=int)

parser.add_argument('-breaks', '--breaks',
                    dest='breaks',
                    help='Optionally, as soon as you want to \
                    stop at the first address you see',
                    default=0,
                    type=int)

parser.add_argument('-v', '--version',
                    dest='version',
                    help='Version programm',
                    default=0,
                    type=int)


args = parser.parse_args()
a = args.a
s = args.s
ra = args.ra
inter = args.inter
inter_name = args.inter_name
mac = args.mac
ports = args.ports
breaks = args.breaks
version = args.version

if 0 < ra < 255:
    r = ra
    r = int(r)
elif ra == 255:
    r = 255
    r = int(r)
else:
    print("Incorrect data")
    r = 255
    r = int(r)

if 0 < s < 255:
    i = s
    oktet = s
elif s == 0:
    i = 0
    oktet = 0
else:
    print("Incorrect data")
    i = 0
    oktet = 0

if inter == 1:
    ping_const = str(ping_const)
    ping = ping_const + inter_flag + inter_name
elif inter == 0:
    ping_const = str(ping_const)
    ping = ping_const
else:
    print("Incorrect data")
    ping_const = str(ping_const)
    ping = ping_const

if mac == 1:
    mac_const = 1
elif mac == 0:
    mac_const = 0
else:
    print("Incorrect data")
    mac_const = 0

if ports == 1:
    ports_const = 1
elif ports == 2:
    ports_const = 2
elif ports == 0:
    ports_const = 0
else:
    print("Incorrect data")
    ports_const = 0

if breaks == 1:
    breaks_const = 1
elif breaks == 0:
    breaks_const = 0
else:
    print("Incorrect data")
    breaks_const = 0

if version == 1:
    print("verion programm: " + version_programm)
    r = 0
    r = int(r)
else:
    pass


def get_mac_address(ip_address):
    cmd = f"arp -n {ip_address}"
    output = subprocess.check_output(cmd, shell=True).decode("utf-8")
    print(output)
    lines = output.split("\n")
    for line in lines:
        if ip_address in line:
            mac_address = line.split()[2]
            print(mac_address)
            replace_mac = mac_address.replace(':', '-')
            url2 = url + replace_mac
            response = urllib.request.urlopen(url2)
            print(response.read().decode('utf-8'))
            return mac_address


def netcat(ip_address):
    port_range = range(1, 65536)
    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            result = s.connect_ex((ip_address, port))
            if result == 0:
                print(f"Port {port} open")


def netcat_wireguard(ip_address):
    netcat = 'nc -zvw3 '
    port = "51820"
    netcat = 'nc -zvw3 '
    command = netcat + ip_address + " " + port + " 2> /dev/null"
    val = os.system(command)
    if val == 0:
        command2 = netcat + ip_address + " " + port + " 1> /dev/null"
        value2 = subprocess.check_output(command2,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        value2 = str(value2)
        x = value2.find("succeeded!")
        if x > 46:
            print("Port number found = " + port)
        else:
            pass

def http_https(ip_address):
    try:
        urllib.request.urlopen("http://" + ip_address)
        print("Website", ip_address, "is available over http.")
    except:
        print("Website", ip_address, "is not available over http.")
    try:
        urllib.request.urlopen("https://" + ip_address)
        print("Website", ip_address, "is available over https.")
    except:
        print("Website", ip_address, "is not available over https.")

while i < r:
    oktet = str(oktet)
    a = str(a)
    hostname = a + "." + oktet
    oktet = int(oktet)
    response = os.system(ping + " " + hostname + " 1> /dev/null")
    if response == 0:
        print(hostname, 'is up!')

        if mac_const == 1:
            response1 = get_mac_address(hostname)
            print("MAC address: " + response1)
        else:
            pass
        if ports_const == 1:
            netcat(hostname)
            netcat_wireguard(hostname)
            http_https(hostname)

        elif ports_const == 2:
            command2 = nmap + hostname
            response2 = subprocess.check_output(command2, shell=True)
            print(response2)
            http_https(hostname)
            

        else:
            pass

        if breaks_const == 1:
            break

        else:
            pass
    else:
        pass

    i = i + 1
    oktet = oktet + 1
