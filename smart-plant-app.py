import RPi.GPIO as GPIO, time
from urllib.parse import urlencode
from urllib.request import Request, urlopen

GPIO.setmode(GPIO.BCM)

def httpPost(url, postFields):
    request = Request(url, urlencode(postFields).encode())
    json = urlopen(request).read().decode()
    return json

def RCtime (PiPin):
    measurement = 0
    GPIO.setup(PiPin, GPIO.OUT)
    GPIO.output(PiPin, GPIO.LOW)
    #time.sleep(0.1)
    
    time.sleep(1)
    GPIO.setup(PiPin, GPIO.IN)
    while (GPIO.input(PiPin) == GPIO.LOW):
        measurement += 1
    return measurement

def upload(moisture):
    ENDPOINT = "https://ketihweaver.ca/rest/smart-tech/v1/plant/moisture/upload"
    post_fields = {'apikey': 'INSERT_YOUR_API_KEY','plantId':'INSERT_YOUR_PLANT_ID','moistureLevel': moisture}
    result = httpPost(ENDPOINT,post_fields)
    print(result)

# Main program loop
while True:
    moistureLevel = RCtime(14)
    upload(moistureLevel)





