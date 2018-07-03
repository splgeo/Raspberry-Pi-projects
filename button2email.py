# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        import smtplib
        
        to = '###########'
        gmail_user = '###############'
        gmail_pwd = '######'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        msg = '\n this is a test \n\n'
        server.sendmail(gmail_user, to, msg)
        server.close()

        time.sleep(120)
        
                
        
