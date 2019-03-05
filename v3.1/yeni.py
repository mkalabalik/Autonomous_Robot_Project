"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame, sys, time
#import Adafruit_PCA9685
import RPi.GPIO as GPIO

# Define some variable
##BLACK = (0, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Robot")


# Used to manage how fast the screen updates
clock = pygame.time.Clock()



############################################  JOYSTICK  ########################################
pygame.joystick.init()  #print(pygame.joystick.get_count())
fjoy = pygame.joystick.Joystick(0)
fjoy.init()


#robot init
#kurulum()
#############################################  ROBOT  ##########################################
class Robot():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

##        self.pwm = Adafruit_PCA9685.PCA9685()
##        self.pwm.set_pwm_freq(500)

        #Mesafe sensörü pinleri
        self.mesafeTrig = 31
        self.mesafeEcho = 32

        #motorların input pinleri
        self.motorSolA = 38
        self.motorSolB = 37
        
        self.motorSagA = 36
        self.motorSagB = 35
        
        #self.motor2A = 11
        #self.motor2B = 13
        #self.pwmPin= 7

        #Motorların hızı
##        self.hiz = 0 #0..100 arası
##        self.hizfark = 20
        
        #pinlerin modları
        GPIO.setup(self.mesafeTrig, GPIO.OUT)
        GPIO.setup(self.mesafeEcho, GPIO.IN)
        
        GPIO.setup(self.motorSolA, GPIO.OUT)
        GPIO.setup(self.motorSolB, GPIO.OUT)
        GPIO.setup(self.motorSagA, GPIO.OUT)
        GPIO.setup(self.motorSagB, GPIO.OUT)
##        GPIO.setup(self.pwmPin, GPIO.OUT)

##        self.pwm = GPIO.PWM(self.pwmPin, 100)
##        self.pwm.start(0)

    def mesafe(self):
        GPIO.output(self.mesafeTrig, GPIO.LOW)
        time.sleep(2)

        GPIO.output(self.mesafeTrig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.mesafeTrig, GPIO.LOW)

        while GPIO.input(self.mesafeEcho) == 0:
##            for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                    self.dur()
##                    self.temizle()
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

##    def hizAyari(self):
##        self.pwm.ChangeDutyCycle(self.hiz)
####        self.pwm.set_pwm(15,0,self.hiz) #self.pwm.set_pwm(channel,on,off)
##        print("Hiz: {}".format(self.hiz))

##    def hizAzalt(self,deger):
##        self.hiz = self.hiz-deger
##        if self.hiz < 0:
##            self.hiz = 0
##        self.hizAyari()
##        print("Hız AZALDI---")

##    def hizArtir(self,deger):
##        self.hiz = self.hiz+deger
##        if self.hiz > 100:
##            self.hiz = 100
##        self.hizAyari()
##        print("Hız ARTTI+++")

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
##        self.hizAyari()
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

##############################################  MAIN  ##########################################
def main(Robot):
    # Loop until the user clicks the close button.
    done = False
    # -------- Main Program Loop -----------
    while not done:
        #Robot.mesafe()
        
        # --- Main event loop
        for event in pygame.event.get():
    ##        print(event)
            if event.type == pygame.QUIT:
                Robot.dur()
                Robot.temizle()
                done = True
            if event.type == pygame.JOYBUTTONDOWN:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 8:
                        Robot.dur()
                        Robot.temizle()
            if event.type == pygame.JOYBUTTONUP:
                pass
##                print("buton bırakıldı")
            if event.type == pygame.JOYAXISMOTION:
                pass
##                print("axis hareketi")
            if event.type == pygame.JOYHATMOTION: #value=(orijin'e göre konum)
                if event.value == (0, 0): #print("hareket olmasın")
                    Robot.dur()
                if event.value == (0, -1): #print("geri hareket etsin")
                    Robot.geri()
                if event.value == (0, 1): #print("ileri hareket etsin")
                    Robot.ileri()
                if event.value == (-1, 0): #print("hız azaltıldı")
                    Robot.solaDon()
                    #Robot.hizAzalt(Robot.hizfark)
                if event.value == (1, 0): #print("hız arttırıldı")
                    Robot.sagaDon()
                    #print(Robot.hiz)
                    #Robot.hizArtir(Robot.hizfark)
                    #print(Robot.hiz)
        # --- Game logic should go here

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
    ##    screen.fill(WHITE)

        # --- Drawing code should go here

        # --- Go ahead and update the screen with what we've drawn.
    ##    pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)



Robot = Robot()
main(Robot)

# Close the window and quit.
pygame.quit()
