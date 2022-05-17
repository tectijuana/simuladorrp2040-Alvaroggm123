from machine import ADC
from time import sleep
from math import log

adc = ADC(26)

def ReadSens():
    value = adc.read_u16()
    return (value)
    #print("Analog value is: " + str(tempp))

def Celsius():
    tempVal = ReadSens()
    return (1/(log(1/(65535/tempVal-1))/3950+1/298.15)-273.15)

while True:
    print("La temperatura es: ", end="")
    print(Celsius())
    sleep(0.25)