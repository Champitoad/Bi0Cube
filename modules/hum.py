#!/usr/bin/python
# -*-coding:Utf-8 -*

from rest import *
from mysql import *
import time

while 1 :
    hum = dhtRead("hum")
    set_db_sensor("hum", hum)
    time.sleep(1)