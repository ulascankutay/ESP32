from machine import Pin, ADC
from time import sleep


while True:
    adc   = ADC(Pin(34))
    value = adc.read_u16()
    Voltage = value * 0.05035
    print('ADC Value:',value, 'Voltage:',Voltage,'mV')
    sleep(1)
    
    # max 65535     3.3V
    # min 0         0V