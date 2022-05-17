import machine

buttons = []

pins = [2,3,4,5,6,7,8,9]


for i in range(0, len(pins)):
    ele =  machine.Pin(pins[i], machine.Pin.IN, machine.Pin.PULL_DOWN)
    buttons.append(ele)

while True:
  cont = 0
  for i in range(0, len(pins)):
    if (buttons[i].value()==0):
      cont+=2**i
  print(cont)