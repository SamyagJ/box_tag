#Samyag Jhaveri

import pygame

class box:
    def __init__(self):
        self.rect=pygame.Rect(8,8,8,100)
        self.color=pygame.Color(0,0,0,100)

    def colorChange(self):
        self.color=pygame.Color(225,0,0,100)

class player:
    def __init__(self):
        self.box=box()

    def move(self,dir):
        if dir is True:
            self.box.rect.move.ip(2,0)
        else:
            self.box.rect.move.ip(-2,0)
class objective:
    def __init__(self):
        self.box=box()

    def handleColision(self,rect):
        if self.box.rect.colliderect(rect):
            self.box.colorChange
