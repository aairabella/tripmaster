import machine
import time
from machine import ADC

#setup
led = machine.Pin(25, machine.Pin.OUT) # LED on the board

adc = ADC(machine.Pin(34))
adc.atten(ADC.ATTN_11DB)

#loop
while True:
  if led.value() == 0:
    led.value(1)
    boton_adc = adc.read()
    if boton_adc < 1000:
      print('+')
    elif (boton_adc > 1000 and boton_adc < 2600):
      print('-')
    elif (boton_adc > 2600 and boton_adc < 3200):
      print('Set')
    
  else:
    led.value(0)
  
  time.sleep(0.5)
