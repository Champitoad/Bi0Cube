#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
from mysql import *
import time

# OUTPUT
ventiloResPin = 13
pinMode(ventiloResPin, OUTPUT)

def checkTemp() :
    refTemp = get_db_parameter("temp")

    temp = dhtRead("temp")
    set_db_sensor("temp", temp)

    while refTemp-temp > 1.0 :
        digitalWrite(ventiloResPin, 1)

        time.sleep(0.5)

        temp = dhtRead("temp")
        set_db_sensor("temp", temp)

while 1 :
    checkTemp()
    time.sleep(1)