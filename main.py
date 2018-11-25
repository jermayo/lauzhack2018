import time
import pygame
import objects as obj
import player
import utilitary
import maps
import physics

def key_action(keys, fullscreen, player1, time):

    if keys[pygame.K_F11]:
        if not fullscreen:
            pygame.display.set_mode([larg,haut], pygame.FULLSCREEN)
            fullscreen=not fullscreen
    if keys[pygame.K_ESCAPE]:
        if fullscreen:
            pygame.display.set_mode([larg,haut])
            fullscreen=not fullscreen

    if keys[pygame.K_d]:
        player1.running=True
        player1.state(time, side="LEFT")
    if keys[pygame.K_a]:
        player1.running=True
        player1.state(time, side="RIGHT")
    if not player1.running:
        player1.state(time)
        player1.running=False


    jump=False
    if keys[pygame.K_w]:
        jump=True


    return fullscreen

GV=utilitary.GlobalVariable()
pygame.init()


infoObject = pygame.display.Info()
larg, haut=infoObject.current_w, infoObject.current_h-120

infoObject.current_w, infoObject.current_h
main=pygame.display.set_mode([larg,haut],0,0)
fullscreen=False


horloge=pygame.time.Clock()

main.fill((255,255,255))
player1=player.mister(larg/2, haut/2, GV)
player1.elem.points_list=player1.getCoord()

turret1 = obj.turret(larg / 4 * 3, haut / 2, GV)
t = 0
obj_list=[]

maxMapSize=25
size=larg/maxMapSize


run=True
while run:

    main.fill((255,255,255))
    fullscreen=key_action(pygame.key.get_pressed(), fullscreen, player1, t)
    maps.setmap1(GV, main, size, haut)

    obj.flag(400, 400, 100, GV).image(main)

    for objet in GV.obj_list:
        objet.image(main, player=player1, GV=GV)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    pygame.display.flip()
    horloge.tick(60)
    t += 0.2

pygame.quit()
