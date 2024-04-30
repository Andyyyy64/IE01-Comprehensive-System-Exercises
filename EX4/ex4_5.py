import smbus
import time
import datetime

I2C_ADDR = 0x27
LCD_WIDTH = 16

bus = smbus.SMBus(1)

def lcd_init():
    lcd_write(0x33, 0x03)
    lcd_write(0x32, 0x03)
    lcd_write(0x28, 0x03)
    lcd_write(0x0C, 0x03)
    lcd_write(0x06, 0x03)
    lcd_write(0x01, 0x03)
    time.sleep(0.005)

def lcd_write(bits, mode):
    bits_high = mode | (bits & 0xF0) | 0x08
    bits_low = mode | ((bits << 4) & 0xF0) | 0x08

    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits | 0x04))
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits & ~0x04))
    time.sleep(0.0005)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_write(line, 0x80)

    for i in range(LCD_WIDTH):
        lcd_write(ord(message[i]), 0x40)

lcd_init()

student_id = "s1300107"
student_name = "rossi andy"

while True:
    lcd_string(student_id, 0x80)
    lcd_string(student_name, 0xC0)
    time.sleep(5)

    now = datetime.datetime.now()
    date_string = f"{now.year}.{now.month}.{now.day}"
    time_string = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"

    lcd_string(date_string, 0x80)
    lcd_string(time_string, 0xC0)
    time.sleep(5)