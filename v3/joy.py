"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame, sys
import Adafruit_PCA9685

# Define some variable
##BLACK = (0, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (100, 100)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Robot")

# Loop until the user clicks the close button.
done = False

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
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(500)
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        #motorların input pinleri
        self.motor1A = 16
        self.motor1B = 18
        #self.motor2A = 11
        #self.motor2B = 13

        #Motorların hızı
        self.hiz = 0 #0..500 arası
        
        #pinlerin modları
        GPIO.setup(self.motor1A, GPIO.OUT)
        GPIO.setup(self.motor1B, GPIO.OUT)

    
    def ileri(self):
        print("İleri hareket")
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)

    def geri(self):
        print("Geri hareket")
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)

    def hizAyari(self, hiz):
        pwm.set_pwm(0,0,hiz) #pwm.set_pwm(channel,on,off)

    def hizAzalt(deger):
        self.hiz = self.hiz-deger
        if self.hiz < 0:
            self.hiz = 500
        self.hizAyari()

    def hizArtir(deger):
        self.hiz = self.hiz+deger
        if self.hiz > 500:
            self.hiz = 500
        self.hizAyari()

    def sagaDon(self):
        pass
    
    def solaDon(self):
        pass

    def dur(self):
        self.hizAyari(0)

    def temizle(self):
        pass

##############################################  MAIN  ##########################################
def main(Robot):
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
    ##        print(event)
            if event.type == pygame.QUIT:
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
                    Robot.hizArtir()
                if event.value == (1, 0): #print("hız arttırıldı")
                    Robot.hizAzalt()
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
