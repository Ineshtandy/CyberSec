import subprocess
import re

def get_current_ip_address(iface):

    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("inet (.+) ", output).group().split()[1].strip()

def get_router_ip_address():

        output = subprocess.check_output(f"netstat -nr | grep default",shell = True).decode()
        return re.search("default (.+) ",output).group().split()[1].strip()

def change_ip_address(routerAddr):
    
    subprocess.check_output(f"ifconfig en0 {routerAddr}", shell=True)

if __name__ == "__main__":
      curIp = get_current_ip_address("en0")
      curRouterIp = get_router_ip_address()
      print("current ip address is = ",curIp)
      change_ip_address(curRouterIp)
      curIp = get_current_ip_address("en0")
      print("new ip address is = ",curIp)


      



