from utilitary import coord

import pygame

class element():
    def __init__(self, GV, points_list, coord, speed=coord(0,0), accel=coord(0,0), tempo=1):
        self.center=physical_point(coord, speed, accel, tempo)
        self.points_list=points_list

        GV.elem_list.append(self)

    def update_coord(self):
        return self.center.move(), collision(obstacle.points_list, self.points_list)

    def check_collision(self, elem_list, old_coord, old_col_x, old_col_y):
        for obstacle in elem_list:
            col_x,col_y=collision(obstacle.points_list, self.points_list)
            if col_x and col_y:
                self.center.coord["x"]=old_coord["x"]
                self.center.coord["y"]=old_coord["y"]

                print(old_col_x, old_col_y)
                self.center.accel["y"]=0
                self.center.speed=coord(0,0)
                return True
        self.center.accel["y"]=1
        return False



class physical_point():
    def __init__(self, coord, speed, accel, tempo):
        self.coord=coord
        self.speed=speed
        self.accel=accel
        self.tempo=tempo

    def move(self):
        t=self.tempo
        new_coord={}
        for i in ["x","y"]:
            new_coord[i]=self.accel[i]*t*t/2+self.speed[i]*t+self.coord[i]
            self.speed[i]+=self.accel[i]*t
        return new_coord


def collision(hb1, hb2):
    #[[min_x, max_x],[min_y,max_y]]

    def get_hit_box(hb):
        l=[]
        for coord in ["x","y"]:
            l2=[]
            for point in hb:
                l2.append(point[coord])
            l.append([min(l2),max(l2)])
        return l

    def point_inside(p, x):
        if int(p)>int(x[0]) and int(p)<int(x[1]):
            return True
        return False

    if hb1==hb2:
        return False, False
    len1=len(hb1)
    len2=len(hb2)
    hb1=get_hit_box(hb1)
    hb2=get_hit_box(hb2)

    if len1==1 and len2==1:
        return False, False

    elif len1==1:
        return point_inside(hb1[0][0], hb2[0]), point_inside(hb1[1][0], hb2[1])
    elif len2==1:
        return point_inside(hb2[0][0], hb1[0]), point_inside(hb2[1][0], hb1[1])

    x,y=False, False
    for i in range(2):
        if point_inside(hb1[0][i], hb2[0]) or point_inside(hb2[0][i], hb1[0]):
            x=True
        if point_inside(hb1[1][i], hb2[1]) or point_inside(hb2[1][i], hb1[1]):
            y=True
    return x,y

g=9.81
