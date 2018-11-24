from utilitary import coord


class ground():
    def __init__(self, coord):
        self.coord=self.coord


class physical_point():
    def __init__(self, object_list, coord=coord(0,0), speed=coord(0,0), accel=coord(0,0), tempo=1):
        self.coord=coord
        self.speed=speed
        self.accel=accel
        self.tempo=tempo
        object_list.append(self)

    def update(self, obstacle_list):
        t=self.tempo
        new_coord={}
        for i in ["x","y"]:
            new_coord[i]=self.accel[i]*t*t/2+self.speed[i]*t+self.coord[i]
#        for obstacle in obstacle_list:
#            if collision(obstacle.coord, )

    def draw(self, object_list):
        self.update(object_list)

def collision(hb1, hb2):
    #[[min_x, min_y],[min_y,max_y]]
    def get_hit_box(hb):
        l=[]
        for coord in ["x","y"]:
            l2=[]
            for point in hb:
                l2.append(point[coord])
            l.append([min(l2),max(l2)])
        return l

    hb1=get_hit_box(hb1)
    hb2=get_hit_box(hb2)

    print(hb1, hb2)

    for i in range(2):
        for j in range(2):
            if hb1[i][j]>hb2[i][0] and hb1[i][j]<hb2[i][1]:
                return True

    return False



    min_y=min([i for i in hb1["x"]])
    max_y=max([i for i in hb1["x"]])

    return False
g=9.81
