class Shapes:
    def __init__(self):
        self._area=0
class Rectangle(Shapes):
    def finding_area(self,l,b):
        self._area=l*b
        return f"The area of this rectangle is {self._area}"
class Circle(Shapes):
    def finding_area(self,radius):
        self._area=3.14*radius*radius
        return f"The area of this circle is {self._area}"
class Triangle(Shapes):
    def finding_area(self,base,height):
        self._area=0.5*base*height
        return f"The area of this triangle is {self._area}"
area=0 #Initializing area as 0(it will be updated when the class runs)
g=Triangle()
print (g.finding_area(2,4))
h=Circle()
print (h.finding_area(7))
i=Rectangle()
print (i.finding_area(5,10))