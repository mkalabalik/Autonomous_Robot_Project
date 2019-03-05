# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import cv2

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 300  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

int pulseWidth(int angle)
{
  int pulse_wide, analog_value;
  pulse_wide   = map(angle, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
  analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
  Serial.println(analog_value);
  return analog_value;
}


def callback(value):
    pass


def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)
    v = 0
    cv2.createTrackbar("val", "Trackbars", v, 800, callback)

def get_trackbar_values(range_filter):
    v = cv2.getTrackbarPos("val", "Trackbars")
    #values.append(v)
    return v


#setup_trackbars(3)
##def servoHareket(deger):
##    for i in range(deger):

def servoOynat(kanal, simdiki, sonraki):
    if sonraki > simdiki:
        delta = 1
    elif sonraki < simdiki:
        delta = -1
    
    while not simdiki == sonraki:
        pwm.set_pwm(kanal, 0, simdiki)
        time.sleep(0.01) 
        simdiki = simdiki + delta
    return sonraki

servoileri = 15
servoyukari = 14

valuefirst = 450
value11=450
value12=450
pwm.set_pwm(servoileri, 0, valuefirst)
pwm.set_pwm(servoyukari, 0, valuefirst)

while True:
    a=input("Bir sayı gir: ")
    if a=="1":
        pwm.set_pwm(servoileri, 0, 400)
        pwm.set_pwm(servoyukari, 0, 400)
        #value11 = servoOynat(servoileri, value11, value11-10*1)
        #value11-=10
        #pwm.set_pwm(servoileri, 0, value11)
        print("simdi "+str(value11))
    elif a=="2":
        value11 = servoOynat(servoileri, value11, value11+10*1)
        #value11+=10
        #pwm.set_pwm(servoileri, 0, value11)
        print("simdi "+str(value11))
    elif a=="4":
        value12 = servoOynat(servoyukari, value12, value12-10*1)
        #value12-=10
        #pwm.set_pwm(servoyukari, 0, value12)
        print("simdi "+str(value12))
    elif a=="5":
        value12 = servoOynat(servoyukari, value12, value12+10*1)
        #value12+=10
        #pwm.set_pwm(servoyukari, 0, value12)
        print("simdi "+str(value12))
    else:
        pwm.set_pwm(servoileri, 0, valuefirst)
        pwm.set_pwm(servoyukari, 0, valuefirst)
        GPIO.cleanup()
        break


##    pwm.set_pwm(11, 0, servo_min)
##    time.sleep(3)
##    print("asd")
##    pwm.set_pwm(11, 0, servo_max)
     #pwm.set_pwm(11, 0, value)
     #pwm.set_pwm(15, 0, value)
    if cv2.waitKey(1) & 0xFF == 27:
        break
