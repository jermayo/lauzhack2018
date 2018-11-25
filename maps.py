import pygame
import utilitary
import objects as obj
from physics import element
from utilitary import coord

def setmap1(GV,main,s,b):
    obj.rect(0, b, 25*s, b-1*s, GV).image(main)
    obj.rect(5*s, b, 7*s, b-2*s, GV).image(main)
    obj.rect(6*s, b, 8*s, b-3*s, GV).image(main)
    obj.rect(11*s, b, 14*s, b-3*s, GV).image(main)
    obj.rect(15*s, b-4*s, 16*s, b-5*s, GV).image(main)
    obj.rect(17*s, b-5*s, 19*s, b-6*s, GV).image(main)
    obj.rect(21*s, b, 25*s, b-6*s, GV).image(main)
    obj.rect(0, b-11*s, 25*s, 0, GV).image(main)
    obj.rect(0, 0, 1*s, b, GV).image(main)
    
    obj.flag(23*s,b-6*s,s,GV).image(main)

    obj.spikes(8*s,b-1*s,3,s,GV).image(main)
    obj.spikes(14*s,b-1*s,7,s,GV).image(main)

    obj.clock(12*s,b-3*s,s,GV).image(main)


def setmap2(GV,main,s,b):
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

    obj.flag(23*s,b-5*s,s,GV).image(main)
