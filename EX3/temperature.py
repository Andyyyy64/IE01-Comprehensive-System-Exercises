import RPi.GPIO as GPIO
import dht11
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SENSOR_PIN = 14

instance = dht11.DHT11(pin=SENSOR_PIN)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temperature: %d°C" % result.temperature)
        print("Humidity: %d%%" % result.humidity)
    time.sleep(1)