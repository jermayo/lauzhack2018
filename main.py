import time
import pygame
import objects as obj
import player
import utilitary
import maps

GV=utilitary.GlobalVariable()
pygame.init()


infoObject = pygame.display.Info()
larg, haut=infoObject.current_w, infoObject.current_h-120

infoObject.current_w, infoObject.current_h
main=pygame.display.set_mode([larg,haut],0,0)
fullscreen=False


horloge=pygame.time.Clock()

main.fill((255,255,255))
player1=player.player(larg / 2, haut / 2)
turret1 = obj.turret(larg / 4 * 3, haut / 2)
t = 0
obj_list=[]

maxMapSize=20
size=larg/maxMapSize


run=True
while run:
    main.fill((255,255,255))
    maps.setmap1(GV, main, size, haut)


    #turret1.image(main, player1.x, player1.y, GV)
    player1.image(main, GV.timeSpeed)
    [head1, head2, head3, arm1, arm2, foot1, foot2] = player1.getCoord()
    pygame.draw.polygon(main, (0,0,0), [[head1["x"], head1["y"]], [head2["x"], head2["y"]], [arm1["x"], arm1["y"]], [foot1["x"], foot1["y"]], [foot2["x"], foot2["y"]], [arm2["x"], arm2["y"]], [head3["x"], head3["y"]]], 1)
    player1.run(t)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    touche=pygame.key.get_pressed()
    if touche[pygame.K_F11]:
        if not fullscreen:
            pygame.display.set_mode([larg,haut], pygame.FULLSCREEN)
            fullscreen=not fullscreen
    if touche[pygame.K_ESCAPE]:
        if fullscreen:
            pygame.display.set_mode([larg,haut])
            fullscreen=not fullscreen
    pygame.display.flip()
    horloge.tick(60)
    t += 0.2

pygame.quit()
