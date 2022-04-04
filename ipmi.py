from asyncio.log import logger
from asyncio.subprocess import PIPE
import subprocess
import re
import os
import sys
import logging, logging.config
from sys import stdout
import time
from datetime import datetime


logging.config.fileConfig('/home/user/python/loging.conf')


def chanel():
    logger = logging.getLogger('chanel')
    logger.debug(str(datetime.now()) + " - Script starting mode: chanel")
    i = 9
    while i > 0:   
        j = str(i)
        ipmi = subprocess.Popen("ipmitool lan print " + j, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        streamdata = ipmi.communicate()[0]
        rc = ipmi.returncode
        pl = os.uname()
        if rc == 0:
            ipmi = subprocess.Popen("ipmitool lan print " + j, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            ipmi = ipmi.stdout.read().decode()
            spli = ipmi.splitlines()
            for line in spli:
                if re.match("IP Address  ", str(line)):
                    logger.info('Detect Chanel: '+ j)
                    return(spli)
            logger.debug('chanel '+ str(i) + ' not active')
            i=i-1
        elif rc == 1:
            logger.debug('chanel '+ str(i) + ' not active')
            i=i-1
        elif rc == 127:
            logger.debug(rc)
            logger.info(streamdata)
            ins = (input('install ipmitool? y/n: '))
            if ins == 'y' or ins == 'Y' or ins == '': 
                if 'Debian' in str(pl):
                    logger.debug('install ipmitool')
                    subprocess.Popen('apt install ipmitool', shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    time.sleep(3)
                    chanel()
            else:
                logger.debug('user not install ipmitool')
                print('goodbye')
                sys.exit()
        else:
            logger.info(streamdata)
            logger.info(rc)
            sys.exit()
        


class Ipmi:


    logger = logging.getLogger('ipm')
    logger.debug(str(datetime.now()) + " - Script starting mode: ipmi" )


    def __init__(self, spli):
        self.chanel = spli
        self._dictdata = {}
        self._bmcdata = {}
        self.data_processing()
        self.bmc_data()
        self.ipadd = self.ip()
        self.macadd = self.mac()
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
        logger = logging.getLogger('ipm')
        #logger.debug(str(datetime.now()) + " - Script starting mode: ipmi" )
        logger.debug('ip addres : ' + self._dictdata['IP Address'])
        return self._dictdata['IP Address']


    def mac(self):
        logger = logging.getLogger('ipm')
        logger.debug('mac addres : ' + self._dictdata['MAC Address'])
        return self._dictdata['MAC Address']


    def bmc_ver(self):
        logger = logging.getLogger('ipm')
        logger.debug('bmc version : ' + self._bmcdata['IPMI Version'])
        return self._bmcdata['IPMI Version']

    
ch = chanel()
ipmi = Ipmi(ch)
print(ipmi.ipadd)
print(ipmi.macadd)
print(ipmi.bmc) 