import time
import pygame
import objects as obj
import player
import utilitary

GV=utilitary.GlobalVariable()
pygame.init()

larg=800
haut=500

main=pygame.display.set_mode([larg,haut])
pygame.display.toggle_fullscreen()

horloge=pygame.time.Clock()

main.fill((255,255,255))
player1=player.player(larg / 2, haut / 2)
t = 0
obj_list=[]
run=True
while run:
    main.fill((255,255,255))
    obj.rect(0, 0, 200, 200, GV).draw(main)


    #player1.image(main)
    #[head1, head2, head3, arm1, arm2, foot1, foot2] = player1.getCoord()
    #pygame.draw.polygon(main, (0,0,0), [[head1["x"], head1["y"]], [head2["x"], head2["y"]], [arm1["x"], arm1["y"]], [foot1["x"], foot1["y"]], [foot2["x"], foot2["y"]], [arm2["x"], arm2["y"]], [head3["x"], head3["y"]]], 1)
    #player1.run(t)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.flip()
    horloge.tick(60)
    t += 0.2

pygame.quit()
