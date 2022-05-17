# My first MicroPython example of a 7-segment
# ascending/descending hexadecimal counter
# by Anderson Costa, created on 05.06.2021

from machine import Pin
from utime import sleep

#       A
#      ---
#  F |  G  | B
#      ---
#  E |     | C
#      ---
#       D

pins = [
  Pin(2, Pin.OUT), # A
  Pin(3, Pin.OUT), # B
  Pin(4, Pin.OUT), # C
  Pin(5, Pin.OUT), # D
  Pin(6, Pin.OUT), # E
  Pin(7, Pin.OUT), # F
  Pin(8, Pin.OUT), # G
  Pin(9, Pin.OUT), # G
  Pin(10, Pin.OUT), # G
  Pin(11, Pin.OUT), # G
  Pin(0, Pin.OUT) # DP (not connected)
]

# Common anode 7 segment
digits = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 0
  [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], # 0
  [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], # 0
  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], # 0
  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], # 0
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], # 0
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], # 0
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], # 0
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0] # 0
]

def reset():
  for pin in pins:
    pin.value(1)

reset()

switch = Pin(12, Pin.IN)

while True:
  if switch.value() == 1:
    for i in range(len(digits)):
      if switch.value() == 0:
        break;      
      for j in range(len(pins) - 1):
        pins[j].value(digits[i][j])
      sleep(0.5)
  else:
    for i in range(len(digits) - 1, -1, -1): 
      if switch.value() == 1:
        break;      
      for j in range(len(pins)):
        pins[j].value(digits[i][j])
      sleep(0.5)
