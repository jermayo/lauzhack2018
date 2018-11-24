import pygame
import math

class player():
    def __init__(self, coord):
        self.coord=coord
        self.angle_l_arm=-60
        self.angle_r_arm=-120
        self.angle_l_leg=-60
        self.angle_r_leg=-120
        size=10


    def image(self):
        r_arm=math.cos(self.angel_r_arm)*self.size
        pygame.draw.polygon(main, [self.coord, [self.coord["x"]+self.size, self.cord+self.size, ])
