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
# colour tuples
BLACK = (0,0,0)
WHITE = (255,255,255)

# Initialize pygame
pygame.init()

# constants
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500

PNG = pygame.image.load("car.png")

# create background
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
# line coordinates
xCoord = 200
xCoord2 = 750
yCoord = 225

#car coordinates
xPos = 75
yPos = 50

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = PNG
        self.rect = self.image.get_rect()

player = Player()

while running:

    #clear screen
    clear = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(clear, (0,0))
    CAR_POS = (xPos, yPos)

    # check if user has cancelled the game
    for event in pygame.event.get():

        # user has quit the game
        if event.type == QUIT:
            running = False

        # a key has been pressed
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE: # esc
                running = False

            elif event.key == K_UP:
                if yPos > 5:
                    yPos = yPos -5

            elif event.key == K_DOWN:
                if yPos < (SCREEN_HEIGHT - 141):
                    yPos = yPos +5

            elif event.key == K_LEFT:
                if xPos > 5:
                    xPos = xPos -5
                    
            elif event.key == K_RIGHT:
                if xPos < (SCREEN_WIDTH - 250):
                    xPos = xPos +5
        keypressed = pygame.key.get_pressed()

        if keypressed[K_DOWN]:
            if yPos < (SCREEN_HEIGHT - 141):
                yPos = yPos +5
        elif keypressed[K_UP]:
            if yPos > 5:
                yPos = yPos -5
        elif keypressed[K_LEFT]:
            if xPos > 5:
                xPos = xPos - 5
        elif keypressed[K_RIGHT]:
            if xPos < (SCREEN_WIDTH - 250):
                xPos = xPos +5
                    

    # middle line(s)
    if xCoord < 0:
        surf1 = pygame.Surface((300 + xCoord, 50))
    elif xCoord > 500:
        surf1 = pygame.Surface((750 - xCoord, 50))
    else:
        surf1 = pygame.Surface((300, 50))
    surf1.fill(WHITE)

    if xCoord2 < 0:
        surf2 = pygame.Surface((300 + xCoord2, 50))
    elif xCoord2 > 500:
        surf2 = pygame.Surface((750 - xCoord2, 50))
    else:
        surf2 = pygame.Surface((300, 50))
    surf2.fill(WHITE)


    screen.blit(surf1, (xCoord, yCoord))
    screen.blit(surf2, (xCoord2, yCoord))
    
    # place car image
    screen.blit(player.image, CAR_POS)
       
    pygame.display.flip()
    xCoord = xCoord -1
    xCoord2 = xCoord2 -1
    if xCoord == -299:
        xCoord = 750
    if xCoord2 == -299:
        xCoord2 = 750
    time.sleep(0.001)

pygame.quit()
        