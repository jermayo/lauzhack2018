import pygame
import utilitary
import objects as obj
from physics import element
from utilitary import coord

def setmap1(GV,main,s,b, player):
    obj.rect(0, b, 25*s, b-1*s, GV).image(main)
    obj.rect(5*s, b, 7*s, b-2*s, GV).image(main)
    obj.rect(6*s, b, 9*s, b-3*s, GV).image(main)
    obj.rect(11*s, b, 14*s, b-3*s, GV).image(main)
    obj.rect(15*s, b-4*s, 16*s, b-5*s, GV).image(main)
    obj.rect(17*s, b-5*s, 19*s, b-6*s, GV).image(main)
    obj.rect(21*s, b, 25*s, b-6*s, GV).image(main)
    obj.rect(0, b-11*s, 25*s, 0, GV).image(main)
    obj.rect(0, 0, 1*s, b, GV).image(main)

    obj.flag(23*s,b-6*s,s,GV).image(main, player=player, GV=GV)

    obj.spikes(9*s,b-1*s,2,s,GV).image(main, player=player, GV=GV)
    obj.spikes(14*s,b-1*s,7,s,GV).image(main,player=player, GV=GV)

    obj.excla(4*s,b-1*s,GV, text="Use WAD to move around", text_coord=(4*s, b/2)).image(main, GV=GV, player=player)


def setmap2(GV,main,s,b, player):
    obj.rect(0, 0, 25*s, b-11*s, GV).image(main)
    obj.rect(0, b, 25*s, b-1*s-1, GV).image(main)

    obj.rect(0, b-6*s, 2*s, b-1*s, GV).image(main)
    obj.rect(2*s, b-5*s, 3*s+1, b-1*s, GV).image(main)
    obj.rect(3*s, b-1*s, 4*s+1, b-4*s, GV).image(main)
    obj.rect(4*s, b-1*s, 5*s+1, b-3*s, GV).image(main)
    obj.rect(5*s, b-1*s, 6*s+1, b-2*s, GV).image(main)
    obj.rect(14*s, b-2*s-1, 25*s+1, b-1*s, GV).image(main)
    obj.rect(15*s, b-3*s-1, 25*s+1, b-2*s, GV).image(main)
    obj.rect(16*s, b-4*s-1, 25*s+1, b-3*s, GV).image(main)
    obj.rect(22*s, b-5*s-1, 25*s+1, b-4*s, GV).image(main)

    obj.rect(8*s, b-5*s, 12*s, b-4*s, GV).image(main)
    obj.rect(10*s, b-5*s, 12*s, b-11*s, GV).image(main)
    obj.rect(12*s, b-6*s, 19*s, b-11*s, GV).image(main)

    obj.excla(11*s,b-1*s,GV, text="Use up and down to change time", text_coord=(0.1*s, b/4)).image(main, GV=GV, player=player)
    obj.clock(9*s,b-1*s,s,GV).image(main, player=player)
    obj.turret(9*s,b-5*s,GV).image(main, player=player, GV=GV)
    obj.turret(21*s,b-4*s,GV).image(main, player=player, GV=GV)

    obj.flag(23*s,b-5*s,s,GV).image(main, player=player, GV=GV)

def setmaptr(GV,main,s,b, player,t):


    obj.rect(0-t*25*s/500, b, 25*s-t*25*s/500, b-1*s, GV).image(main)
    obj.rect(5*s-t*25*s/500, b, 7*s-t*25*s/500, b-2*s, GV).image(main)
    obj.rect(6*s-t*25*s/500, b, 9*s-t*25*s/500, b-3*s, GV).image(main)
    obj.rect(11*s-t*25*s/500, b, 14*s-t*25*s/500, b-3*s, GV).image(main)
    obj.rect(15*s-t*25*s/500, b-4*s, 16*s-t*25*s/500, b-5*s, GV).image(main)
    obj.rect(17*s-t*25*s/500, b-5*s, 19*s-t*25*s/500, b-6*s, GV).image(main)
    obj.rect(21*s-t*25*s/500, b, 25*s-t*25*s/500, b-6*s, GV).image(main)
    obj.rect(0-t*25*s/500, b-11*s, 25*s-t*25*s/500, 0, GV).image(main)
    obj.rect(0-t*25*s/500, 0, 1*s-t*25*s/500, b, GV).image(main)

    obj.flag(23*s-t*25*s/500,b-6*s,s,GV).image(main, player=player, GV=GV)

    obj.spikes(9*s-t*25*s/500,b-1*s,2,s,GV).image(main, player=player, GV=GV)
    obj.spikes(14*s-t*25*s/500,b-1*s,7,s,GV).image(main,player=player, GV=GV)

    obj.excla(4*s-t*25*s/500,b-1*s,GV).image(main, GV=GV, player=player)




    obj.rect(0+(500-t)*25*s/500, 0, 25*s+(500-t)*25*s/500, b-11*s, GV).image(main)
    obj.rect(0+(500-t)*25*s/500, b, 25*s+(500-t)*25*s/500, b-1*s-1, GV).image(main)

    obj.rect(0+(500-t)*25*s/500, b-6*s, 2*s+(500-t)*25*s/500, b-1*s, GV).image(main)
    obj.rect(2*s+(500-t)*25*s/500, b-5*s, 3*s+1+(500-t)*25*s/500, b-1*s, GV).image(main)
    obj.rect(3*s+(500-t)*25*s/500, b-1*s, 4*s+1+(500-t)*25*s/500, b-4*s, GV).image(main)
    obj.rect(4*s+(500-t)*25*s/500, b-1*s, 5*s+1+(500-t)*25*s/500, b-3*s, GV).image(main)
    obj.rect(5*s+(500-t)*25*s/500, b-1*s, 6*s+1+(500-t)*25*s/500, b-2*s, GV).image(main)
    obj.rect(14*s+(500-t)*25*s/500, b-2*s-1, 25*s+1+(500-t)*25*s/500, b-1*s, GV).image(main)
    obj.rect(15*s+(500-t)*25*s/500, b-3*s-1, 25*s+1+(500-t)*25*s/500, b-2*s, GV).image(main)
    obj.rect(16*s+(500-t)*25*s/500, b-4*s-1, 25*s+1+(500-t)*25*s/500, b-3*s, GV).image(main)
    obj.rect(22*s+(500-t)*25*s/500, b-5*s-1, 25*s+1+(500-t)*25*s/500, b-4*s, GV).image(main)

    obj.rect(8*s+(500-t)*25*s/500, b-5*s, 12*s+(500-t)*25*s/500, b-4*s, GV).image(main)
    obj.rect(10*s+(500-t)*25*s/500, b-5*s, 12*s+(500-t)*25*s/500, b-11*s, GV).image(main)
    obj.rect(12*s+(500-t)*25*s/500, b-6*s, 19*s+(500-t)*25*s/500, b-11*s, GV).image(main)

    obj.excla(11*s+(500-t)*25*s/500,b-1*s,GV, "").image(main, GV=GV, player=player)
    obj.clock(9*s+(500-t)*25*s/500,b-1*s,s,GV).image(main, player=player)
    obj.turret(9*s+(500-t)*25*s/500,b-5*s,GV).image(main, player=player, GV=GV)
    obj.turret(21*s+(500-t)*25*s/500,b-4*s,GV).image(main, player=player, GV=GV)

    obj.flag(23*s+(500-t)*25*s/500,b-5*s,s,GV).image(main, player=player, GV=GV)
