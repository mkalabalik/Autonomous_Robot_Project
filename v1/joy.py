"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame, sys
##import robot

# Define some colors
##BLACK = (0, 0, 0)
##WHITE = (255, 255, 255)
##GREEN = (0, 255, 0)
##RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (100, 100)
screen = pygame.display.set_mode(size)

pygame.joystick.init()
##print(pygame.joystick.get_count())
fjoy = pygame.joystick.Joystick(0)
fjoy.init()

#robot init
##robot.kurulum()

##pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
                    robot.dur()
                    robot.temizle()
        if event.type == pygame.JOYBUTTONUP:
            print("buton bırakıldı")
        if event.type == pygame.JOYAXISMOTION:
            print("axis hareketi")
        if event.type == pygame.JOYHATMOTION: #value=(orijin'e göre konum)
            if event.value == (0, 0): #print("hareket olmasın")
                robot.dur()
            if event.value == (0, -1): #print("geri hareket etsin")
                robot.geri()
            if event.value == (0, 1): #print("ileri hareket etsin")
                robot.ileri()
            
    
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

# Close the window and quit.
pygame.quit()
