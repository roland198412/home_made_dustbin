from machine import Pin
import utime

class Distance:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

    def getDistance(self):
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
            
        while self.echo.value() == 1:
            signalon = utime.ticks_us()
        
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        print("The distance from object is", distance, "cm")
        return distance
