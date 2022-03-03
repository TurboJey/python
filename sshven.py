from encodings import utf_8
from readline import insert_text
import subprocess
import os
import paramiko
import pymysql
import re
from getpass import getpass


def ssh():
    user = (input("insert login: "))
    secret = getpass("insert password: ")
    port = ("22")

    i=0
    try:
        db = pymysql.connect(host="localhost",
                        user="admin",
                        passwd="123",
                        db="ipadd")
        cur = db.cursor()
        cur.execute("select count(*) from ip")
        cn = cur.fetchone()
    except:
        #print("Something went wrong vs database")
        er = subprocess.call("systemctl status mariadb.service", shell=True)
        print(er) 

    else:

        while i < cn[0]:
            j=str(i + 1)
            cur.execute('select ip from ip where id='+ j) 
            res = cur.fetchone()
            #print (res)
            res2 = res[0]
            #print (res2)
            r = 0
            while True:
                try:

                    client = paramiko.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(hostname=res2, username=user, password=secret, port=port) 
                    _stdin, stdout,_stderr = client.exec_command("cat /etc/network/interfaces")
                    test=stdout.read().decode()
                    _stdin, stdout,_stderr = client.exec_command("ip a")
                    test2=stdout.read().decode()
                    _stdin, stdout,_stderr = client.exec_command("lspci -n")
                    test3=stdout.read().decode()
                    vid =  re.findall( "\w{4}:\w{4}", test3)
                    with open ("/home/kanakin/test2", "a") as f:
                        f.writelines('\n' + res2 + '\n')
                        f.writelines("" + "\n")
                    with open("/home/kanakin/test", "a") as f:
                        #f.seek(0, 2) 
                        f.writelines('\n' + res2 + '\n')
                        f.writelines('\n' + test + '\n')
                        f.writelines('\n' + test2 + '\n')
                    if vid != "none":
                        ia = 0
                        ja = 1
                        while ia < len(vid):
                            t = vid[ia]
                            t2 = t[:4]
                            cur.execute('select name from ven where ven_id="'+ t2 + '"' )
                            rest = cur.fetchone()
                            with open("/home/kanakin/test2", "a") as f:
                                f.writelines(t2)
                                f.writelines(" PCI device No. ")
                                f.writelines(str(ja))
                                f.writelines(" belongs to ")
                                f.writelines(str(rest) + '\n')
                            ia = ia + 1
                            ja = ja + 1 
                    client.close()
                except Exception:
                    r = r + 1
                    if r == 3:
                        print("the number of attempts has ended")
                        exit()
                    print("wrong login or password")
                    user = (input("insert login: "))
                    secret = getpass("insert password: ")
                    
                else:
                    
                    i = i + 1
                    break        
        db.close()


def empty():
    if (os.stat("/home/kanakin/test").st_size == 0 and os.stat("/home/kanakin/test2").st_size == 0): 
        ssh()
        print("write files")
    elif (os.stat("/home/kanakin/test").st_size != 0 and os.stat("/home/kanakin/test2").st_size != 0):
        print("files not empty")
        case = (input("did you wont rewrite files y/n: "))
        if (case == "" or case == "y" or case == "Y"):
            subprocess.call("cat /dev/null > /home/kanakin/test", shell=True)
            subprocess.call("cat /dev/null > /home/kanakin/test2", shell=True)
            ssh()
            print("write files")
        elif (case == "n" or case == "N"):
            print("goodbye")
            exit()
        else:
            empty()

empty()