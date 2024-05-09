import RPi.GPIO as GPIO
import time

led = 18
button = 25
DELAY_SECONDS = int(input("Enter the last digit of your ID: ")) + 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(DELAY_SECONDS)
        GPIO.output(LED_PIN, GPIO.LOW)
        break

GPIO.cleanup()
