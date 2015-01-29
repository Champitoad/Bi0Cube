#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
from mysql import *
import time

# INPUT
CO2RatePin = 3
pinMode(CO2RatePin, INPUT)

# OUTPUT
CO2CaptPin = 7
CO2ProdPin1 = 4
CO2ProdPin2 = 5
pinMode(CO2CaptPin, OUTPUT)
pinMode(CO2ProdPin1, OUTPUT)
pinMode(CO2ProdPin2, OUTPUT)

def checkCO2Rate() :
    refCO2Rate = get_db_parameter("CO2")

    CO2Rate = int(analogRead(CO2RatePin))
    set_db_sensor("CO2", CO2Rate)

    while abs(CO2Rate-refCO2Rate) > 0.1 :
        if CO2Rate-refCO2Rate > 0.1 :
            digitalWrite(CO2CaptPin, 0)
        if CO2Rate-refCO2Rate < -0.1 :
            digitalWrite(CO2ProdPin1, 0)
			digitalWrite(CO2ProdPin2, 0)

        time.sleep(0.5)

        CO2Rate = int(analogRead(CO2RatePin))
        set_db_sensor("CO2", CO2Rate)
	
	digitalWrite(CO2CaptPin, 1)
	digitalWrite(CO2ProdPin1, 1)
	digitalWrite(CO2ProdPin2, 1)

while 1 :
    checkCO2Rate()
    time.sleep(1)