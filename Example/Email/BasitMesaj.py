import umail
import time 

config =      {'host'       : 'smtp.gmail.com',
               'port'       : 587,
               'username'   : 'nameulas@gmail.com',
               'password'   : '',
               'from_name'  : 'ESP8266',
               'to_name'    : 'Ulas Can',
               'to'         : 'ulascankutay@gmail.com',
               'subject'    : 'Mail deneme esp8266 ile ',
               'text'       : 'Selam esp ile mail yollamayı deneyimledim6 '}


def  send_mail(congif):
    print("mail gönderiliyor..")
    smtp = umail.SMTP(config['host'], config['port'], username=config['username'], password=config['password'])
    smtp.to(config['to'])
    smtp.write("From: {0} <{0}>\n".format(config['from_name'], config['username']))
    smtp.write("To: {0} <{0}>\n".format(config['to_name'], config['to']))
    smtp.write("Subject: {0}\n".format(config['subject']))
    smtp.send(config['text'])
    smtp.quit()
    print("mail gönderildi")
    
    
while True :
    send_mail(config)
    time.sleep(1)
    break
