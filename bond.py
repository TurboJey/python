from encodings import utf_8
from readline import insert_text
import subprocess
import os
import paramiko
import re
from getpass import getpass

interface = subprocess.check_output("ip -o link show | awk -F': ' '{print $2}' | grep 'vmnet' | uniq -w5 -D", shell=True).decode('utf-8')
interface = interface.split()
if interface != "none":
    i = 0
    while i < len(interface):
        print(interface[i])
        subprocess.call("cat /dev/null > /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'MTU = 9216' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'TYPE=Ethernet' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'PROXY_METHOD=none' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'BROWSER_ONLY=no' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'DEVICE='"+ interface[i] + ">> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'NAME=slave'" + str(i + 1) + ">> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'BOOTPROTO=none' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'SLAVE=yes' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'NM_CONTROLLED=yes' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
        subprocess.call("echo 'ONBOOT=yes' >> /home/kanakin/testbond/" + interface[i] + ".txt", shell=True)
         #print (interface[i])
        i = i + 1
    