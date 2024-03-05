import socket
import sys
import re
from common_ports import ports_and_services

def to_string(hostname, ip_addr, ports):
    output = 'Open ports for '
    if hostname != None:
        output += "{} ({})".format(hostname, ip_addr)
    else:
        output += "{}".format(ip_addr)
    
    output += "\nPORT" + " " * 5 + "SERVICE"
    for port in ports:
        service = ports_and_services[port]
        output += "\n{}".format(port) + " " * (9-len(str(port))) + "{}".format(service)
    return output

def get_open_ports(target, port_range, verbose = False):
    open_ports = []
    ip = None
    host = None
    try:
        ip = socket.gethostbyname(target)   
        
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        if re.search('[a-zA-Z]', target):
            return 'Error: Invalid hostname'
        return 'Error: Invalid IP address'
    except socket.error:
        return 'Error: Invalid IP address'
    
    try:
        host = socket.gethostbyaddr(target)[0]
    except socket.herror as e:
        host=None
        
    start, end = port_range
   
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            
            s.close()
        except socket.error as e:
            print(e)
       
    if verbose:
        return to_string(host, ip, open_ports)
    else:
        return open_ports 
    
def main():
    ports = get_open_ports("104.26.10.78", [440, 450], True)
    print(ports)

if __name__ == '__main__':
    main()
