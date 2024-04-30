import RPi.GPIO as GPIO
import time

BUTTON_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        print("Button pressed")
    else:
        print("Button not pressed")
    time.sleep(0.1)

GPIO.cleanup()