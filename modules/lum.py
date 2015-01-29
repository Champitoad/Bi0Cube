#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
from mysql import *
import time

# INPUT
lumPin = 1

# OUTPUT
ledsPin = 12

def checkLum() :
    lum = int(analogRead(lumPin))
    set_db_sensor("lum", lum)

    if lum < 100 :
        digitalWrite(ledsPin, 1)
    else :
        if digitalRead(ledsPin) != 0 :
            if lum > 180 :
                digitalWrite(ledsPin, 0)

while 1 :
    checkLum()
    time.sleep(1)