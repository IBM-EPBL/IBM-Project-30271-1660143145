#Python Program for Led Blinking using Raspberry Pi
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,1)
time.sleep(1)
GPIO.output(11,0)
time.sleep(1)
GPIO.output(11,1)
time.sleep(1)
GPIO.output(11,0)
time.sleep(1)
GPIO.cleanup()


#Python Program for Traffic Light using Raspberry Pi
from gpiozero import LED
import time
red=LED(16)
yellow=LED(18)
green=LED(17)
red.on()
time.sleep(5)
red.off()
yellow.on()
time.sleep(2)
yellow.off()
green.on()
time.sleep(5)
green.off()
