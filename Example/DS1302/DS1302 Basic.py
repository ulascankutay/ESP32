from machine import Pin
import ds1302
import time

ds = ds1302.DS1302(Pin(12),Pin(13),Pin(15))


ds.start()

ds.date_time() 


ds.date_time([2024, 04, 03, 3, 01, 22, 0]) 

while True :
    
    rtc_time = ds.date_time()
    print("{:02d}.{:02d}.{:04d} {:02d}:{:02d}:{:02d}:{:02d}".format(rtc_time[2], rtc_time[1], rtc_time[0], rtc_time[3], rtc_time[4], rtc_time[5], rtc_time[6]))
    time.sleep(1)
    
    
    if(rtc_time[4]==01 and rtc_time[5]==25 and rtc_time[6] == 50):
        print("mama zamanı")
        