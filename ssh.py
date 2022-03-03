from encodings import utf_8
from readline import insert_text
import subprocess
import os
import paramiko
import pymysql
import re
from getpass import getpass

user = (input("insert login: "))
secret = getpass("insert password: ")
port = ("22")

def ssh():
    
    i=1
    try:
        db = pymysql.connect(host="localhost",
                        user="admin",
                        passwd="123",
                        db="ipadd")
        cur = db.cursor()
    except:
        #print("Something went wrong vs database")
        er = subprocess.call("systemctl status mariadb.service", shell=True)
        print(er) 

    else:

        while i < 4:
            j=str(i)
            cur.execute('select ip from ip where id='+ j) 
            res = cur.fetchone()
            #print (res)
            res2 = res[0]
            #print (res2)
            while True:
                try:

                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(hostname=res2, username=user, password=secret, port=port) 
                    
                except:
                    print("wrong login or password")
                    user = (input("insert login: "))
                    secret = getpass("insert password: ")
                else:
                    _stdin, stdout,_stderr = client.exec_command("cat /etc/network/interfaces")
                    test=stdout.read().decode()
                    _stdin, stdout,_stderr = client.exec_command("ip a")
                    test2=stdout.read().decode()
                    client.close()
                    with open("/home/kanakin/test", "a") as f:
                        #f.seek(0, 2) 
                        f.writelines('\n' + res2 + '\n')
                        f.writelines('\n' + test + '\n')
                        f.writelines('\n' + test2 + '\n')
                    i = i + 1
                    break        
        db.close()     



"""
def ven():
    try:
        db = pymysql.connect(host="localhost",
                     user="admin",
                     passwd="123",
                     db="vendor")
    except:
        print("Something went wrong vs database")
        er = subprocess.call("systemctl status mariadb.service", shell=True)
        print(er)
    else:
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
                    i = i + 1
                    j = j + 1
        db.close()
#ven()
"""


def venssh():
    try:
        db = pymysql.connect(host="localhost",
                     user="admin",
                     passwd="123",
                     db="ipadd")
        cur = db.cursor()
        db2 = pymysql.connect(host="localhost",
                     user="admin",
                     passwd="123",
                     db="vendor")
        cur2 = db2.cursor()
    except:
        print("Something went wrong vs database")
        er = subprocess.call("systemctl status mariadb.service", shell=True)
        print(er)
    else:
        i = 1
        while i < 4:
            j=str(i)
            cur.execute('select ip from ip where id='+ j)
            res = cur.fetchone()
            #print (res)
            res2 = res[0]
            #print (res2)
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=res2, username=user, password=secret, port=port)
            _stdin, stdout,_stderr = client.exec_command("lspci -n")
            v =stdout.read().decode()
            v =  re.findall( "\w{4}:\w{4}", v)
            with open("/home/kanakin/test2", "a") as f:
                f.writelines(res2 + '\n')
            if v != "none":
                ia = 0
                ja = 1
                while ia < len(v):
                    test = v[ia]
                    test2 = test[:4]
                    cur2.execute('select name from ven where ven_id="'+ test2 + '"' )
                    rest = cur2.fetchone()
                    #print("PCI device No.", j, "belongs to", rest)
                    with open("/home/kanakin/test2", "a") as f:
                        f.writelines(test2)
                        f.writelines(" PCI device No. ")
                        f.writelines(str(ja))
                        f.writelines(" belongs to ")
                        f.writelines(str(rest) + '\n')
                    ia = ia + 1
                    ja = ja + 1 
            i = i + 1
            client.close()
        db.close()
        db2.close()


def empty():
    if os.stat("/home/kanakin/test").st_size == 0:
        #print("file empty")
        ssh()
        print("write /home/kanakin/test")
    elif os.stat("/home/kanakin/test").st_size != 0:
        print("file test not empty")
    if os.stat("/home/kanakin/test2").st_size == 0:
        venssh()
        print("write /home/kanakin/test2")
    elif os.stat("/home/kanakin/test").st_size != 0:
        print("file test2 not empty")
empty()