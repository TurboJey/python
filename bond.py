from encodings import utf_8
from readline import insert_text
import subprocess
import os
import paramiko
import re
from getpass import getpass

interface = subprocess.check_output("ip -o link show | awk -F': ' '{print $2}' | grep 'vmnet' | uniq -w5 -D", shell=True).decode('utf-8')
#interface = subprocess.check_output("ip -o link show | awk -F': ' '{print $2}' | grep 'enp[0-9]\|ens[0-9]' | uniq -w5 -D", shell=True).decode('utf-8')
interface = interface.split()
if interface != "none":
    i = 0
    j = 1
    while i < len(interface):
        print(interface[i])
        file = open("/home/kanakin/testbond/" + interface[i], "w")
        file.close()

        #subprocess.call("cat /dev/null > /home/kanakin/testbond/" + interface[i], shell=True)
        with open("/home/kanakin/testbond/" + interface[i], "a") as fint:
            fint.write("MTU = 9216" + "\n" + "TYPE=Ethernet" + "\n" + "PROXY_METHOD=none" + "\n" + "BROWSER_ONLY=no" + "\n" + "DEVICE=" + interface[i] + "\n" + "NAME=slave" + str(j) + "\n" + "BOOTPROTO=none" + "\n" + "SLAVE=yes" + "\n" + "NM_CONTROLLED=yes" + "\n" + "ONBOOT=yes" + "\n")

        if (j == 1  or j == 2):
            with open("/home/kanakin/testbond/" + interface[i], "a") as fint:
                fint.write("MASTER=bond0")

        else:
            with open("/home/kanakin/testbond/" + interface[i], "a") as fint:
                fint.write("MASTER=bond1   ")


        if j == 2:
            #subprocess.call("cat /dev/null > /home/kanakin/testbond/bond0", shell=True)
            with open("/home/kanakin/testbond/bond0", "w") as fbond:
                fbond.write("DEVICE=bond0" + "\n" + "NAME=bond0" + "\n" + "TYPE=Bond" + "\n" + "BONDING_MASTER=yes" + "\n" + "IPV6INIT=no" + "\n" + "MTU=9216" + "\n" + "ONBOOT=yes" + "\n" + "USERCTL=no" + "\n" + "NM_CONTROLLED=yes" + "\n" + "BOOTPROTO=DHCP" + "\n" + "BONDING_OPTS=\"mode=802.3ad xmit_hash_policy=layer2+3 lacp_rate=1 miimon=100\"")
            #subprocess.call("ifup bond0",shell=True)
        
        if j == 4:
            with open("/home/kanakin/testbond/bond1", "w") as fbond:
                fbond.write("DEVICE=bond1" + "\n" + "NAME=bond1" + "\n" + "TYPE=Bond" + "\n" + "BONDING_MASTER=yes" + "\n" + "IPV6INIT=no" + "\n" + "MTU=9216" + "\n" + "ONBOOT=yes" + "\n" + "USERCTL=no" + "\n" + "NM_CONTROLLED=yes" + "\n" + "BOOTPROTO=DHCP" + "\n" + "BONDING_OPTS=\"mode=802.3ad xmit_hash_policy=layer2+3 lacp_rate=1 miimon=100\"")

            #subprocess.call("ifup bond1",shell=True)


        i = i + 1
        j = j + 1