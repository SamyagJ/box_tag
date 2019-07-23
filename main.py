#7/23/2019

from classes import *

import pygame:
    pygame.init()

player=player()
objectives=[]
objectives.append(objective())
objectives.append(objective())
objectives.append(objective())
screen=pygame.display.set_mode(1024,720)

def update():
    for i in objectives:
        i.handleCollision(player.box.rect)

def render():
    screen.fill(color(255,255,255,100))
    screen.fill(player.color,player.box.rect)
    for i in objectives:
        screen.fill(i.box.color,i.box.rect)

def main():
    update()
    render()
    pygame.display.flip()

    if __name__=='__main__':
        main()
