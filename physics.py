from utilitary import coord

class element():
    def __init__(self, GV, points_list, coord, speed=coord(0,0), accel=coord(0,0), tempo=1):
        self.center=physical_point(coord, speed, accel, tempo)
        self.points_list=points_list

        GV.elem_list.append(self)

    def update(self, obstacle_list):
        new_coord=self.center.move()
        for obstacle in obstacle_list:
            if not collision(obstacle.points_list, self.points_list):
                for point in self.points_list:
                    for coord in ["x","y"]:
                        point[coord]=new_coord[coord]-self.center.coord[coord]
                self.center.coord=new_coord


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

    def point_inside(p, x, y):
        if p[0]>x[0] and p[0]<x[1] and p[1]>y[0] and p[1]<y[1]:
            print(p,x,y)
            return True

        return False

    len1=len(hb1)
    len2=len(hb2)
    hb1=get_hit_box(hb1)
    hb2=get_hit_box(hb2)

    print(hb1, hb2)
    if len1==1 and len2==1:
        return False
    elif len1==1:
        return point_inside([hb1[0][0],hb1[1][0]], hb2[0], hb2[1])
    elif len2==1:
        return point_inside([hb2[0][0],hb2[1][0]], hb1[0], hb1[1])

    flag=False
    for i in range(2):
        for j in range(2):
            if point_inside([hb1[0][i],hb1[1][j]], hb2[0], hb2[1]) or point_inside([hb2[0][i],hb2[1][j]], hb1[0], hb1[1]):
                return True
    return False

g=9.81
