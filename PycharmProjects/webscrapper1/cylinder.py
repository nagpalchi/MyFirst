class Cylinder():
    pi=22/7
    def __init__(self,height,radius):
        self.height = height
        self.radius= radius
    def volume(self):
        return self.pi*self.radius*self.radius*self.height
    def surfaceArea(self):
        return 2*self.pi*self.radius*self.height
cylinder1 = Cylinder(10,20)
print("Surface Area is "+str(cylinder1.surfaceArea())+"Sq.cm")
print("Volume is "+str(cylinder1.volume())+"Cubic.cm")