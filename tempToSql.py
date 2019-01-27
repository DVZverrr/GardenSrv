import sys
import datetime
from time import sleep
import Adafruit_DHT
import sqlite3

if len(sys.argv) == 2:
  pin = int(sys.argv[1])
else:
  print('Input pin number')
  sys.exit(1)

if pin > 31:
  print('Pin number must be from 0 to 31')
  sys.exit(1)
  
#todo: connection string to config
dbconnect = sqlite3.connect("sensorData.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

try:
  while True:
    readed = False
    hum,temp = Adafruit_DHT.read(Adafruit_DHT.AM2302, pin)
    if hum is not None and temp is not None:
      #print('insert into temperature(temperature, date) values({0:0.1f}, {1})'.format(temp, str(datetime.datetime.now())))
      cursor.execute('insert into temperature(temperature, date) values(?,?)', (temp, str(datetime.datetime.now())))
      cursor.execute('insert into humidity(humidity, date) values(?,?)', (hum, str(datetime.datetime.now())))
      print('Temp={0:0.1f}* Humidity={1:0.1f}%'.format(temp,hum))
      readed = True
    else:
      print('Failed to get sensor data :(')
    if readed:
      sleep(300)
    else  
      sleep(2)

except KeyboardInterrupt:
  dbconnect.commit()
  dbconnect.close()
  print('stop')
