from machine import DAC, Pin

dac = DAC(Pin(25)) 
dac.write(128)      # deger aralığı 0-255 şuan % 50 