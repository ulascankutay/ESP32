from machine import Pin
from time import sleep

# pinler
relay_pins = [23, 22, 1, 3]

# pin nesnelerini tutacak liste
relay = []

# pin atamaları 
for pin in relay_pins:
    relay.append(Pin(pin, Pin.OUT,value=1))

#kontrol fonksiyonu 
def control_relay(kanal, durum):
    print("Kanal {} durumu: {}".format(kanal, durum))
    relay[kanal-1].value(durum)

while True:

     control_relay(1,0)
     sleep(1)
     control_relay(4,0)
     sleep(1)
     control_relay(1,1)
     break
