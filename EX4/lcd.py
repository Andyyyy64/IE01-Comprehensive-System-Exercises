import smbus
import time

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