import subprocess
import re

def get_current_ip_address(iface):

    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("inet (.+) ", output).group().split()[1].strip()

def get_router_ip_address():

        output = subprocess.check_output(f"netstat -nr | grep default",shell = True).decode()
        print(re.search("default (.+) ",output).group().split()[1].strip())

get_router_ip_address()



