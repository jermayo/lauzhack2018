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
    if keys[pygame.K_d]:
        player1.running=True
        player1.state(time, side="RIGHT")
        player1.elem.center.speed["x"]=5
    elif keys[pygame.K_a]:
        player1.running=True
        player1.state(time, side="LEFT")
        player1.elem.center.speed["x"]=-5
    else:
        player1.running=False
        player1.state(time)
        player1.elem.center.speed["x"]=0
    if keys[pygame.K_w]:
        player1.elem.center.speed["y"]=-10


    return fullscreen

GV=utilitary.GlobalVariable()
pygame.init()


infoObject = pygame.display.Info()
larg, haut=int(infoObject.current_w), int(infoObject.current_h)-120

infoObject.current_w, infoObject.current_h
main=pygame.display.set_mode([larg,haut],0,0)
fullscreen=False

maxMapSize=25
size=larg/maxMapSize
GV.size = size


horloge=pygame.time.Clock()

main.fill((255,255,255))
player1=player.mister(larg/2, haut/2, GV)
player1.elem.points_list=player1.getCoord()

turret1 = obj.turret(larg / 4 * 3, haut / 2, GV)
t = 0
obj_list=[]




run=True
maps.setmap1(GV, main, size, haut)
while run:

    main.fill((255,255,255))
    coord=player1.getCoord()

    pygame.draw.polygon(main, (0,0,0), [[coord[0]["x"],coord[0]["y"]],[coord[1]["x"],coord[1]["y"]],[coord[3]["x"],coord[3]["y"]],[coord[2]["x"],coord[2]["y"]]], 1)
    #GV.obj_list=[]
    fullscreen=key_action(pygame.key.get_pressed(), fullscreen, player1, t)

    for objet in GV.obj_list:
        if objet.image(main, player=player1, GV=GV):
            GV.obj_list.remove(objet)



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    pygame.display.flip()
    horloge.tick(60)
    t += 0.2
pygame.quit()
