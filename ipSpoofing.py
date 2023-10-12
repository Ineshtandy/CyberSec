import subprocess
import re

def get_current_ip_address():

    output = subprocess.check_output(f"ifconfig eth0", shell=True).decode()
    return re.search("inet (.+) ", output).group().split()[1].strip()

def get_router_ip_address():

        output = subprocess.check_output(f"ip r | grep default",shell = True).decode()
        return re.search("via (.+) ",output).group().split()[1].strip()

def change_ip_address(routerAddr):
    
    subprocess.check_output(f"ifconfig eth0 {routerAddr}", shell=True)

if __name__ == "__main__":
      curIp = get_current_ip_address()
      curRouterIp = get_router_ip_address()
      print("current ip address is = ",curIp)
      change_ip_address(curRouterIp)
      curIp = get_current_ip_address("en0")
      print("new ip address is = ",curIp)


      



