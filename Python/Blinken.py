import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)

def blink(timeout):
    GPIO.output(4, True)
    time.sleep(timeout)
    GPIO.output(4, False)
    time.sleep(timeout)
    

setup()
while True:
    blink(1)
    blink(2)
    blink(1)