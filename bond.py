from encodings import utf_8
from readline import insert_text
import subprocess
import os
import paramiko
import pymysql
import re
from getpass import getpass

interface = subprocess.check_output("ip -o link show | awk -F': ' '{print $2}' | grep 'enp[0-9]\|ens[0-9]' | uniq -w5 -D", shell=True) 
print (interface)