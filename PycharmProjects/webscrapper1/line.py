import math
class LineMethods():
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def slope(self):
        try:
            return "Slope is "+str(float(self.y2-self.y1)/(self.x2-self.x1))
        except Exception as ex:
            print(ex)
            return "Denominator is ZERO.. madafaka"
    def length(self):
        return "distance is"+str(float(math.sqrt((self.y2-self.y1)*(self.y2-self.y1)+(self.x2-self.x1)*(self.x2-self.x1))))
line1 = LineMethods(2,3,5,6)
line2 = LineMethods(1,2,9,6)
print(line1.slope())
print(line2.slope())
print(line1.length())
print(line2.length())

