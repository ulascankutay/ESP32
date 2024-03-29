from machine import deepsleep
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)


led.value(1)
sleep(1)
led.value(0)
sleep(1)

#uykuya geçmeden bekleme
sleep(5)

print('derin uyku başlıyor')

#10 saniye boyunca derin uyku
deepsleep(10000)

