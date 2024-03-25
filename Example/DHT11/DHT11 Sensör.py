from machine import Pin
from time import sleep
import dht 
 
sensor = dht.DHT11(Pin(0))

def dht_sensor():
    try:
        sleep(2)
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        print(t)
        print('Sıcaklık: %3.1f C' %t)
        print('Nem: %3.1f %%' %h)
    except OSError as e:
        print('sensör okunmadı')
    
 
while True:
    dht_sensor()
    sleep(2)
