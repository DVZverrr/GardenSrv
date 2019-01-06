from flask import Flask
import Adafruit_DHT

app = Flask(__name__)

@app.route('/')
def hello_world():
    hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    if hum is not None and temp is not None:
      return 'Humidity: ' + hum + ' Temp: ' + temp
    else:
      return 'Failed to get data from sensor'
