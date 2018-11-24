import pygame
import utilitary
import objects as obj
from physics import element
from utilitary import coord

def setmap1(GV,main,s,b):  
    obj.rect(0, b, 6*s, b-1*s, GV).draw(main)
    obj.rect(6*s, b, 7*s, b-2*s, GV).draw(main)
    obj.rect(7*s, b, 9*s, b-3*s, GV).draw(main)
    obj.rect(11*s, b, 14*s, b-3*s, GV).draw(main)
    obj.rect(15*s, b-5*s, 16*s, b-6*s, GV).draw(main)
    obj.rect(17*s, b-5*s, 18*s, b-6*s, GV).draw(main)
    obj.rect(20*s, b, 25*s, b-6*s, GV).draw(main)
