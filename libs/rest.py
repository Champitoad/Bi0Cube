#!/usr/bin/python
# -*-coding:Utf-8 -*

import urllib2
from bridge.bridgeclient import *

INPUT = 0
OUTPUT = 1

ip = "192.168.240.1"

bridge = BridgeClient()

def digitalRead(pin) :
    urllib2.urlopen("http://" + ip + "/arduino/digital/" + str(pin))
    value = bridge.get("D"+str(pin))

    return value

def digitalWrite(pin, state) :
    response = urllib2.urlopen("http://" + ip + "/arduino/digital/" + str(pin) + "/" + str(state))
    html = response.read()

    return html

def analogRead(pin) :
    urllib2.urlopen("http://" + ip + "/arduino/analog/" + str(pin))
    value = bridge.get("A"+str(pin))

    return value

def analogWrite(pin, state) :
    response = urllib2.urlopen("http://" + ip + "/arduino/analog/" + str(pin) + "/" + str(state))
    html = response.read()

    return html

def pinMode(pin, mode) :
    if mode == INPUT :
        strmode = "/input"
    else :
        strmode = "/output"
    response = urllib2.urlopen("http://" + ip + "/arduino/mode/" + str(pin) + strmode)
    return response.read()

def dhtRead(sensor) :
    response = urllib2.urlopen("http://" + ip + "/arduino/dhtread/" + sensor)
    return int(float(response.read()))
