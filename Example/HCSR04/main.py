from hcsr04 import HCSR04
from time import sleep

usensor = HCSR04(trigger_pin=12, echo_pin=14,echo_timeout_us=10000)

 
while True :
    try :
        mesafe = usensor.distance_cm()
        print(mesafe,"\n")
        sleep(2)
    except KeyboardInterrupt:
        pass 