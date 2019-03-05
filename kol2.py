import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
pwm=GPIO.PWM(15, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(15, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(15, False)
	pwm.ChangeDutyCycle(0)

SetAngle(30)
print("30")
sleep(5)
SetAngle(60)
print("60")
sleep(5)
SetAngle(0)
print("0")
pwm.stop()
GPIO.cleanup()
