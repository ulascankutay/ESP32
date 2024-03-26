from machine import UART


uart2 = UART(0,baudrate=115200,rxbuf=18)


uart2.write('selam bebek\n')


# gelen mesaj bit sayısı
uart2.any()

# okuma 
uart2.read()


while True :
    
    if uart2.any() > 0 :
        data = uart2.read()
        if data == b'LED ON':
            LED.on()
            uart2.write("LED On yapildi\r\n")
        elif data == b'LED OFF':
            LED.off()
            uart2.write("LED Off yapildi\r\n")
        else:
            uart2.write("Komut Hatasi\r\n")












"""
uart kapatma
uart2.deinit()
"""