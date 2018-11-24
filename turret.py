import pygame
import math

class turret():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle_cannon = 0
        self.size = 40
        self.dead = False


    def image(self, main, playerX, playerY):

        pygame.draw.polygon(main, (0,0,0), [[self.x + self.size, self.y], [self.x - self.size, self.y], [self.x - int(self.size / 1.8), self.y - self.size], [self.x + int(self.size / 1.8), self.y - self.size]], 1)
        pygame.draw.arc(main, (0,0,0), [self.x - int(self.size / 2), self.y - self.size*3/2, self.size, self.size], 0, math.pi)
        if(playerY < self.y + self.size):
            angle = math.atan((self.y-playerY) / (playerX - self.x))
            baseX = self.x + int(math.cos(angle) * self.size)
            baseY = self.y - self.size + int(math.sin(angle) * self.size)
            pygame.draw.line(main, (0,0,0), [baseX, baseY], [baseX + int(math.cos(angle) * self.size), baseY - int(math.sin(angle) * self.size)], 5)
        #else if(playerX > self.x):
        #    pygame.draw.line(main, (0,0,0), )
        else:
            pygame.draw.line(main, (0,0,0), [self.x - int(self.size / 2), self.y - self.size], [self.x - self.size, self.y - self.size], 5)
