import RPi.GPIO as GPIO
##from time import sleep
import sys

Motor1A = 16
Motor1B = 18
Motor1E = 22

def kurulum():
    GPIO.setmode(GPIO.BOARD)
    
    #Motor1A = 16
    #Motor1B = 18
    #Motor1E = 22

##    Motor2A = 38 #16
##    Motor2B = 36 #18
##    Motor2E = 32 #22
##
##    Motor3A = 11 #16
##    Motor3B = 13 #18
##    Motor3E = 15 #22
##
##    Motor4A = 33 #16
##    Motor4B = 31 #18
##    Motor4E = 29 #22

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

##    GPIO.setup(Motor2A,GPIO.OUT)
##    GPIO.setup(Motor2B,GPIO.OUT)
##    GPIO.setup(Motor2E,GPIO.OUT)
##
##    GPIO.setup(Motor3A,GPIO.OUT)
##    GPIO.setup(Motor3B,GPIO.OUT)
##    GPIO.setup(Motor3E,GPIO.OUT)
##
##    GPIO.setup(Motor4A,GPIO.OUT)
##    GPIO.setup(Motor4B,GPIO.OUT)
##    GPIO.setup(Motor4E,GPIO.OUT)
    print("Kurulum tamamlandı")
    
def ileri():
    print("İleri hareket")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

##    GPIO.output(Motor2A,GPIO.HIGH)
##    GPIO.output(Motor2B,GPIO.LOW)
##    GPIO.output(Motor2E,GPIO.HIGH)
##
##    GPIO.output(Motor3A,GPIO.HIGH)
##    GPIO.output(Motor3B,GPIO.LOW)
##    GPIO.output(Motor3E,GPIO.HIGH)
##
##    GPIO.output(Motor4A,GPIO.HIGH)
##    GPIO.output(Motor4B,GPIO.LOW)
##    GPIO.output(Motor4E,GPIO.HIGH)

def geri():
    print("Geri hareket")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

##    GPIO.output(Motor2A,GPIO.LOW)
##    GPIO.output(Motor2B,GPIO.HIGH)
##    GPIO.output(Motor2E,GPIO.HIGH)
##
##    GPIO.output(Motor3A,GPIO.LOW)
##    GPIO.output(Motor3B,GPIO.HIGH)
##    GPIO.output(Motor3E,GPIO.HIGH)
##
##    GPIO.output(Motor4A,GPIO.LOW)
##    GPIO.output(Motor4B,GPIO.HIGH)
##    GPIO.output(Motor4E,GPIO.HIGH)
    
def dur():         
    GPIO.output(Motor1E,GPIO.LOW)
##    GPIO.output(Motor2E,GPIO.LOW)
##    GPIO.output(Motor3E,GPIO.LOW)
##    GPIO.output(Motor4E,GPIO.LOW)

    print("Motor durdu")
    
##def dongu():
##    pass

##kurulum()
##dongu()

def temizle():
    GPIO.cleanup()
    print("Pinler temizlendi")
    cikis()
def cikis():
    sys.exit()