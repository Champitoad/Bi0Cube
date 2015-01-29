#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
import time

ventiloResPin = 13

pinMode(ventiloResPin, OUTPUT)

digitalWrite(ventiloResPin, 0)
time.sleep(3)

digitalWrite(ventiloResPin, 1)
