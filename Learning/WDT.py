from machine import WDT

# wdt süresi ayarlama milisaniye 
wdt = WDT(timeout = 5000)
"""

tekrarlanmayan kodlar 

"""
while True :
"""


Sonsuz dongü içerisinde çalışacak kodlar


"""

# sonsuz dongü içerisinde wdt sıfırlanması
wdt.feed() 