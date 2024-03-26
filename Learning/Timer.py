from machine import Timer

def TIM0_Callback(timer):
    print("1")

def TIM1_Callback(timer):
    print("2")

tim0 = Timer(0)
tim1 = Timer(1)

tim0.init(period=5000, mode=Timer.PERIODIC, callback=TIM0_Callback)
tim1.init(period=5000, mode=Timer.PERIODIC, callback=TIM1_Callback)
