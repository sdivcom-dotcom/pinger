import nmap
   
begin = 20
end = 23

target = '192.168.1.10'

scanner = nmap.PortScanner()
   
for i in range(begin,end+1):

    res = scanner.scan(target,str(i))
   
    res = res['scan'][target]['tcp'][i]['state']
   
    print(f'port {i} is {res}.')