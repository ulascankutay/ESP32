from machine import Pin,SoftI2C
import ssd1306
import gfx
import time

i2c = SoftI2C(scl=Pin(5),sda=Pin(4))

oled=ssd1306.SSD1306_I2C(128,64,i2c)
while True :
    oled.text("SELAM ssd1306",0,0,1)
    oled.text(" ile oled ",0,10,1 )
    time.sleep(1)
    oled.show()

    time.sleep(2)
    oled.fill(1)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
