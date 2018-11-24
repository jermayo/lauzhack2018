import pygame
import math
import utilitary

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
        if(playerX == self.x):
            self.angle_cannon = math.pi / 2
        elif(playerX < self.x):
            self.angle_cannon = math.pi - math.atan((self.y-playerY) / (self.x - playerX))
        else:
            self.angle_cannon = math.atan((self.y-playerY) / (playerX - self.x))

        if(playerY < self.y - self.size):
            baseX = int(self.x + math.cos(self.angle_cannon) * self.size / 2)
            baseY = int(self.y - self.size - math.sin(self.angle_cannon) * self.size / 2)
            pygame.draw.line(main, (0,0,0), [baseX, baseY], [baseX + int(math.cos(self.angle_cannon) * self.size /2), baseY - int(math.sin(self.angle_cannon) * self.size / 2)], 5)
        else:
            if(playerX < self.x):
                pygame.draw.line(main, (0,0,0), [self.x - int(self.size / 2), self.y - self.size], [self.x - self.size, self.y - self.size], 5)
            else:
                pygame.draw.line(main, (0,0,0), [self.x + int(self.size / 2), self.y - self.size], [self.x + self.size, self.y - self.size], 5)


    def getCoord(self):
        angle1 = utilitary.coord(self.x + self.size, self.y)
        angle2 = utilitary.coord(self.x - self.size, self.y)
        sommet = utilitary.coord(self.x, int(self.y - 3 / 2 * self.size))

        return [angle1, angle2, sommet]
