import pygame
import math

class player():

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.angle_body=math.pi/2
        self.angle_l_arm=-2 * math.pi / 3
        self.angle_r_arm=-math.pi / 3
        self.angle_l_leg=-2 * math.pi / 3
        self.angle_r_leg=-math.pi / 3
        self.angle_l_knee=-math.pi / 16 * 9
        self.angle_r_knee=-math.pi / 16 * 7
        self.size=40


    def image(self, main):
        #Body
        neckX = int(self.x + math.cos(self.angle_body) * 1.8 * self.size)
        neckY = int(self.y - math.sin(self.angle_body) * 1.8 * self.size)
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [neckX,neckY])
        #Head
        pygame.draw.circle(main, (0,0,0), [neckX, int(neckY - self.size / 2)], int(self.size / 2), 1)
        #arms
        shouldersX = int(self.x + 3 / 2 *  math.cos(self.angle_body) * self.size)
        shouldersY = int(self.y - 3 / 2 *  math.sin(self.angle_body) * self.size)
        pygame.draw.line(main, (0,0,0), [shouldersX, shouldersY], [int(shouldersX + math.cos(self.angle_l_arm) * self.size * 1.3), int(shouldersY -  math.sin(self.angle_l_arm) * self.size * 1.3)])
        pygame.draw.line(main, (0,0,0), [shouldersX, shouldersY], [int(shouldersX + math.cos(self.angle_r_arm) * self.size * 1.3), int(shouldersY -  math.sin(self.angle_r_arm) * self.size * 1.3)])
        #legs
        legLX = int(self.x + math.cos(self.angle_l_leg) * self.size)
        legLY = int(self.y - math.sin(self.angle_l_leg) * self.size)
        legRX = int(self.x + math.cos(self.angle_r_leg) * self.size)
        legRY = int(self.y - math.sin(self.angle_r_leg) * self.size)
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [legLX, legLY])
        pygame.draw.line(main, (0,0,0), [self.x, self.y], [legRX, legRY])
        pygame.draw.line(main, (0,0,0), [legLX, legLY], [int(legLX + math.cos(self.angle_l_knee) * self.size * 0.8), int(legLY - math.sin(self.angle_l_knee) * self.size * 0.8)])
        pygame.draw.line(main, (0,0,0), [legRX, legRY], [int(legRX + math.cos(self.angle_r_knee) * self.size * 0.8), int(legRY - math.sin(self.angle_r_knee) * self.size * 0.8)])
