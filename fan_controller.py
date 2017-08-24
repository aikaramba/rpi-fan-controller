#!/usr/bin/env python3

# Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
# Modified: Andrii Balaniuk <a.balanyuk@yahoo.com>

import os
import signal
import sys
import RPi.GPIO as GPIO

from time import sleep

pin = 18 # fan control pin
maxTMP = 60 # temperature goal after which the fan will turn on
minTMP = 55 # temperature goal after which the fan will turn off
checkRate = 3 # in seconds

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()
def getCPUtemperature():
    res = os.popen("vcgencmd measure_temp").readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp
def fanON():
    setPin(True)
    return()
def fanOFF():
    setPin(False)
    return()
def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        fanON()
    if CPU_temp<minTMP:
        fanOFF()
    return()
def setPin(mode):
    GPIO.output(pin, mode)
    return()

# main loop
setup()
while True:
    getTEMP()
    sleep(checkRate)
