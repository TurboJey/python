from asyncio.subprocess import PIPE
import subprocess
import re
import os
from sys import stdout


def chanel():
    i = 1
    while i < 10:   
        j = str(i)
        ipmi = subprocess.Popen("ipmitool lan print " + j, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ipmi = ipmi.stdout.read().decode()
        spli = ipmi.splitlines()
        for line in spli:
            if re.match("IP Address  ", str(line)):
                print("ipmi use "+ j +" chanel")
                return(spli)


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
            if len(bmc) == 1:
                self._bmcdata.update({bmc[0].strip(): ' '})
            elif len(bmc) == 2:    
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