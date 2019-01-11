import RPi.GPIO as GPIO  
import time  
import signal  
import atexit  
import AdafruitDHT

atexit.register(GPIO.cleanup)    

GPIO.setmode(GPIO.BCM)  
GPIO.setup(17, GPIO.OUT, initial=False)  
p = GPIO.PWM(17,50) #50HZ  
p.start(0)    

while(True):
  data = AdafruitDHT.temp()
  if data[0] > 80:
    p.start(0)
    print("in")
    for i in range(0,360,10):  
      time.sleep(0.02)
      p.ChangeDutyCycle(2.5 + 10 * i / 360)  
  else:
      print("stop")
      p.stop()

