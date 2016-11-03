import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.setup(14, GPIO.IN)
    print "GPIO:[" + str(GPIO.input(14)) + "]"
    print time.time()

GPI.cleanup()
