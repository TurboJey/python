import re
import os
import subprocess
import pymysql

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
                i = i + 1
                j = j + 1
    db.close()

try:
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