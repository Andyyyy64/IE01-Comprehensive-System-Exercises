import RPi.GPIO as GPIO
import time

LED_PIN = 18
PWM_FREQ = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, PWM_FREQ)
pwm.start(0)

try:
    while True:
        for duty_cycle in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
        for duty_cycle in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()