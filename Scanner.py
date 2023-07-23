import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool.")
print("<------------------------------------------------------->")

ip_addr = input("Please enter the IP you want to scan: ")
print("The IP entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan to run
             1)SYN ACK Scan
             2) UDP Scan
             3)Comprehensive Scan""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-V -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
      print("Nmap Version: ", scanner.nmap_version())
      scanner.scan(ip_addr, '1-1024', '-V -sS')
      print(scanner.scaninfo())
      print("IP Status: ", scanner[ip_addr].state())
      print(scanner[ip_addr].all_protocols())
      print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '3':
     print("Nmap Version: ", scanner.nmap_version())
     scanner.scan(ip_addr, '1-1024', '-V -sS')
     print(scanner.scaninfo())
     print("IP Status: ", scanner[ip_addr].state())
     print(scanner[ip_addr].all_protocols())
     print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option.")