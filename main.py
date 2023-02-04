import os
import argparse

ping_const = "ping -c 1 -w 1 "
parser = argparse.ArgumentParser(description='Write ip addders without the last octet - example python3 main.py -a=192.168.1 -s=0 -ra=255')

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
                        default=3,
                        type=int)

parser.add_argument('-inter', '--interface',
                        dest='inter',
                        help='Optionally, enter the interface from which you want to scan ',
                        default=None,
                        type=int)

parser.add_argument('-mac', '--mac',
                        dest='mac',
                        help='Optionally, if you want the mac address of all detected devices to be displayed',
                        default=None,
                        type=int)

parser.add_argument('-ports', '--ports',
                        dest='ports',
                        help='Optionally, displays all open ports of the found devices',
                        default=None,
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
        if 
        #break
    else:
        g = 0
    i = i + 1
    oktet = oktet + 1