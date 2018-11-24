import pygame

from physics import element
from utilitary import coord

class rect():
    def __init__(self, x1, y1, x2, y2, left,  up, right, down, obj_list):
        self.width=x2-x1
        self.heigth=y2-y1
        self.elem, obj_list=element(obj_list, [coord(x1,y1), coord(x2,y1), coord(x1,y2), coord(x2,y2)], coord(x1,y1))
        self.drawn_sides=[left,up,right,down]
        return obj_list

    def draw(self, surface, color=(0,0,0)):
        pygame.draw.rect(surface, color, [self.elem.coord["x"], self.elem.coord["y"], self.width, self.heigth], 0)
