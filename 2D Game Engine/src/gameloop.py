import sys
import pygame
import numpy 
import random as rd
from Entity import *


pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


copyScreen = None

running = True

clickTotal = 1 
def drawCircle():
            entity = Entity(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            # Can be commented out to remove the extra pink circle
            entity.isDrawn = True
            

while running:
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            drawCircle()
            
    for i in EntityManager.allObjs:
        pygame.draw.circle(screen, (40,40,40), (i.px, i.py), 20) #rd.randrange(0, 256),rd.randrange(0, 256),rd.randrange(0, 256) cycles through random colors, 
    # fill the screen with a color to wipe away anything from last frame
   

    pygame.draw.circle(screen, "red", (width/2, height/2), 25)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    #pygame.display.flip()
    
    
    
    
    pygame.display.update()
    
    clock.tick(144)  # limits FPS to 60

pygame.quit()