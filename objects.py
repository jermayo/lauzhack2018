import pygame
import math
import utilitary

from physics import element
from utilitary import coord

class rect():
    def __init__(self, x1, y1, x2, y2, GV):
        self.draw_info=[x1,y1, x2-x1, y2-y1]
        self.elem=element(GV, [coord(x1,y1), coord(x2,y1), coord(x1,y2), coord(x2,y2)], coord(x1,y1))
        GV.obj_list.append(self)

    def image(self, surface, color=(0,0,0)):
        pygame.draw.rect(surface, color, self.draw_info, 0)


class bullet():

    def __init__(self, x, y, angle, GV):
        self.elem = element(GV, [coord(x,y)], coord(x,y), speed = coord(utilitary.cart_coord(10, angle)))

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
        self.fire = 20


    def image(self, main, playerX, playerY, timeSpeed, GV):

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
            endX = baseX + int(math.cos(self.angle_cannon) * self.size /2)
            endY = baseY - int(math.sin(self.angle_cannon) * self.size / 2)
            pygame.draw.line(main, (0,0,0), [baseX, baseY], [endX, endY], 5)
        else:
            if(playerX < self.x):
                endX = self.x - self.size
                endY = self.y - self.size
                pygame.draw.line(main, (0,0,0), [self.x - int(self.size / 2), self.y - self.size], [endX, endY], 5)
            else:
                endX =self.x + self.size
                endY = self.y - self.size
                pygame.draw.line(main, (0,0,0), [self.x + int(self.size / 2), self.y - self.size], [endX, endY], 5)

        self.fire -= timeSpeed / 4
        if(self.fire > 20):
            self.fire = 20
        elif(self.fire < 0):
            bullet(endX, endY, self.angle_cannon, GV)
            self.fire = 20



    def getCoord(self):
        angle1 = utilitary.coord(self.x + self.size, self.y)
        angle2 = utilitary.coord(self.x - self.size, self.y)
        sommet = utilitary.coord(self.x, int(self.y - 3 / 2 * self.size))

        return [angle1, angle2, sommet]


class flag():
    def __init__(self, x, y, size, GV):
        h=size/15
        self.point_list=[[x+size-h, y], [x+size-h, y-size*3/2], [x, y-size*7/4+h/2], [x+size-h, y-size*2+h], [x+size-h, y-size*2], [x+size, y-size*2], [x+size, y]]
        self.elem=element(GV, [coord(x,y), coord(x+size, y), coord(x+size, y+2*size)], coord(x, y+2*size), coord(x,y))
        GV.obj_list.append(self)

    def image(self, main, color=(0,200,0)):
        pygame.draw.polygon(main, color, self.point_list)
