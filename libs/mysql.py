#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = 0

try :
    con = mdb.connect('127.0.0.1', 'root', 'ppebi0cube', 'bioduino');
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])

def set_db_sensor(sensor, value) :
    with con :
        cur = con.cursor()
        cur.execute("UPDATE Sensors SET Value = " + str(value) + " WHERE Sensor = '" + sensor + "'")

def get_db_parameter(param) :
    with con :
        cur = con.cursor()
        cur.execute("SELECT * FROM Parameters")
        rows = cur.fetchall()
        for row in rows :
            if row[1] == param :
                return int(row[2])