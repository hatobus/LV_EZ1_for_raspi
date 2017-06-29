import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Dist():
    
    def __init__(self):
        pass
    
    def Measure(self,gp):
        GPIO_TRIGECHO = gp 
        GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)
        GPIO.output(GPIO_TRIGECHO, False)
      # This function measures a distance
      # Pulse the trigger/echo line to initiate a measurement
        GPIO.output(GPIO_TRIGECHO, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGECHO, False)
      #ensure start time is set in case of very quick return
        start = time.time()

      # set line to input to check for start of echo response
        GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
        while GPIO.input(GPIO_TRIGECHO)==0:
            start = time.time()

      # Wait for end of echo response
        while GPIO.input(GPIO_TRIGECHO)==1:
            stop = time.time()

        GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
        GPIO.output(GPIO_TRIGECHO, False)

        elapsed = stop-start
        distance = (elapsed * 34300)/2.0
        time.sleep(0.1)
        return distance
