# -*- coding: utf-8 -*-
# python dynamic_color_tracking.py --filter HSV --webcam
from threading import Thread
import cv2
import argparse
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
from imutils.video import WebcamVideoStream
import imutils
from time import sleep
import pygame
import sys
import time
import RPi.GPIO as GPIO

# Define some variable
##BLACK = (0, 0, 0)

# pygame.init()

# Set the width and height of the screen [width, height]
#size = (500, 500)
#screen = pygame.display.set_mode(size)

# pygame.display.set_caption("Robot")


# Used to manage how fast the screen updates
#clock = pygame.time.Clock()

# robot init
# kurulum()
#############################################  ROBOT  ##########################################
class Robot():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

##        self.pwm = Adafruit_PCA9685.PCA9685()
# self.pwm.set_pwm_freq(500)

        # Mesafe sensörü pinleri
        self.mesafeTrig = 31
        self.mesafeEcho = 32

        # motorların input pinleri
        self.motorSolA = 38
        self.motorSolB = 37

        self.motorSagA = 36
        self.motorSagB = 35

        self.motor2A = 11
        self.motor2B = 13
        self.pwmPin = 7

        # Motorların hızı
        self.hiz = 0  # 0..100 arası
        ##self.hizfark = 20

        # pinlerin modları
        GPIO.setup(self.mesafeTrig, GPIO.OUT)
        GPIO.setup(self.mesafeEcho, GPIO.IN)

        GPIO.setup(self.motorSolA, GPIO.OUT)
        GPIO.setup(self.motorSolB, GPIO.OUT)
        GPIO.setup(self.motorSagA, GPIO.OUT)
        GPIO.setup(self.motorSagB, GPIO.OUT)
        GPIO.setup(self.pwmPin, GPIO.OUT)

        self.PWM = GPIO.PWM(self.pwmPin, 100)
        self.PWM.start(0)
        # self.PWM.ChangeDutyCycle(10)

    def mesafe(self):
        GPIO.output(self.mesafeTrig, GPIO.LOW)
        time.sleep(2)

        GPIO.output(self.mesafeTrig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.mesafeTrig, GPIO.LOW)

        while GPIO.input(self.mesafeEcho) == 0:
            # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            # self.dur()
            # self.temizle()
            print("burda")
            pulseIlk = time.time()
        while GPIO.input(self.mesafeEcho) == 1:
            pulseSon = time.time()
            print("şurda")

        pulseSuresi = pulseSon - pulseIlk

        mesafe = pulseSuresi * 17150
        mesafe = round(mesafe, 2)

        print(mesafe)

    def ileri(self):
        print("İleri hareket")
        GPIO.output(self.motorSolA, GPIO.HIGH)
        GPIO.output(self.motorSolB, GPIO.LOW)

        GPIO.output(self.motorSagA, GPIO.HIGH)
        GPIO.output(self.motorSagB, GPIO.LOW)

    def geri(self):
        print("Geri hareket")
        GPIO.output(self.motorSolA, GPIO.LOW)
        GPIO.output(self.motorSolB, GPIO.HIGH)

        GPIO.output(self.motorSagA, GPIO.LOW)
        GPIO.output(self.motorSagB, GPIO.HIGH)

    def hizAyari(self):
        self.pwm.ChangeDutyCycle(self.hiz)
        self.pwm.set_pwm(15, 0, self.hiz)  # self.pwm.set_pwm(channel,on,off)
        ##print("Hiz: {}".format(self.hiz))

    def hizAzalt(self, deger):
        self.hiz = self.hiz - deger
        if self.hiz < 0:
            self.hiz = 0
        self.hizAyari()
        print("Hız AZALDI---")

    def hizArtir(self, deger):
        self.hiz = self.hiz + deger
        if self.hiz > 100:
            self.hiz = 100
        self.hizAyari()
        print("Hız ARTTI+++")

    def sagaDon(self):
        print("Saga Dönüyor")
        GPIO.output(self.motorSolA, GPIO.HIGH)
        GPIO.output(self.motorSolB, GPIO.LOW)

        GPIO.output(self.motorSagA, GPIO.LOW)
        GPIO.output(self.motorSagB, GPIO.HIGH)

    def solaDon(self):
        print("Sola Dönüyor")
        GPIO.output(self.motorSolA, GPIO.LOW)
        GPIO.output(self.motorSolB, GPIO.HIGH)

        GPIO.output(self.motorSagA, GPIO.HIGH)
        GPIO.output(self.motorSagB, GPIO.LOW)

    def dur(self):
        ##        self.hiz = 0
        # self.hizAyari()
        print("Durdu")
        GPIO.output(self.motorSolA, GPIO.LOW)
        GPIO.output(self.motorSolB, GPIO.LOW)

        GPIO.output(self.motorSagA, GPIO.LOW)
        GPIO.output(self.motorSagB, GPIO.LOW)

    def temizle(self):
        GPIO.cleanup()
        print("Temizlendi")
        print("Çıkılıyor")
        sys.exit()


class WebcamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
                # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True


class PiVideoStream:
    def __init__(self, resolution=(320, 240), framerate=32):
        # initialize the camera and stream
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture,
                                                     format="bgr", use_video_port=True)

        # initialize the frame and the variable used to indicate
        # if the thread should be stopped
        self.frame = None
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        for f in self.stream:
            # grab the frame from the stream and clear the stream in
            # preparation for the next frame
            self.frame = f.array
            self.rawCapture.truncate(0)

            # if the thread indicator variable is set, stop the thread
            # and resource camera resources
            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True


def callback(value):
    pass


def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)

    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255

        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


def get_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--filter', required=True,
                    help='Range filter. RGB or HSV')
    ap.add_argument('-w', '--webcam', required=False,
                    help='Use webcam', action='store_true')
    args = vars(ap.parse_args())

    if not args['filter'].upper() in ['RGB', 'HSV']:
        ap.error("Please speciy a correct filter.")

    return args


def get_trackbar_values(range_filter):
    values = []

    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)
    return values


def main():
    robot = Robot()
    # robot.hizAzalt(100)
    # robot.hizArttir(10)
    # robot.PWM.ChangeDutyCyle(10)
    args = get_arguments()

    range_filter = args['filter'].upper()

    stream = PiVideoStream().start()
    setup_trackbars(range_filter)

    mod = -1
    eskimod = -1

    while True:
        image = vs.read()

        if range_filter == 'RGB':
            frame_to_thresh = image.copy()
        else:
            frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
        # Yesil renk
        v1_min = 40
        v2_min = 143
        v3_min = 65
        v1_max = 114
        v2_max = 255
        v3_max = 255
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        mod = -1
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            midpoint = 40
            # only proceed if the radius meets a minimum size
            if ((radius > 10) and (radius < 210)):
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(image, center, 3, (0, 0, 255), -1)
                if(int(x) < (319 - midpoint)):
                    cv2.putText(image, "sola don", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                    mod = 1
                    # robot.solaDon()
                    # sleep(0.1)
                    # robot.dur()
                elif(int(x) > (319 + midpoint)):
                    cv2.putText(image, "saga don", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                    mod = 3
                    # robot.sagaDon()
                    # sleep(0.1)
                    # robot.dur()
                else:
                    mod = 2
                    # robot.ileri()

                    # sleep(0.1)
                    # robot.dur()
                    cv2.putText(image, "ilerle", (center[0] + 10, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                cv2.putText(image, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            else:
                mod = -1
        else:
            mod = -1

        # robot.dur()
        # sleep(0.1)

        if(mod == eskimod):
            robot.dur()
            sleep(1)
            print("uyu")
        if(mod == 1):
            robot.solaDon()
            print("soladon moduna gecildi")
        elif(mod == 2):
            robot.ileri()
            print("ileri moduna gecildi")
        elif(mod == 3):
            robot.sagaDon()
            print("sagadon moduna gecildi")
        else:
            robot.dur()
            print("dur moduna gecildi")
        eskimod = mod

        # show the frame to our screen
        cv2.imshow("Original", image)
        #cv2.imshow("Thresh", thresh)
        #cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xFF is ord('q'):
            robot.dur()
            robot.temizle()
            break


if __name__ == '__main__':
    main()
