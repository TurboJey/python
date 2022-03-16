from encodings import utf_8
from readline import insert_text
import subprocess
from scp import SCPClient
import os
import paramiko
import re
from getpass import getpass
import pymysql


user = "root"
secret = "P@ssw0rd"
i = 0
ii = 0
num = 1
db = pymysql.connect(host="localhost",
                user="admin",
                passwd="123",
                db="ipadd")
cur = db.cursor()
cur.execute("select count(*) from ip2")
cn = cur.fetchone()
while i < cn[0]:
    j = str(i + 1)
    cur.execute('select ip from ip2 where id = "' + j + '"')
    ip = cur.fetchone()
    ip = ip[0]
    print(ip)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=user, password=secret, port=22) 
    _stdin, stdout,_stderr = client.exec_command("ip -o link show | awk -F': ' '{print $2}' | grep 'enp[0-9]\|ens[0-9]' | uniq -w4 -D")
    test=stdout.read().decode()
    interface = test.split()
    client.close()
    
    while ii < len(interface):
        file = open("/home/kanakin/testbond/" + interface[ii], "w")
        file.close()
        #subprocess.call("cat /dev/null > /home/kanakin/testbond/" + interface[i], shell=True)
        with open("/home/kanakin/testbond/" + interface[ii], "a") as fint:
            fint.write("MTU = 9216" + "\n" + "TYPE=Ethernet" + "\n" + "PROXY_METHOD=none" + "\n" + "BROWSER_ONLY=no" + "\n" + "DEVICE=" + interface[ii] + "\n" + "NAME=slave" + str(j) + "\n" + "BOOTPROTO=none" + "\n" + "SLAVE=yes" + "\n" + "NM_CONTROLLED=yes" + "\n" + "ONBOOT=yes" + "\n")

        if (num == 1 or num == 2):
            with open("/home/kanakin/testbond/" + interface[ii], "a") as fint:
                fint.write("MASTER=bond0")

        else:
            with open("/home/kanakin/testbond/" + interface[ii], "a") as fint:
                fint.write("MASTER=bond1   ")

        p = subprocess.Popen(["sshpass","-p", "P@ssw0rd", "scp", "-r","/home/kanakin/testbond/" + interface[ii], "root@"+ip+":/home/user/"])
        if num == 2:
            #subprocess.call("cat /dev/null > /home/kanakin/testbond/bond0", shell=True)
            with open("/home/kanakin/testbond/bond0", "w") as fbond:
                fbond.write("DEVICE=bond0" + "\n" + "NAME=bond0" + "\n" + "TYPE=Bond" + "\n" + "BONDING_MASTER=yes" + "\n" + "IPV6INIT=no" + "\n" + "MTU=9216" + "\n" + "ONBOOT=yes" + "\n" + "USERCTL=no" + "\n" + "NM_CONTROLLED=yes" + "\n" + "BOOTPROTO=DHCP" + "\n" + "BONDING_OPTS=\"mode=802.3ad xmit_hash_policy=layer2+3 lacp_rate=1 miimon=100\"")
            #subprocess.call("ifup bond0",shell=True)
            p = subprocess.Popen(["sshpass","-p","P@ssw0rd", "scp", "-r","/home/kanakin/testbond/bond0", "root@"+ip+":/home/user/"])
        
        if num == 4:
            with open("/home/kanakin/testbond/bond1", "w") as fbond:
                fbond.write("DEVICE=bond1" + "\n" + "NAME=bond1" + "\n" + "TYPE=Bond" + "\n" + "BONDING_MASTER=yes" + "\n" + "IPV6INIT=no" + "\n" + "MTU=9216" + "\n" + "ONBOOT=yes" + "\n" + "USERCTL=no" + "\n" + "NM_CONTROLLED=yes" + "\n" + "BOOTPROTO=DHCP" + "\n" + "BONDING_OPTS=\"mode=802.3ad xmit_hash_policy=layer2+3 lacp_rate=1 miimon=100\"")
            p = subprocess.Popen(["sshpass","-p","P@ssw0rd", "scp", "-r","/home/kanakin/testbond/bond1", "root@"+ip+":/home/user/"])
            #subprocess.call("ifup bond1",shell=True)
        ii = ii + 1
        num = num + 1
    #print(test)
    i = i + 1