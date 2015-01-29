#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
from mysql import *
import time

# INPUT
O2RatePin = 2
pinMode(O2RatePin, INPUT)

# OUTPUT
O2CaptPin = 6
O2ProdPin1 = 2
O2ProdPin2 = 3
pinMode(O2CaptPin, OUTPUT)
pinMode(O2ProdPin1, OUTPUT)
pinMode(O2ProdPin2, OUTPUT)

def checkO2Rate() :
    refO2Rate = get_db_parameter("O2")

    O2Rate = int(analogRead(O2RatePin))
    set_db_sensor("O2", O2Rate)

    while abs(O2Rate-refO2Rate) > 0.1 :
        if O2Rate-refO2Rate > 0.1 :
            digitalWrite(O2CaptPin, 0)
        if O2Rate-refO2Rate < -0.1 :
            digitalWrite(O2ProdPin1, 0)
			digitalWrite(O2ProdPin2, 0)

        time.sleep(0.5)

        O2Rate = int(analogRead(O2RatePin))
        set_db_sensor("O2", O2Rate)
		
	digitalWrite(O2CaptPin, 1)
	digitalWrite(O2ProdPin1, 1)
	digitalWrite(O2ProdPin2, 1)

while 1 :
    checkO2Rate()
    time.sleep(1)