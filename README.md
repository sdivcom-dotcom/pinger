# pinger

*A python script for pinging your assigned zone:*

 - python3 main.py 
 - -a 192.168.1 
 - -s 0 
 - -ra 255 
 - -inter 1 
 - -inter_name "network interface" 
 - -mac 1 
 - -ports 1
 - -breaks 1 
 - -v 1
   
   network interfaces = ['lo', 'enp0s25', 'wlp3s0']
   
   usage: main.py [-h] [-a A] [-s S] [-ra RA] [-inter INTER]
   [-inter_name INTER_NAME] [-mac MAC] [-ports PORTS] [-breaks BREAKS]
   [-v VERSION]
 - Write ip addders without the last octet - example python3 main.py
   -a 192.168.1 -s 0 -ra 255 ['lo', 'enp0s25', 'wlp3s0']

options:

 - *-h, --help show this help message and exit
   -a A, --adress_zone A*
   
   Enter the address without the last octet and period
   
   *-s S, --start_address S*
   
   Enter the address you want to start scanning
   
   *-ra RA, --range RA Enter the last address to be scanned*
   
   *-inter INTER, --interface INTER*
   
   Optionally, if you want the scan to be on the specified interface
   only, specify 1 ['lo', 'enp0s25', 'wlp3s0']
   
   *-inter_name INTER_NAME, --interface_name INTER_NAME*
   
   Optionally, enter the interface from which you want to scan ['lo',
   'enp0s25', 'wlp3s0']
   
   *-mac MAC, --mac MAC Optionally, if you want the mac address of all detected devices to be displayed*
   
   *-ports PORTS, --ports PORTS*
   
   Optionally, displays all open ports of the found devices
  IMPORTANT!!! For now to run this function you need to run it through sudo with -ports 2 flag 
  You can scan all ports up to 11000 port without sudo and use -ports 1 flag.

   
   *-breaks BREAKS, --breaks BREAKS*
   
   Optionally, as soon as you want to stop at the first address you see
   
   *-v VERSION, --version VERSION*
   
   Version programm
