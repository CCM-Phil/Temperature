#!/usr/bin/env python

import urllib2
#import RPi.GPIO as GPIO
import os
import time
import datetime

#load thermometer drivers
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
store_temp = 9999

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()
 
    return int(mytemp[1])
 
  except:
    return 99999

# Temp sensor ID	
# eg id = '28-000006b05e41'
id = TempSensorId
#  print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))

while True:
	try:
		return_temp = '{:.3f}'.format(gettemp(id)/float(1000))
		if return_temp != store_temp:
			urllib2.urlopen('https://api.thingspeak.com/update?api_key='+ThingSpeakKey+'&field1='+str(return_temp))
			store_temp = return_temp
		time.sleep(60)
	except KeyboardInterrupt:  
		sys.exit("User Quit")	
	except Exception,e: 
		#
		#print str(e)
		continue