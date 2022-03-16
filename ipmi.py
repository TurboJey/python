from asyncio.subprocess import PIPE
import subprocess
import re
import os
from sys import stdout

 

class Ipmi():
    def chanel(self):
        i = 1
        while i < 10:
            j = str(i)
            ipmi = subprocess.Popen("ipmitool lan print " + j, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            ipmi = ipmi.stdout.read().decode('utf-8')
            spl = ipmi.splitlines()
            self.num = j
            for line in spl:
                res = re.match("IP Address  ", str(line))
                if res != None:
                    print("ipmi use "+ self.num +" chanel")
                    return(self.num)                
            i = i + 1        

    

    def ip(self):
        ipmi = subprocess.Popen("ipmitool lan print " + self.num, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ipmi = ipmi.stdout.read().decode('utf-8')
        spl = ipmi.splitlines()
        for line in spl:
            if re.match("IP Address  ", str(line)):
                res = line.split(': ')
                print(res[1])


    def bmc_version(self):
        ipmi = subprocess.Popen("ipmitool bmc info", shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ipmi = ipmi.stdout.read().decode('utf-8')
        spl = ipmi.splitlines()
        for line in spl:
            if re.match("IPMI Version", str(line)):
                res = line.split(': ')
                print(res[1])


    def mac(self):
        ipmi = subprocess.Popen("ipmitool lan print " + self.num, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ipmi = ipmi.stdout.read().decode('utf-8')
        spl = ipmi.splitlines()
        for line in spl:
            if re.match("MAC Address", str(line)):
                res = line.split(': ')
                print(res[1])

main = Ipmi()
main.chanel()
main.ip()
main.bmc_version()
main.mac()