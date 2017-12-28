# LV-EZ1 for Raspberry pi

[![SUSHI-WARE LICENSE](https://img.shields.io/badge/license-SUSHI--WARE%F0%9F%8D%A3-blue.svg)](https://github.com/MakeNowJust/sushi-ware)

This Repo is MaxBotix's LV‑ProxSonar‑EZ sensors Repo. 

To use Raspberry pi and GPIO. LV-EZ series can use Serial, PWM and Analog. In case of Arduino, using Analog pins. This repo using Raspberry pi and PWM. 

## Data Sheets
Data Sheets is [here](http://maxbotix.com/documents/LV-ProxSonar-EZ_Datasheet.pdf). 

### Data from data sheets 
- Automatic multi-sensor operation
- Maximum reported range of 254 inches (645 cm)
- ~5 foot proximity detection zone (60 inches or 152 cm)
- Run up to 8+ sensors in the same environment
- Choice of 2 digital outputs: Logic Level (High/Low) and RS232 serial
- 42kHz Ultrasonic sensor measures distance to objects
- Read from sensor outputs: Serial and Pulse Width
- Virtually no sensor dead zone, objects closer than 6 inches range as 6 inches
- Operates from 2.5-5.5V
- Low 2.0mA average current requirement

## Wiring
Wiring sample is down side picture. 

![](https://i.imgur.com/OKOk3So.png)


![](https://i.imgur.com/a8J6Qi5.jpg)

Connect to the LV-EZ1 in the order GND(-), VCC(+), GPIO(Pin15) from the left.

# Program

Using Python. 
This program is using ultrasonic wave. As the sound advances 340 meters per second, to get distance that into consideration and measure the distance to the object.

### Method
Easy to get distance. 

As the sound advances 340m per second (equal 34300 cm). 
The distance can be obtained by multiplying the speed and the elapsed time. That is, the distance is 34300 * elpsed time(ms)

## example code

When this code is executed print distance per second.

### Output example

Ultrasonic Measurement
Distance : 192.1 cm
Distance : 192.1 cm
Distance : 191.8 cm
        :
        :
        :
(Ctrl + D) Stop


``` getdist.py
# coding: utf-8
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGECHO = 15

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)  # Initial state as output


# Set trigger to False (Low)
GPIO.output(GPIO_TRIGECHO, False)

def measure():
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

try:

    while True:

        distance = measure()
        print "  Distance : %.1f cm" % distance
        time.sleep(1)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()
```
