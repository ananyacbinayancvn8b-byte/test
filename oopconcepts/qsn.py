class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        print("area",3.14*radius*radius)

c=Circle(5)


class Rect(Shape):
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
        print("area",len*bre)

r=Rect(5,9)


class Square(Shape):
    def __init__(self,s):
        self.s=s
        print("area",s*s)

sq=Square(8)
       
sq.area()

