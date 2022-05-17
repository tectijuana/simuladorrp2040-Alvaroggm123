import machine
from time import sleep_ms as delalay

stepper = []

pins = [2, 3, 5, 4]
# ----- BM,BP,AM,AP
for i in range(0, len(pins)):
    ele =  machine.Pin(pins[i], machine.Pin.OUT)
    stepper.append(ele)

cnt = 0
while True:
  delalay(100)
  stepper[0].value(0) #BM
  stepper[3].value(1) #AP
  delalay(100)
  stepper[3].value(0) #AP
  stepper[1].value(1) #BP
  delalay(100)
  stepper[1].value(0) #BP
  stepper[2].value(1) #AM
  delalay(100)
  stepper[2].value(0) #BM
  stepper[0].value(1) #AP
  delalay(100)
  cnt +=1
  print ("Cant de vueltas: ", end="")
  print (cnt)