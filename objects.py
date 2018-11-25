import pygame
import math
import utilitary

from physics import element
from physics import collision
from utilitary import coord

class rect():
    def __init__(self, x1, y1, x2, y2, GV, color=(0,0,0)):
        self.draw_info=[x1,y1, x2-x1, y2-y1]
        self.elem=element(GV, [coord(x1,y1), coord(x2,y1), coord(x1,y2), coord(x2,y2)], coord(x1,y1))
        GV.obj_list.append(self)
        self.color=color

    def image(self, main, player=None, GV=None):
        pygame.draw.rect(main, self.color, self.draw_info, 0)
        return False

class spikes():
    def __init__(self, x1, y, number, size, GV):
        self.point_list=[]
        for i in range (0,number,1):
            self.point_list.append([x1+i*size, y])
            self.point_list.append([x1+i*size+size/2, y-size])
            self.color=(200,0,0)

        self.elem=element(GV, [coord(x1, y), coord(x1+number*size, y), coord(x1+number*size, y-size), coord(x1, y-size)], coord(x1,y))

        self.point_list.append([x1+number*size, y])
        GV.obj_list.append(self)

    def image(self, main, player=None, GV=None):
        pygame.draw.polygon(main, self.color, self.point_list)

class clock():
    def __init__(self,x,y,size,GV):
        self.elem=element(GV, [coord(x+size/2,y-size)],coord(x+size/2,y-size))
        GV.obj_list.append(self)
        self.size = size

    def image(self,main, player=None, GV=None):
        pygame.draw.circle(main, (0,0,0), [int(self.elem.center.coord["x"]), int(self.elem.center.coord["y"])], int(self.size/2),5)
        pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"],self.elem.center.coord["y"]-self.size/2*4/5],[self.elem.center.coord["x"],self.elem.center.coord["y"]],3)
        pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"],self.elem.center.coord["y"]],[self.elem.center.coord["x"]+math.sin(math.pi/4)*self.size*3/10,self.elem.center.coord["y"]-math.sin(math.pi/4)*self.size*3/10],4)

class bullet():

    def __init__(self, x, y, angle, GV):
        self.elem = element(GV, [coord(x,y)], coord(x,y), speed = coord(10*math.cos(angle), -10*math.sin(angle)))
        GV.obj_list.append(self)

    def image(self, main, player=None, GV=None):
        x = self.elem.center.coord["x"]
        y = self.elem.center.coord["y"]
        pygame.draw.circle(main, (0,0,0), [int(x), int(y)], 5)

        x += self.elem.center.speed["x"] * GV.timeSpeed
        y += self.elem.center.speed["y"] * GV.timeSpeed
        if(x < 0 or x > 1980 or y < 0 or y > 1080):
            return True
        if(collision(player.elem.points_list, self.elem.points_list)):
            player.isAlive = False
        self.elem.center.coord["x"] = x
        self.elem.center.coord["y"] = y
        return False


class turret():

    def __init__(self, x, y, GV):
        self.angle_cannon = 0
        self.size = GV.size / 2.5
        self.dead = False
        self.fire = 20
        self.elem = element(GV, [coord(x + self.size, y), coord(x + self.size, y - int(self.size * 3 / 2)), coord(x - self.size, y - int(self.size * 3 / 2)), coord(x - self.size, y)], coord(x, y))
        GV.obj_list.append(self)


    def image(self, main, player=None, GV=None):

        pygame.draw.polygon(main, (0,0,0), [[self.elem.center.coord["x"] + self.size, self.elem.center.coord["y"]], [self.elem.center.coord["x"] - self.size, self.elem.center.coord["y"]], [self.elem.center.coord["x"] - int(self.size / 1.8), self.elem.center.coord["y"] - self.size], [self.elem.center.coord["x"] + int(self.size / 1.8), self.elem.center.coord["y"] - self.size]], 1)
        pygame.draw.arc(main, (0,0,0), [self.elem.center.coord["x"] - int(self.size / 2), self.elem.center.coord["y"] - self.size*3/2, self.size, self.size], 0, math.pi)
        if(player.elem.center.coord["x"] == self.elem.center.coord["x"]):
            if(player.elem.center.coord["y"] < self.elem.center.coord["y"]):
                self.angle_cannon = math.pi / 2
            else:
                self.angle_cannon = -math.pi / 2
        elif(player.elem.center.coord["x"] < self.elem.center.coord["x"]):
            if(player.elem.center.coord["y"] < self.elem.center.coord["y"]):
                self.angle_cannon = math.pi - math.atan((self.elem.center.coord["y"]-player.elem.center.coord["y"]) / (self.elem.center.coord["x"] - player.elem.center.coord["x"]))
            else:
                self.angle_cannon = math.pi
        else:
            if(player.elem.center.coord["y"] < self.elem.center.coord["y"]):
                self.angle_cannon = math.atan((self.elem.center.coord["y"]-player.elem.center.coord["y"]) / (player.elem.center.coord["x"] - self.elem.center.coord["x"]))
            else:
                self.angle_cannon = 0

        if(player.elem.center.coord["x"] < self.elem.center.coord["x"] - self.size):
            baseX = int(self.elem.center.coord["x"] + math.cos(self.angle_cannon) * self.size / 2)
            baseY = int(self.elem.center.coord["y"] - self.size - math.sin(self.angle_cannon) * self.size / 2)
            endX = baseX + int(math.cos(self.angle_cannon) * self.size /2)
            endY = baseY - int(math.sin(self.angle_cannon) * self.size / 2)
            pygame.draw.line(main, (0,0,0), [baseX, baseY], [endX, endY], 5)
        else:
            if(player.elem.center.coord["x"] < self.elem.center.coord["x"]):
                endX = self.elem.center.coord["x"] - self.size
                endY = self.elem.center.coord["y"] - self.size
                pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"] - int(self.size / 2), self.elem.center.coord["y"] - self.size], [endX, endY], 5)
            else:
                endX =self.elem.center.coord["x"] + self.size
                endY = self.elem.center.coord["y"] - self.size
                pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"] + int(self.size / 2), self.elem.center.coord["y"] - self.size], [endX, endY], 5)

        self.fire -= GV.timeSpeed
        if(self.fire > 20):
            self.fire = 20
        elif(self.fire < 0):
            bullet(endX, endY, self.angle_cannon, GV)
            self.fire = 20

        return False



    def getCoord(self):
        angle1 = utilitary.coord(self.elem.center.coord["x"] + self.size, self.elem.center.coord["y"])
        angle2 = utilitary.coord(self.elem.center.coord["x"] - self.size, self.elem.center.coord["y"])
        sommet = utilitary.coord(self.elem.center.coord["x"], int(self.elem.center.coord["y"] - 3 / 2 * self.size))

        return [angle1, angle2, sommet]


class flag():
    def __init__(self, x, y, size, GV):
        h=size/15
        self.color = color=(0,200,0)
        self.point_list=[[x+size-h, y], [x+size-h, y-size*3/2], [x, y-size*7/4+h/2], [x+size-h, y-size*2+h], [x+size-h, y-size*2], [x+size, y-size*2], [x+size, y]]
        self.elem=element(GV, [coord(x,y), coord(x+size, y), coord(x+size, y+2*size)], coord(x, y+2*size), coord(x,y))
        GV.obj_list.append(self)

    def image(self, main, player=None, GV=None):
        pygame.draw.polygon(main, self.color, self.point_list)
        return False
