from machine import ADC
import time
adc = ADC(0)            # create ADC object on ADC pin
adc.read()
while True :
    print(adc.read())
    time.sleep(1)