import time
import pygame



pygame.init()

larg=800
haut=500
main=pygame.display.set_mode([larg,haut])

horloge=pygame.time.Clock()

run=True
while run:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.flip()


pygame.quit()
