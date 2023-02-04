import os
import subprocess
import argparse

ping_const = "ping -c 1 -w 1 "
parser = argparse.ArgumentParser(description='Write ip addders without the last octet - example python3 main.py -a=192.168.1 -s=0 -ra=255')
nmap = 'sudo nmap '
mac_parser =' | grep "MAC Address:" | grep -oE "([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2} \(.*\)"'

parser.add_argument('-a', '--adress_zone',
                        dest='a',
                        help='Enter the address without the last octet and period',
                        default="192.168.1",
                        type=str)

parser.add_argument('-s', '--start_address',
                        dest='s',
                        help='Enter the address you want to start scanning',
                        default=0,
                        type=int)

parser.add_argument('-ra', '--range',
                        dest='ra',
                        help='Enter the last address to be scanned ',
                        default=12,
                        type=int)

parser.add_argument('-inter', '--interface',
                        dest='inter',
                        help='Optionally, enter the interface from which you want to scan ',
                        default=None,
                        type=int)

parser.add_argument('-mac', '--mac',
                        dest='mac',
                        help='Optionally, if you want the mac address of all detected devices to be displayed',
                        default=0,
                        type=int)

parser.add_argument('-ports', '--ports',
                        dest='ports',
                        help='Optionally, displays all open ports of the found devices',
                        default=0,
                        type=int)

parser.add_argument('-breaks', '--breaks',
                        dest='breaks',
                        help='Optionally, as soon as you want to stop at the first address you see',
                        default=0,
                        type=int)


#T#ODO
#nmap scanning and print mac address and ports
#sudo nmap 192.168.1.85 | grep "MAC Address:" | grep -oE '([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2} \(.*\)'
#sudo nmap 192.168.1.85 | grep open
#and flag interface

args = parser.parse_args()
a = args.a
s = args.s
ra = args.ra
mac = args.mac

if (0 < ra < 255): 
    r = ra
elif ra == 255:
    r = 255
else:
    print("Incorrect data")
    r = 255

if (0 < s < 255): 
    i = s
    oktet = s
elif s == 0:
    i = 0
    oktet = 0
else:
    print("Incorrect data")
    i = 0
    oktet = 0

if mac == 1:
    mac_const = 1
elif mac == 0:
    mac_const = 0
else:
    print("Incorrect data")
    mac_const = 0

if ports == 1:
    ports_const = 1
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


r = int(r)
while i < r:
    oktet = str(oktet)
    a = str(a)
    ping_const = str(ping_const)
    hostname = a + "." + oktet
    oktet = int(oktet)
    response = os.system(ping_const + hostname + " 1>/dev/null")
    if response == 0:
        print(hostname, 'is up!')
        if mac_const == 1:
            command1 = nmap + hostname + mac_parser
            response1 = subprocess.check_output(command1, shell=True)
            print(response1)
        else:
            g = 0
        if ports_const == 1:
            command2 = nmap + hostname
            response2 = subprocess.check_output(command2, shell=True)
            print(response2)
        else:
            g = 0
        if breaks_const == 1:
            break
        else:
            g = 0
        

        #break
    else:
        g = 0
    i = i + 1
    oktet = oktet + 1