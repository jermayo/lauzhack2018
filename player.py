import pygame
import math
import utilitary as util
import physics
import objects as obj

class mister():

    def __init__(self, x, y, GV):
        self.angle_body=math.pi/2
        self.angle_l_arm=-2 * math.pi / 3
        self.angle_r_arm=-math.pi / 3
        self.angle_l_leg=-2 * math.pi / 3
        self.angle_r_leg=-math.pi / 3
        self.angle_l_knee=-math.pi / 16 * 9
        self.angle_r_knee=-math.pi / 16 * 7
        self.size=GV.size / 2.5
        self.health = 9
        self.energy = 1
        self.elem=physics.element(GV, None, util.coord(x,y), accel=util.coord(0,1))
        self.isAlive = True
        self.is_grounded=False
        self.on_wall=False
        GV.obj_list.append(self)

        self.running=False
        self.jumping=False



    def image(self, main, player=None, GV=None):

        old_coord=self.elem.center.coord
        self.elem.center.coord=self.elem.update_coord()
        old_points_list=self.elem.points_list
        self.elem.points_list=self.getCoord()
        self.is_grounded, self.on_wall=self.elem.check_collision(GV.elem_list, old_coord, old_points_list)


        self.energy -= (-GV.timeSpeed+1) / 100
        if(self.energy < 0):
            self.energy = 0
        #Body
        neckX = int(self.elem.center.coord["x"] + math.cos(self.angle_body) * 1.8 * self.size)
        neckY = int(self.elem.center.coord["y"] - math.sin(self.angle_body) * 1.8 * self.size)
        pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"], self.elem.center.coord["y"]], [neckX,neckY])
        #Head
        pygame.draw.circle(main, (0,0,0), [neckX, int(neckY - self.size / 2)], int(self.size / 2), 1)
        #arms
        shouldersX = int(self.elem.center.coord["x"] + 3 / 2 *  math.cos(self.angle_body) * self.size)
        shouldersY = int(self.elem.center.coord["y"] - 3 / 2 *  math.sin(self.angle_body) * self.size)
        pygame.draw.line(main, (0,0,0), [shouldersX, shouldersY], [int(shouldersX + math.cos(self.angle_l_arm) * self.size * 1.3), int(shouldersY -  math.sin(self.angle_l_arm) * self.size * 1.3)])
        pygame.draw.line(main, (0,0,0), [shouldersX, shouldersY], [int(shouldersX + math.cos(self.angle_r_arm) * self.size * 1.3), int(shouldersY -  math.sin(self.angle_r_arm) * self.size * 1.3)])
        #legs
        legLX = int(self.elem.center.coord["x"] + math.cos(self.angle_l_leg) * self.size)
        legLY = int(self.elem.center.coord["y"] - math.sin(self.angle_l_leg) * self.size)
        legRX = int(self.elem.center.coord["x"] + math.cos(self.angle_r_leg) * self.size)
        legRY = int(self.elem.center.coord["y"] - math.sin(self.angle_r_leg) * self.size)
        pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"], self.elem.center.coord["y"]], [legLX, legLY])
        pygame.draw.line(main, (0,0,0), [self.elem.center.coord["x"], self.elem.center.coord["y"]], [legRX, legRY])
        pygame.draw.line(main, (0,0,0), [legLX, legLY], [int(legLX + math.cos(self.angle_l_knee) * self.size * 0.8), int(legLY - math.sin(self.angle_l_knee) * self.size * 0.8)])
        pygame.draw.line(main, (0,0,0), [legRX, legRY], [int(legRX + math.cos(self.angle_r_knee) * self.size * 0.8), int(legRY - math.sin(self.angle_r_knee) * self.size * 0.8)])
        return False

    def state(self, time, side=None):
        if side=="RIGHT":
            #self.elem.center.coord["y"] += math.cos(time*2)/30*self.size
            self.angle_l_leg = 3 / 16*math.pi * math.cos(time) - math.pi / 2
            self.angle_r_leg = 3 / 16*math.pi * math.cos(time + math.pi) - math.pi / 2
            self.angle_l_arm = 3 / 16*math.pi * math.cos(time) - math.pi / 2
            self.angle_r_arm = 3 / 16*math.pi * math.cos(time + math.pi) - math.pi / 2
            if(time % (2*math.pi) < math.pi):
                self.angle_l_knee = 3 / 16*math.pi * math.cos(time) - math.pi / 8 * 5
            elif(time % (2*math.pi) < 14 * math.pi / 8):
                self.angle_l_knee = -13 * math.pi / 16
            else:
                self.angle_l_knee = -13 * math.pi / 16 + 6 * math.pi / 16 * math.sin(2 * (time - 14 * math.pi / 8))
            if((time + math.pi) % (2*math.pi) < math.pi):
                    self.angle_r_knee = 3 / 16*math.pi * math.cos(time + math.pi) - math.pi / 8 * 5
            elif((time + math.pi) % (2*math.pi) < 14 * math.pi / 8):
                    self.angle_r_knee = -13 * math.pi / 16
            else:
                    self.angle_r_knee = -13 * math.pi / 16 + 6 * math.pi / 16 * math.sin(2 * (time + math.pi - 14 * math.pi / 8))
        elif side=="LEFT":
            #self.elem.center.coord["y"] += math.cos(time*2)/30*self.size
            self.angle_l_leg = math.pi - (3 / 16*math.pi * math.cos(time) - math.pi / 2)
            self.angle_r_leg = math.pi - (3 / 16*math.pi * math.cos(time + math.pi) - math.pi / 2)
            self.angle_l_arm = math.pi - (3 / 16*math.pi * math.cos(time) - math.pi / 2)
            self.angle_r_arm = math.pi - (3 / 16*math.pi * math.cos(time + math.pi) - math.pi / 2)
            if(time % (2*math.pi) < math.pi):
                self.angle_l_knee = math.pi - (3 / 16*math.pi * math.cos(time) - math.pi / 8 * 5)
            elif(time % (2*math.pi) < 14 * math.pi / 8):
                self.angle_l_knee = math.pi - (-13 * math.pi / 16)
            else:
                self.angle_l_knee = math.pi - (-13 * math.pi / 16 + 6 * math.pi / 16 * math.sin(2 * (time - 14 * math.pi / 8)))
            if((time + math.pi) % (2*math.pi) < math.pi):
                    self.angle_r_knee = math.pi - (3 / 16*math.pi * math.cos(time + math.pi) - math.pi / 8 * 5)
            elif((time + math.pi) % (2*math.pi) < 14 * math.pi / 8):
                    self.angle_r_knee = math.pi - (-13 * math.pi / 16)
            else:
                    self.angle_r_knee = math.pi - (-13 * math.pi / 16 + 6 * math.pi / 16 * math.sin(2 * (time + math.pi - 14 * math.pi / 8)))
        else:
            self.angle_body=math.pi/2
            self.angle_l_arm=-2 * math.pi / 3
            self.angle_r_arm=-math.pi / 3
            self.angle_l_leg=-2 * math.pi / 3
            self.angle_r_leg=-math.pi / 3
            self.angle_l_knee=-math.pi / 16 * 9
            self.angle_r_knee=-math.pi / 16 * 7

    def getCoord(self):
        return [util.coord(self.elem.center.coord["x"] + 0.5 * self.size, self.elem.center.coord["y"]+ 1.6 * self.size), util.coord(self.elem.center.coord["x"] - 0.5 * self.size, self.elem.center.coord["y"]+ 1.6 * self.size), util.coord(self.elem.center.coord["x"] + 0.5 * self.size, self.elem.center.coord["y"]- 2.3 * self.size), util.coord(self.elem.center.coord["x"] - 0.5 * self.size, self.elem.center.coord["y"]- 2.3 * self.size)]
