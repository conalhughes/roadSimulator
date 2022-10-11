import pygame
import time

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500

# create background
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
xCoord = 200
xCoord2 = 750
yCoord = 200
while running:

    # # check if user has cancelled the game
    for event in pygame.event.get():

        # user has quit the game
        if event.type == QUIT:
            running = False

        # a key has been pressed
        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE: # esc
                running = False

    # place car image
    png = pygame.image.load("car.png")
    car = pygame.Surface((250,141)) # size of png
    car.blit(png, (0,0))
    screen.blit(car, (75, 50))  


    # make surface black again
    leftbug = pygame.Surface((5,100))
    leftbug.fill((0,0,0))
    screen.blit(leftbug, (0,yCoord))
    surfBlack1 = pygame.Surface((1, 100))
    surfBlack1.fill((0,0,0))
    surfBlack2 = pygame.Surface((1, 100))
    surfBlack2.fill((0,0,0))

    # if xCoord < 350:
    screen.blit(surfBlack1, (xCoord+300, yCoord))

    # if xCoord2 < 350:
    screen.blit(surfBlack2, (xCoord2+300, yCoord))

    # middle line(s)
    if xCoord < 0:
        surf1 = pygame.Surface((300 + xCoord, 100))
    elif xCoord > 500:
        surf1 = pygame.Surface((750 - xCoord, 100))
    else:
        surf1 = pygame.Surface((300, 100))
    surf1.fill((255,255,255))

    if xCoord2 < 0:
        surf2 = pygame.Surface((300 + xCoord2, 100))
    elif xCoord2 > 500:
        surf2 = pygame.Surface((750 - xCoord2, 100))
    else:
        surf2 = pygame.Surface((300, 100))
    surf2.fill((255,255,255))


    screen.blit(surf1, (xCoord, yCoord))
    screen.blit(surf2, (xCoord2, yCoord))
    
    
       
    pygame.display.flip()
    xCoord = xCoord -1
    xCoord2 = xCoord2 -1
    if xCoord == -299:
        xCoord = 750
    if xCoord2 == -299:
        xCoord2 = 750
    time.sleep(0.01)

pygame.quit()
        