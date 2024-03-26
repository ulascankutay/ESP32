"""from machine import Pin,PWM

pwm = PWM(Pin(2),freq=100, duty=20 )
pwm.freq()
print(pwm.freq())
pwm.duty()
print(pwm.duty())

pwm.deinit()"""
from machine import Pin, PWM
from time import sleep

fr = 1000
dty = 0

while True:
    pwm = PWM (Pin (2), freq=fr, duty=dty)
    sleep(1)
    dty = dty + 10
    if dty > 1000: dty = 0
    print(dty)