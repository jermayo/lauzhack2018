import time
import pygame

import player

pygame.init()

larg=800
haut=500
main=pygame.display.set_mode([larg,haut])

horloge=pygame.time.Clock()

main.fill((255,255,255))
player1=player.player(larg / 2, haut / 2)

run=True
while run:
    main.fill((255,255,255))
    player1.image(main)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.flip()


pygame.quit()
