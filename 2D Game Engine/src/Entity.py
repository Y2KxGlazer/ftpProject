import pygame

    
class Entity:
    isDrawn = False
    px, py = 0, 0
    pygame.Vector2(px, py)
    def __init__(self, x, y) -> None:
        self.px, self.py = x, y
        EntityManager(self)
    
        
class EntityManager:
    allObjs = []
    totalObjs = 0
    
    def fixSize(): # Used to match the totalObjs instanted to the container that holds all of the objects
        EntityManager.totalObjs = len(EntityManager.allObjs)
        
    def checkDuplicates(entity): # Attempts to remove entities that have the same position(Currently done with x and y, will need a more advanced method later)
        if EntityManager.allObjs:
            if EntityManager.allObjs[-1].px == entity.px and EntityManager.allObjs[-1].py == entity.py:
                del EntityManager.allObjs[-1]
                EntityManager.fixSize()
                
    def __init__(self, entity) -> None:
        EntityManager.totalObjs += 1 # Counts twice because of the Entity(call)
        EntityManager.checkDuplicates(entity)
        EntityManager.allObjs.append(entity)
        
        
                
                

            

    