from socket import AddressFamily
import psutil
from tabulate import tabulate

class Network_Details(object):
     def __init__(self):
          self.parser=psutil.net_if_addrs()
     
     def __repr__(self):
          self.interfaces=[]
          self.address_ip=[]
          self.subnet_ip=[]
          self.broadcast_ip=[]
          for interface_name,interface_addresses in self.parser.items():
               self.interfaces.append(interface_name)
               for address in interface_addresses:
                    if str(address.family)=='AddressFamily.AF_INET':
                         self.address_ip.append(address.address)
                         self.subnet_ip.append(address.netmask)
                         self.broadcast_ip.append(address.broadcast)
          data={
               "Interface":[*self.interfaces],
               "IP-Address":[*self.address_ip],
               "Netmask":[*self.subnet_ip],
               "Broadcast-IP":[*self.subnet_ip]
          }
          return tabulate(data,headers="keys",tablefmt="github")

if __name__=="__main__":
     print(Network_Details())