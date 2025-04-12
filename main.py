#https://www.tomshardware.com/how-to/raspberry-pi-pico-ultrasonic-sensor
from servo import Servo
from distance import Distance
from time import sleep
import utime

# Create a Servo object on pin 0
servo=Servo(pin=0)
servo.move(15)

distance = Distance(trigger_pin=3, echo_pin=2)



while True:
   d = distance.getDistance()
   utime.sleep(0.2)
   
   if d <= 10 :
       
       servo.move(90)
       
       utime.sleep(2)
       servo.move(0)
       