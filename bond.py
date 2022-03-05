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
        subprocess.call("cat /dev/null > /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'MTU = 9216' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'TYPE=Ethernet' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'PROXY_METHOD=none' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'BROWSER_ONLY=no' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'DEVICE='"+ interface[i] + ">> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'NAME=slave'" + str(j) + ">> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'BOOTPROTO=none' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'SLAVE=yes' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'NM_CONTROLLED=yes' >> /home/kanakin/testbond/" + interface[i], shell=True)
        subprocess.call("echo 'ONBOOT=yes' >> /home/kanakin/testbond/" + interface[i], shell=True)
         #print (interface[i])
        
        if (j == 1  or j == 2):
            subprocess.call("echo 'MASTER=bond0' >> /home/kanakin/testbond/" + interface[i], shell=True)
        else:
            subprocess.call("echo 'MASTER=bond1' >> /home/kanakin/testbond/" + interface[i], shell=True)

        if j == 2:
            subprocess.call("cat /dev/null > /home/kanakin/testbond/bond0", shell=True) 
            subprocess.call("(echo 'DEVICE=bond0' ; echo 'NAME=bond0' ; echo 'TYPE=Bond' ; echo 'BONDING_MASTER=yes' ; echo 'IPV6INIT=no' ; echo 'MTU=9216' ; echo 'ONBOOT=yes' ; echo 'USERCTL=no' ; echo 'NM_CONTROLLED=yes' ; echo 'BOOTPROTO=DHCP' ) >> /home/kanakin/testbond/bond0", shell=True)
            opt1 = ("echo 'BONDING_OPTS=\"mode=802.3ad xmit_hash_policy=layer2+3 lacp_rate=1 miimon=100\"'  >> /home/kanakin/testbond/bond0")
            subprocess.call(opt1 ,shell=True) 
            #subprocess.call("ifup bond0",shell=True)
        if j == 4:
            subprocess.call("cat /dev/null > /home/kanakin/testbond/bond1", shell=True) 
            subprocess.call("(echo 'DEVICE=bond1' ; echo 'NAME=bond1' ; echo 'TYPE=Bond' ; echo 'BONDING_MASTER=yes' ; echo 'IPV6INIT=no' ; echo 'MTU=9216' ; echo 'ONBOOT=yes' ; echo 'USERCTL=no' ; echo 'NM_CONTROLLED=yes' ; echo 'BOOTPROTO=DHCP' ) >> /home/kanakin/testbond/bond1", shell=True)
            opt2 = ("echo 'BONDING_OPTS=\"mode=802.3ad xmit_hash_policy=layer2+3 lacp_rate=1 miimon=100\"'  >> /home/kanakin/testbond/bond1")
            subprocess.call(opt2 ,shell=True) 
            #subprocess.call("ifup bond1",shell=True)


        i = i + 1
        j = j + 1