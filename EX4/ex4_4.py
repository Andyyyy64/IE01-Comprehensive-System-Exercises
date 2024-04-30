import RPi.GPIO as GPIO
import time

SERVO_PIN = 18
PWM_FREQ = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, PWM_FREQ)
pwm.start(0)

def set_angle(angle):
    duty_cycle = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)

try:
    while True:
        for angle in [-90, -45, 0, 45, 90]:
            set_angle(angle)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()