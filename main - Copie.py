import time
import pygame
import objects as obj
import player
import utilitary
import maps

GV=utilitary.GlobalVariable()
pygame.init()

def setSize():

    print("hellooooo")
    width=pygame.display.get_surface().get_width()
    height=pygame.display.get_surface().get_height()
    print(width)
    print(height)
    size=width/maxMapSize
    bottom=height
    return(size,bottom)

larg=1600
haut=1000

maxMapSize = 20
size=50
bottom=1000

main=pygame.display.set_mode([larg,haut])
pygame.display.toggle_fullscreen()

horloge=pygame.time.Clock()

main.fill((255,255,255))
player1=player.player(larg / 2, haut / 2)
t = 0
obj_list=[]
run=True

(size,bottom)=setSize()


while run:
    main.fill((255,255,255))
    maps.setmap1(GV,main,size,bottom)
    #player1.image(main)
    #[head1, head2, head3, arm1, arm2, foot1, foot2] = player1.getCoord()
    #pygame.draw.polygon(main, (0,0,0), [[head1["x"], head1["y"]], [head2["x"], head2["y"]], [arm1["x"], arm1["y"]], [foot1["x"], foot1["y"]], [foot2["x"], foot2["y"]], [arm2["x"], arm2["y"]], [head3["x"], head3["y"]]], 1)
    #player1.run(t)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    touche=pygame.key.get_pressed()
    if touche[pygame.K_ESCAPE]:
        pygame.display.toggle_fullscreen()

    pygame.display.flip()
    horloge.tick(60)
    t += 0.2

pygame.quit()
