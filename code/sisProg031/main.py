# -------------------------------- #
# Sistemas programables            #
# Practica 2                       #
# González Martínez Álvaro Gabriel #
# -------------------------------- #

from machine import Pin
from utime import sleep

led = Pin(2, Pin.OUT)
push_button = Pin(28, Pin.IN)

led.value(0)

while True:
    logic_state = push_button.value()
    if logic_state == True:
        led.value(0)
    else:
        led.value(1)
    sleep(.5)