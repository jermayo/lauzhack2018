import pygame

def bougeBalle(x,y):
    global vx,vy,cote,rayon
    n=20
    
    if y<7:            #bord d'en huat
        vy=-vy
    elif y>haut-7:  #bord d'en bas 
        vy=-vy
    if x<7:    #gauche
        return "2",None
    elif x>larg-7:   #droite
        return "1",None
    elif x>=20-abs(vx) and x<=27 and y>=flipd-7 and y<=flipd+tflip+7 and cote==-1:
        vx=-vx
        acc=0.1
        vx=abs(vx)/vx*(abs(vx)+acc)
        #vy=abs(vy)/vy*(abs(vy)+acc)
        vy=-(((flipd+tflip/2-by)*vx)/n+acc)
        cote=-cote
        rayon=50

    elif x>=larg-27 and x<=larg-20+abs(vx) and y>=flipg-7and y<=flipg+tflip+7 and cote==1:
        vx=-vx
        acc=0.1
        vx=abs(vx)/vx*(abs(vx)+acc)
        vy=((flipd+tflip/2-by)*vx)/n+acc
        cote=-cote
        rayon=50
    x+=vx
    y+=vy
    return x,y


def flipPlayer(touche):
    global flipd,flipg
    vitesse=3
    if touche[pygame.K_q] and flipd>0 and playerD==1:
        flipd-=vitesse
    if touche[pygame.K_a] and flipd<haut-tflip and playerD==1:
        flipd+=vitesse
    if touche[pygame.K_o] and flipg>0 and playerG==1 :
        flipg-=vitesse
    if touche[pygame.K_l] and flipg<haut-tflip and playerG==1:
        flipg+=vitesse


def bot():
    global flipd,flipg
    if botD==1:
        flipd=by-tflip/2
    if botG==1:
        flipg=by-tflip/2
    return

def menu():
    label1=myfont3.render("PONG",1,(255,255,255))
    label2=myfont2.render("Joueur 1 (w et s) contre Joueur 2 (o et l) : 1",1,(255,255,255))
    label3=myfont2.render("Joueur 1 (w et s) contre Ordinateur : 2",1,(255,255,255))
    label4=myfont2.render("Ordinateur 1 ontre Ordinateur 2 : 3",1,(255,255,255))
    main.blit(label1,(larg/2-100,haut/2-60))
    pygame.display.flip()
    main.blit(label2,(larg/2-200,haut/2))
    pygame.time.delay(500)
    pygame.display.flip()
    main.blit(label3,(larg/2-200,haut/2+40))
    pygame.time.delay(500)
    pygame.display.flip()
    main.blit(label4,(larg/2-200,haut/2+80))
    pygame.time.delay(500)
    pygame.display.flip()
    return

def end(win):
    if win==1:
        text="Player 1 win"
    elif win==2:
        text="Player 2 win"
    else:
        text=None
    label=myfont1.render(text,1,(255,255,255))
    main.blit(label,(larg/2-100,haut/2-50))
    pygame.display.flip()
    pygame.time.delay(500)
    label2=myfont2.render("Rejouer ? (Oui=0,Non=1)",1,(255,255,255))
    main.blit(label2,(larg/2-130,haut/2+30))
    pygame.display.flip()


pygame.init()

myfont1=pygame.font.SysFont("monospace",30,bold=True)
myfont2=pygame.font.SysFont("monospace",20)
myfont3=pygame.font.SysFont("monospace",50,bold=True)

horloge=pygame.time.Clock()
larg=800
haut=500
main=pygame.display.set_mode([larg,haut])





run1=True
while run1:
    main.fill((0,0,0))
    pygame.time.delay(1000)
    run2=True
    playerD=0
    playerG=0
    botD=0
    botG=0
    menu()
    while 1:
        touche=pygame.key.get_pressed()
        if touche[pygame.K_1]:
            playerD=1
            playerG=1
            run2=False
            break
        if touche[pygame.K_2]:
            playerD=1
            botG=1
            run2=False
            break
        if touche[pygame.K_3]:
            botD=1
            botG=1
            run2=False
            break
        for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    run1=False
                    run2=False
                    break
                
    tflip=100
    vitesse=0.5
    vx=vitesse
    vy=vitesse
    flipd=haut/2-tflip/2
    flipg=haut/2-tflip/2
    bx=int(larg/2)
    by=int(haut/2)
    win=0
    run2=True
    cote=1
    rayon=7

    for i in range(5,0,-1):
        main.fill((0,0,0))
        pygame.draw.rect(main,(255,255,255),[10,flipd,10,tflip])
        pygame.draw.rect(main,(255,255,255),[larg-10,flipg,-10,tflip])
        pygame.draw.circle(main,(255,255,255),[int(bx),int(by)],7)

        text=str(i)
        label=myfont3.render(text,1,(255,255,255))
        main.blit(label,(larg/2-15,haut/2-60))
        pygame.display.flip()
        horloge.tick(1)

    while run2:
        main.fill((0,0,0))
        
        bx,by=bougeBalle(bx,by)
        if bx=="1":
            win=1
            break
        elif bx=="2":
            win=2
            break
        if rayon>7:
            pygame.draw.circle(main,(255,255,255),[int(bx),int(by)],int(rayon))
            rayon-=0.5
        pygame.draw.circle(main,(255,255,255),[int(bx),int(by)],int(rayon))

        flipPlayer(pygame.key.get_pressed())
        bot()
        pygame.draw.rect(main,(255,255,255),[10,flipd,10,tflip])
        pygame.draw.rect(main,(255,255,255),[larg-20,flipg,10,tflip])
        
        pygame.display.flip()

        horloge.tick(1000)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run1=False
                run2=False
                break
    end(win)
    
    while 1:
        touche=pygame.key.get_pressed()
        if touche[pygame.K_0]:
            break
        if touche[pygame.K_1]:
            run1=False
            break
        for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    run1=False
pygame.quit()
