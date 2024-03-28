import network

ssid ="ESP-32 AccessPoint"
ch = 5
sc=3
pwd = "nasoerm"
# wifi access point modunda ayarlama 
wifi = network.WLAN(network.AP_IF)
#Static ip atmama
wifi.ifconfig(('192.168.205.1', '255.255.255.0', '192.168.205.04', '192.168.105.1'))
#https://docs.micropython.org/en/latest/library/network.WLAN.html
wifi.config(essid=ssid,channel=ch,security=sc,key=pwd)

wifi.active(True)


