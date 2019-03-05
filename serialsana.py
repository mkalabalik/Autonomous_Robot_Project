#!/usr/bin/python3
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

# read from Arduino
#input = ser.read()

#print("Read input " + input.decode("utf-8") + " from Arduino")


while True:
        # write something back

        #ser.write(b'A')

        # read response back from Arduino
        input = ser.readline()
        print(type(input))
        #input_number = ord(input)
        speed = int(str(input)[2:-5])
        print(speed)
        #print("Read input " + input.decode("utf-8") + " from Arduino")
        
##        for i in range (0,3):
##
##                input = ser.read()
##
##                input_number = ord(input)
##
##                print ("Read input back: " + str(input_number))

##        time.sleep(1)
