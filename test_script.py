'''from encodings import utf_8
from readline import insert_text
import subprocess
from scp import SCPClient
import os
import paramiko
import re
from getpass import getpass
import pymysql'''
"""
def vend():
    cur = db.cursor()
    check = subprocess.call("lspci -n", shell=True, stdout=subprocess.DEVNULL)
    if check == 0:
        pci = subprocess.check_output("lspci -n", shell=True).decode('utf-8')
        pci = re.findall( "\w{4}:\w{4}", pci)
        if pci != "none":
            i = 0
            j = 1
            while i < len(pci):
                test = pci[i]
                test2 = test[:4]
                cur.execute('select name from ven where ven_id="'+ test2 + '"' )
                res = cur.fetchone()
                print("PCI device No.", j, "belongs to", res)
                i = i + 1user = (input("insert login: "))
secret = getpass("insert password: ")
port = (input("select port for ssh: "))
    db = pymysql.connect(host="localhost",
                     user="admin",
                     passwd="123",
                     db="vendor")
except:
    #print("Something went wrong vs database")
    er = subprocess.call("systemctl status mariadb.service", shell=True)
    print(er)

else:
    vend()

user = (input("insert login: "))
secret = getpass("insert password: ")
port = ("22")
host = "172.16.27.131"
while True:
    try:

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port) 
        #_stdin, stdout,_stderr = client.exec_command("cat /etc/network/interfaces")
        #test=stdout.read().decode()
        #_stdin, stdout,_stderr = client.exec_command("ip a")
        #test2=stdout.read().decode()
        client.close()
    except:
        print("ssh not cfrom encodings import utf_8
from readline import insert_text
import subprocess
from scp import SCPClient
import os
import paramiko
import re
from getpass import getpass
        
    else:
        print("ssh connect")
        break
    
db = pymysql.connejj=str(ii)
            cur.execute('select ip from ip where id='+ j) 
            res = cur.fetchone()
            #print (res)
            res2 = res[0]
            #print (res2)
            while True:
                try:

                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(hostname=res2, username=user, password=secret, port=22)
                except:
                    print("somthing wrong whis ssh")
                else:ct(host="localhost",
                        user="admin",
                        passwd="123",
                        db="ipadd")
cur = db.cursor()
cur.execute("select count(*) from ip")
cn = cur.fetchone()
print(cn[0])    
"""
'''#hostname = "192.168.225.128"
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
'''


from asyncio.subprocess import PIPE
import subprocess
import re
import os
import sys
from sys import stdout


def chanel():
    i = 1  
    j = str(i)
    ipmi = subprocess.Popen("ipmitool lan print 3", shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    streamdata = ipmi.communicate()[0]
    rc = ipmi.returncode
    if rc == 0:
        ipmi = subprocess.Popen("ipmitool lan print " + j, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ipmi = ipmi.stdout.read().decode()
        spli = ipmi.splitlines()
        for line in spli:
            if re.match("IP Address  ", str(line)):
                print("ipmi use "+ j +" chanel")
                return(spli)
    else:
        print(streamdata)
        print(rc)
        sys.exit()
    i = i + 1


class Ipmi:


    def __init__(self, spli):
        self.chanel = spli
        self._dictdata = {}
        self._bmcdata = {}
        self.data_processing()
        self.bmc_data()
        self.macadd = self.mac()
        self.ipadd = self.ip()
        self.bmc = self.bmc_ver()
        

    def data_processing(self):
        for line in self.chanel:
            res = line.split(':', 1)
            self._dictdata.update({res[0].strip(): res[1].strip()})
        del self._dictdata['']


    def bmc_data(self):
        ipmi = subprocess.Popen("ipmitool bmc info", shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ipmi = ipmi.stdout.read().decode('utf-8')
        spl = ipmi.splitlines()
        for line in spl:
            bmc = line.split(':', 1)
            if len(bmc) == 2:    
                self._bmcdata.update({bmc[0].strip(): bmc[1].strip()})
    

    def ip(self):
        return self._dictdata['IP Address']


    def mac(self):
        return self._dictdata['MAC Address']


    def bmc_ver(self):
        return self._bmcdata['IPMI Version']

    
ch = chanel()
ipmi = Ipmi(ch)
print(ipmi.ipadd)
print(ipmi.macadd)
print(ipmi.bmc)