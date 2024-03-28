import network

ssid ="***"
pwd = "****"
# wifi STA modunda ayarlama 
wifi = network.WLAN(network.STA_IF)
#wifi açma
wifi.active(True)
#wifi bağlanma
wifi.connect(ssid, pwd)
# static ip atama 
wifi.ifconfig(('192.168.2.031', '255.255.255.0', '192.168.11.1', '192.168.11.1'))
# bağlantı kontrol 
wifi.isconnected()