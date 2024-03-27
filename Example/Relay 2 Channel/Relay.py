from machine import Pin
from time import sleep


relay = Pin(26, Pin.OUT)
relay2 = Pin(27, Pin.OUT)

relay2. value(0)

while True:
  relay.value(0)
  sleep(2)
  relay.value(1)
  sleep(2)
   
"""
Role bağlantı sırası

NO  (Normally Open)
COM (mains voltage)
NC  (Normally Closed)



"""