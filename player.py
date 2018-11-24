import pygame
import math

class player():

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.angle_body=90
        self.angle_l_arm=-120
        self.angle_r_arm=-60
        self.angle_l_leg=-60
        self.angle_r_leg=-120
        self.angle_l_knee=270
        self.angle_r_knee=270
        self.size=10


    def image(self, main):
        #Body
        neckX = self.x + math.sin(self.angle_body) * 2 * self.size
        neckY = self.y - math.cos(self.angle_body) * 2 * self.size
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [neckX,neckY])
        #Head
        pygame.draw.circle(main, (0,0,0), [neckX + size / 2, neckY], self.size / 2)
        #arms
        pygame.draw.line(main, (0,0,0), [3 / 4 * neckX, 3 / 4 * neckY], [3 / 4 * neckX + math.sin(angle_l_arm) * self.size, 3 / 4 * neckY -  math.cos(angle_l_arm) * self.size])
        pygame.draw.line(main, (0,0,0), [3 / 4 * neckX, 3 / 4 * neckY], [3 / 4 * neckX + math.sin(angle_r_arm) * self.size, 3 / 4 * neckY -  math.cos(angle_r_arm) * self.size])
        #legs
        legLX = self.x + math.sin(angle_l_leg) * self.size
        legLY = self.y - math.cos(angle_l_leg) * self.size
        legRX
        legRY
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [legLX, legLY])
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [legRX, legRY])
        pygame.draw.line(main, (0,0,0), [legLX, legLY], [legLX + math.sin(angle_l_knee) * self.size, legLY - math.cos(angle_l_knee) * size])
        pygame.draw.line(main, (0,0,0), [legRX, legRY], [legRX + math.sin(angle_r_knee) * self.size, legRY - math.cos(angle_r_knee) * size])
