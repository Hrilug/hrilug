#!/usr/bin/python3
import os
import subprocess    
from subprocess import run
import time

print("texting...")
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
temp = getCPUtemperature()
def ping (ip):
    a=run('ping -c 2 %s' %ip,shell=True,stdout=subprocess.PIPE)
print(temp)
print(a.returncode) 
