# -*- coding: utf-8 -*-

from tkinter import *
from PIL import ImageTk, Image
import os, time, sys
import Main
import picamera
import serial

strLicense = "34ZT1451fff"
hiz = 0.01
hizLimiti = 2999

WINDOWWIDTH = 972 #324*3
WINDOWHEIGHT = 486


class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Plaka Tanıma")
        self.geometry("{}x{}+100+100".format(WINDOWWIDTH, WINDOWHEIGHT))

        self.strLicence = strLicense
        self.speed = hiz
        self.speedLimit = hizLimiti

        #Camera
        self.camera = picamera.PiCamera()
        self.camera.close()

        #Serial connection
        self.serial = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

        #Left frame
        self.frameLeft = Frame(self)
        self.frameLeft.place(x = 0, y = 0, height = 486, width = 324)
        self.frameRight = Frame(self)
        self.frameRight.place(x = WINDOWWIDTH/3, y = 0)
        #self.frameRight.pack(side = "right")

        #Read images
        self.imgOriginalSceneGui = ImageTk.PhotoImage(Image.open("imgOriginalSceneGui.png"))
        self.imgLicense = ImageTk.PhotoImage(Image.open("imgLicenseGui.png"))
        self.imgLicenseChars = ImageTk.PhotoImage(Image.open("imgLicenseCharsGui.png"))

        #Entry of Speed
        self.entrySpeed = Entry(self.frameLeft, width = 4, font=("Calibri",40))
        self.entrySpeed.insert(0, self.speed)
        self.entrySpeed.place(x = 2*WINDOWWIDTH/20, y = 1*WINDOWHEIGHT/6)
        #entryLicense.grid(column=1, row=3, padx=20, pady=20)

        #Buttons
        self.var = IntVar()
        self.Button1 = Radiobutton(self.frameLeft, text = "Option radardan ",
                                   variable = self.var,value = 1, command = self.fromRadar)
        self.Button2 = Radiobutton(self.frameLeft, text = "Option kameradan",
                                   variable = self.var, value = 2, command = self.fromCamera)
        self.Button3 = Radiobutton(self.frameLeft, text = "Option klasörden",
                                   variable = self.var, value = 3, command = self.fromDirectory)
        self.Button1.place(x = 0, y = 0*WINDOWHEIGHT/18)
        self.Button2.place(x = 0, y = 1*WINDOWHEIGHT/18)
        self.Button3.place(x = 0, y = 2*WINDOWHEIGHT/18)

        #When close the window, run exit function
        self.protocol('WM_DELETE_WINDOW', self.exitFunction)

        #Start main function
        self.main()

    def putImages(self):
        """
        Put the images on GUI
        """

        #Left frame
        self.labelLicense = Label(self.frameLeft, image = self.imgLicense)
        self.labelLicense.place(x = 0, y = 3*WINDOWHEIGHT/6)
        #self.labelLicense.grid(column=1, row=1)

        self.labelLicenseThresh = Label(self.frameLeft, image = self.imgLicenseChars)
        self.labelLicenseThresh.place(x = 0, y = 4*WINDOWHEIGHT/6)
        #self.labelLicenseThresh.grid(column=1, row=2, padx=20, pady=20)

        self.entryLicense = Entry(self.frameLeft, width = len(strLicense), font=("Calibri", 40))
        self.entryLicense.insert(0, strLicense)
        self.entryLicense.place(x = WINDOWWIDTH/20, y = 5*WINDOWHEIGHT/6)
        #self.entryLicense.grid(column=1, row=3, padx=20, pady=20)

        #Right frame
        self.labelImageOriginal = Label(self.frameRight, image = self.imgOriginalSceneGui)
        self.labelImageOriginal.pack(side = "left") #, fill = "both", expand = "yes"

    def cameraClose(self):
        self.camera.close()
        
    def cameraOpen(self):
        if self.camera.closed:
            self.camera = picamera.PiCamera()
            time.sleep(1)
        
    def takePhoto(self):
        print("takePhoto doesnt work")
        self.camera.capture("imgOriginalScene.png")
        
    def refreshImages(self):
        self.labelImageOriginal.destroy()
        self.labelImageOriginal.destroy()
        self.labelImageOriginal.destroy()
        self.imgOriginalSceneGui = ImageTk.PhotoImage(Image.open("imgOriginalSceneGui.png"))
        self.imgLicense = ImageTk.PhotoImage(Image.open("imgLicenseGui.png"))
        self.imgLicenseChars = ImageTk.PhotoImage(Image.open("imgLicenseCharsGui.png"))

    def speedFromSerial(self):
        try:
            bytesDataFromSerial = self.serial.readline()
            #print(bytesDataFromSerial)
            strSpeedFromData = str(bytesDataFromSerial)[2:-5]
            
            intSpeed = int(strSpeedFromData)
##        except (SystemExit, KeyboardInterrupt):
##            print("Keyboarddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
##            self.exitFunction()
        except:
            print(sys.exc_info()[0])
            print("-----------------")
            print(sys.exc_info()[1])
            print("-----------------")
            print(sys.exc_info()[2])
            print("-----------------")
            intSpeed = -1
        return intSpeed
    
    def fromRadar(self):
        print("Reading speed from radar...")
        while True:
            self.speed = self.speedFromSerial()
            self.entrySpeed.insert(0, self.speed)
            self.entrySpeed.update()
            print(self.speed)
            if self.speed > self.speedLimit:
                print("ALERT ALERT ALERT.yt.tYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                #self.fromCamera()
    
    def fromDirectory(self):
        self.cameraClose()
        print("Reading file from directory")
        Main.main("resim13.jpg")
        self.refreshImages()
        self.main()        
    def fromCamera(self):
        print("Reading file from camera")
        self.cameraOpen()
        self.takePhoto()
        Main.main()
        self.refreshImages()
        self.main()
        
    def exitFunction(self):
        self.destroy()
        #self.after(1250, self.destroy)
        print("exit function running")
        
    def main(self):
        self.putImages()
        
gui = Gui()
gui.mainloop()

