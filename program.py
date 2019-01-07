from flask import Flask
from time import sleep
import Adafruit_DHT

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = '<html><head></head><body>'
    for i  in range(50):
      hum, temp = Adafruit_DHT.read(Adafruit_DHT.AM2302, 17)
      result = result + 'Attempt {0:d}: '.format(i+1)
      if hum is not None and temp is not None:
        result = result + 'Humidity: {0:0.1f}%  Temp: {1:0.1f}C<br>'.format(hum,temp)
      else:
        result = result + 'Failed to get data from sensor<br>'
      sleep(2)
    return result + '</body></html>'

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
