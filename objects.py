import pygame

from physics import element
from utilitary import coord

class rect():
    def __init__(self, x1, y1, x2, y2, GV):
        self.draw_info=[x1, y1 ,x2-x1, y2-y1]
        self.elem=element(GV, [coord(x1,y1), coord(x2,y1), coord(x1,y2), coord(x2,y2)], coord(x1,y1))


    def draw(self, main, color=(0,0,0)):
        pygame.draw.rect(main, (0,0,0), self.draw_info, 0)
