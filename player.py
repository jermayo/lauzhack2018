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


    def image(self, main, coord):
        //Body
        neckX = self.x + math.sin(self.angle_body) * 2 * size
        neckY = self.y - math.cos(self.angle_body) * 2 * size
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [neckX,neckY])
        //Head
        pygame.draw.circle(main, (0,0,0), [neckX + size / 2, neckY], size / 2)
        //arms
        pygame.draw.line(main, (0,0,0), [3 / 4 * neckX, 3 / 4 * neckY], [3 / 4 * neckX + math.sin(angle_l_arm) * size, 3 / 4 * neckY -  math.cos(angle_l_arm) * size])
        pygame.draw.line(main, (0,0,0), [3 / 4 * neckX, 3 / 4 * neckY], [3 / 4 * neckX + math.sin(angle_r_arm) * size, 3 / 4 * neckY -  math.cos(angle_r_arm) * size])
        //legs
        legLX = self.x + math.sin(angle_l_leg) * size
        legLY = self.y - math.cos(angle_l_leg) * size
        legRX
        legRY
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [legLX, legLY])
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [legRX, legRY])
        pygame.draw.line(main, (0,0,0), [legLX, legLY], [legLX + math.sin(angle_l_knee) * size, legLY - math.cos(angle_l_knee) * size])
        pygame.draw.line(main, (0,0,0), [legRX, legRY], [legRX + math.sin(angle_r_knee) * size, legRY - math.cos(angle_r_knee) * size])
