print("Hello, Pi Pico!")
'''
Using the MPU6050 inertial unit (accelerometer + gyroscope) with a Raspberry Pi Pico.
The Pico LED lights up when the MPU6050 is shaken.
For more info:
bekyelectronics.com/raspberry-pi-pico-and-mpu-6050-micropython/
'''

from imu import MPU6050  # https://bekyelectronics.com/raspberry-pi-pico-mcu6050/
import time
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
imu = MPU6050(i2c)

# LED initially off
Pin(25, Pin.OUT).value(0)

while True:
    # acceleration reading
    acceleration = imu.accel.magnitude
    print (acceleration)
    
    # value at rest is 1
    if abs(acceleration - 1) > 0.1:
        print("It is moving!")   
        Pin(25, Pin.OUT).value(1) # turn on the LED
    else: 
        Pin(25, Pin.OUT).value(0) # turn off the LED
        
    time.sleep(0.2)