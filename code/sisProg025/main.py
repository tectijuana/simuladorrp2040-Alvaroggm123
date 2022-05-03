# -------------------------------- #
# Sistemas programables            #
# Practica 2                       #
# González Martínez Álvaro Gabriel #
# -------------------------------- #

from machine import Pin
from time import sleep

led0 = Pin(6, Pin.OUT)
led1 = Pin(7, Pin.OUT)
led2 = Pin(8, Pin.OUT)
push_button0 = Pin(2, Pin.IN)
push_button1 = Pin(3, Pin.IN)
push_button2 = Pin(4, Pin.IN)

led.value(0)

while True:
    if push_button0.value() == True:
        led0.value(0)
    elif push_button1.value() == True:
        led1.value(0)
    elif push_button2.value() == True:
        led2.value(0)
    else:
        led0.value(1)
        led1.value(1)
        led2.value(1)