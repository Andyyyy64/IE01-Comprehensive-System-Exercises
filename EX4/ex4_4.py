import RPi.GPIO as GPIO
import time

servo = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(servo, 50)
p.start(0)

def set_angle(angle):
    duty_cycle = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    p.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

try:
    while True:
        for angle in [-90, -45, 0, 45, 90]:
            set_angle(angle)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
