#7/23/2019

from classes import *

import pygame

pygame.init()

player=player()
objectives=[]
objectives.append(objective())
objectives.append(objective())
objectives.append(objective())
screen=pygame.display.set_mode((1024,720))
x=5
y=5
player.box.rect.center = ((x,y))

objectives[0].box.rect.center

def update():
    keys=pygame.key.get_pressed()
    #if keys[k_a]:
    #    player.move(False)
    #if keys [h_d]:
    #    player.move(True)

    for i in objectives:
        i.handleCollision(player.box.rect)


def render():
    screen.fill(pygame.Color("blue"))
    screen.fill(player.box.color, player.box.rect)
    for i in objectives:
        screen.fill(i.box.color, i.box.rect)

def main():
    while True:
        update()
        render()
        pygame.display.flip()

if __name__ == "__main__":
    main()


