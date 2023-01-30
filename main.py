import os
import argparse

ping_const = "ping -c 1 -w 1 "
parser = argparse.ArgumentParser(description='Write ip addders without the last octet - example python3 main.py --a=192.168.1 --s=0 --ra=255')
parser.add_argument("--a")
parser.add_argument("--s")
parser.add_argument("--ra")
parser.add_argument("--nmap")
args = parser.parse_args()
a = args.a
s = args.s
ra = args.ra

if a == None:
    a = "192.168.1"
else:
    g = 0

if ra == None:
    r = 255
elif ra != None:
    ra = int(ra)
    if (0 < ra < 255): 
        r = ra
    elif ra == 255:
        r = 255
    else:
        print("Incorrect data")
        r = 255
else:
    print("Incorrect data")
    r = 255

if s == None:
    i = 0   
    oktet = 0
elif s != None:
    s = int(s)
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
        #break
    else:
        g = 0
    i = i + 1
    oktet = oktet + 1
