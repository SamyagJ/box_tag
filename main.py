#7/23/2019
import sys,pygame
from pygame.locals import *
from classes import box,objective,player
from pygame import Color

import pygame

import random

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((640,480))
player=player()
player.box.rect.center=(20,240)
objectives=[]
objectives.append(objective())
objectives.append(objective())
objectives.append(objective())


count=0
for i in objectives:
    i.box.rect.center=(count +100,240)
    count += 100\




def update():
    pygame.event.pump()
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(2)
    if key[pygame.K_RIGHT]:
        player.move(1)
    if key[pygame.K_UP]:
        player.move(3)
    if key[pygame.K_DOWN]:
        player.move(4)
    for i in objectives:
        i.handleCollision(player.box.rect)


def render():
    screen.fill(pygame.Color("blue"))
    screen.fill(player.box.color, player.box.rect)
    for i in objectives:
        screen.fill(i.box.color, i.box.rect)

def main():
    while True:
        clock.tick(60)
        update()
        render()
        pygame.display.flip()

if __name__ == "__main__":
    main()


