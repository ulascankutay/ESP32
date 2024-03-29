from machine import RTC


rtc = RTC()


print(rtc.datetime())
      
print(str(rtc.datetime()[0])+" Yıl")
print(str(rtc.datetime()[1])+"  ay")
print(str(rtc.datetime()[2])+" gün")
print(str(rtc.datetime()[3])+" hangi gün") # 1 pazartesi 2 salı gibi 
print(str(rtc.datetime()[4])+" saat")
print(str(rtc.datetime()[5])+" dakika")





