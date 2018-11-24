import pygame
import math
import utilitary

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


class bullet():

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 5

    def image(self, main):
        pygame.draw.circle(main, (0,0,0), [self.x, self.y], 1)
        self.x += int(math.cos(angle) * speed)
        self.y += int(math.sin(angle) * speed)




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
