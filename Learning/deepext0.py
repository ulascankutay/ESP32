import esp32
from machine import Pin
from machine import deepsleep
from time import sleep


"""

        Bir tane gpıo pin tetikleme
#uyandırma butonu ---- rtc pinleri kullan
wake1 = Pin(14, mode = Pin.IN)

#tetikleme alındığı anda uyanma
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)


"""

  
  """ Birden çok gpıo pin tetilkleme"""
wake1 = Pin(14, mode = Pin.IN)
wake2 = Pin(25, mode = Pin.IN)


esp32.wake_on_ext1(pins = (wake1, wake2), level = esp32.WAKEUP_ANY_HIGH)


print('derin uyku 10saniye sonra basliyor')
sleep(10)
print('uykuda')
deepsleep()