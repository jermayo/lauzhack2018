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

    player1.running=False
    if keys[pygame.K_d] and not player1.on_wall:
        player1.running=True
        player1.state(time, side="RIGHT")
        player1.elem.center.speed["x"]=6
    elif keys[pygame.K_a] and not player1.on_wall:
        player1.running=True
        player1.state(time, side="LEFT")
        player1.elem.center.speed["x"]=-6
    else:
        player1.running=False
        player1.state(time)
        player1.elem.center.speed["x"]=0
    if keys[pygame.K_w] and player1.is_grounded and not player1.on_wall:
        player1.elem.center.speed["y"]=-17

    if keys[pygame.K_RCTRL]:
        GV.timeSpeed=1

    if keys[pygame.K_UP]:
        if GV.timeSpeed<=1:
            GV.timeSpeed+=0.1

    if keys[pygame.K_DOWN]:
        if GV.timeSpeed>=-1:
            GV.timeSpeed-=0.1



    return fullscreen

GV=utilitary.GlobalVariable()
pygame.init()


infoObject = pygame.display.Info()
larg, haut=int(infoObject.current_w), int(infoObject.current_h)-120

infoObject.current_w, infoObject.current_h
main=pygame.display.set_mode([larg,haut],0,0)
fullscreen=False

maxMapSize=25
GV.size = larg/maxMapSize


horloge=pygame.time.Clock()

main.fill((255,255,255))


t = 0

player1=player.mister(larg/8, haut/2, GV)
player1.elem.points_list=player1.getCoord()
level_pass=False
maps.setmap1(GV, main, GV.size, haut, player1)
mainrun=True
next_level=0

while mainrun and GV.level_pass<2:

    if GV.level_pass==1 and next_level==0:
        main.fill((255,255,255))
        
    
        next_level=1
    if next_level:
        l=level_pass
        GV=utilitary.GlobalVariable()
        GV.level_pass=1
        GV.size=larg/maxMapSize

        player1=player.mister(larg/8, haut/2, GV)
        player1.elem.points_list=player1.getCoord()

        maps.setmap2(GV, main, GV.size, haut, player1)
    main.fill((255,255,255))
    #GV.obj_list=[]
    fullscreen=key_action(pygame.key.get_pressed(), fullscreen, player1, t)

    for objet in GV.obj_list:
        if objet.image(main, player=player1, GV=GV):
            GV.obj_list.remove(objet)



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            mainrun=False


    pygame.display.flip()
    horloge.tick(60)
    t += 0.2
pygame.quit()
