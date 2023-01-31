# pinger
# A python script for pinging your assigned zone
# Write ip addders without the last octet - example python3 main.py -a=192.168.1 -s=0 -ra=255

options:
  -h, --help            show this help message and exit
  -a A, --adress_zone A
                        Enter the address without the last octet and period
  -s S, --start_address S
                        Enter the address you want to start scanning
  -ra RA, --range RA    Enter the last address to be scanned