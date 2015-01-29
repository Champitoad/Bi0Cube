#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
import time

ledsPin = 12

digitalWrite(ledsPin, 1)
time.sleep(3)
digitalWrite(ledsPin, 0)
