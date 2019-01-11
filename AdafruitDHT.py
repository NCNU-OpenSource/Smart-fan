import sys
import Adafruit_DHT

import RPi.GPIO as GPIO

def temp():
    GPIO.setmode(GPIO.BCM)
    humidity, temperature = Adafruit_DHT.read_retry(22, 18)
    if temperature > 25 and humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:

        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    return [humidity, temperature]
