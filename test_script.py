from encodings import utf_8
from readline import insert_text
import subprocess
from scp import SCPClient
import os
import paramiko
import re
from getpass import getpass
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
    
db = pymysql.connect(host="localhost",
                        user="admin",
                        passwd="123",
                        db="ipadd")
cur = db.cursor()
cur.execute("select count(*) from ip")
cn = cur.fetchone()
print(cn[0])    
"""
hostname = "192.168.225.128"
user = "root"
secret = "123"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, username=user, password=secret, port=22) 
_stdin, stdout,_stderr = client.exec_command("ip -o link show | awk -F': ' '{print $2}' | grep 'enp[0-9]\|ens[0-9]' | uniq -w4 -D")
test=stdout.read().decode()
client.close()
print(test)
