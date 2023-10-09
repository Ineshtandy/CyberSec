import subprocess
# helps open new programs, send and receive data, redirect input and output of the process 
# handles input output and errors genereated
import string
import random
import re
# provides regular expressions

def get_random_mac_address():
    """Generate and return a MAC address in the format of Linux"""
    # get the hexdigits uppercased
    allHexiDigits = string.hexdigits.upper()
    # set copies all distinct characters from the string passed and stores them
    uppercased_hexdigits = ''.join(set(allHexiDigits))
    # ditinct characters set is now converted into a string
    # 2nd character must be 0, 2, 4, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

# this function gets the mac address of the current computer
def get_current_mac_address(iface):
    # use the ifconfig command to get the interface details, including the MAC address

    # check_output returns the std output of the command
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    # mac address is located after ether word so we search to grab it 
    return re.search("ether (.+) ", output).group().split()[1].strip()

def change_mac_address(iface, new_mac_address):
    # disable the network interface
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    # change the MAC
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_address}", shell=True)
    # enable the network interface again
    subprocess.check_output(f"ifconfig {iface} up", shell=True)