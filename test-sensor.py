#The following code was from this blog post:
#http://www.raspberrypi-spy.co.uk/2012/08/reading-analogue-sensors-with-one-gpio-pin/
#
#It demostrates the responses from an analogue GPIO like our moisture sensor.
#Compared to the original blog post, we changed the pin to 14 instead of 4.

import RPi.GPIO as GPIO, time

# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

# Define function to measure charge time
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement

# Main program loop
while True:
  print RCtime(14) # Measure timing using GPIO4
