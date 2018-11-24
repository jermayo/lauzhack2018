import time
import pygame



pygame.init()

larg=800
haut=500
main=pygame.display.set_mode([larg,haut])

while True:
    time.sleep(0.5)
    main.fill((0,0,0))
    pygame.display.flip()
    time.sleep(0.5)
    main.fill((255,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            break
    pygame.display.flip()


pygame.quit()
