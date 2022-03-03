import re
import os
import subprocess
import pymysql
import paramiko
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
        print("ssh not connect, wrong login or password")
        user = (input("insert login: "))
        secret = getpass("insert password: ")

        
    else:
        print("ssh connect")
        break
    """
db = pymysql.connect(host="localhost",
                        user="admin",
                        passwd="123",
                        db="ipadd")
cur = db.cursor()
cur.execute("select count(*) from ip")
cn = cur.fetchone()
print(cn[0])