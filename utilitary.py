import math

class GlobalVariable():
    def __init__(self):
        self.obj_list=[]
        self.main=0

def coord(x,y):
    return {"x":x, "y":y}
#returns cartesian coord from polar
def cart_coord(radius, theta):
    return radius*math.cos(theta), radius*math.sin(theta)

#returns polar coord from cartesian
def polar_coord(x, y):
    if x==0:
        if y>0:
            angle=math.pi/2
        elif y<0:
            angle=-math.pi/2
        elif y==0:
            angle=0
    else:
        angle=math.atan(y/x)
    return math.sqrt(x*x+y*y), angle
