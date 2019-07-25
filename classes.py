#Samyag Jhaveri

import pygame

class box:
    def __init__(self):
        self.rect=pygame.Rect(10,20,20,20)
        self.color=pygame.Color(0,0,0)

    def colorChange(self):
        self.color=pygame.Color(225,0,0)

class player:
    def __init__(self):
        self.box=box()

    def move(self,dir):
        if dir is 1:
            self.box.rect.move_ip(2,0)
        if dir is 2:
            self.box.rect.move_ip(-2,0)
        if dir is 3:
            self.box.rect.move_ip(0,-2)
        if dir is 4:
            self.box.rect.move_ip(0,2)



class objective:
    def __init__(self):
        self.box=box()

    def handleCollision(self,rect):
        if self.box.rect.colliderect(rect):
            self.box.colorChange()
