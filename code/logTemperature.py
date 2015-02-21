#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys

""" Log Current Time, Temperature in Celsius and Fahrenheit
Return a list[time,tempC,tempF] """

def readTemp():
        tempfile=open("/sys/bus/w1/devices/28-000006975c64/w1_slave")
        tempfile_text=tempfile.read()
        currentTime=time.strftime('%x %X %Z')
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        tempF=(tempC*9.0/5.0)+32.0
        return[currentTime,tempC,tempF]



con = None

try:

        con= mydb.connect ('temperature.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE tempdata(time text, tempC DOUBLE, tempF DOUBLE)')
        mytempdata = readTemp()
        thetime=str(mytempdata[0])
        thecls=mytempdata[1]
        thefrnh=mytempdata[2]
        cur.execute('''INSERT INTO tempdata(time,tempC,tempF)VALUES(?,?,?)''', (thetime,thecls,thefrnh))
        print 'Current Temperature is: '+ str(thefrnh)+ 'F'
        print "temperature logged\n"

finally:


    if con:
        con.close()

