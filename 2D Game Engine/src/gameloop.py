import sys
import pygame
import numpy 
from Entity import *


pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

running = True

c1 = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    if(pygame.mouse.get_pressed()[0]):
        circle = Entity(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if (not circle.isDrawn):
            circle.isDrawn = True
            pygame.draw.circle(screen, "black", (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 25)
            e1 = EntityManager(circle)  
        # c1 = circle
        

    else:
        continue
    

    print("circle", circle.px, circle.py)  
    
    print(e1.totalObjs)

    pygame.draw.circle(screen, "red", (width/2, height/2), 25)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(144)  # limits FPS to 60

pygame.quit()