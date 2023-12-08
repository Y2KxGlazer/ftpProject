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
    def __init__(self, entity) -> None:
        self.allObjs.append(entity)
        EntityManager.totalObjs += 1