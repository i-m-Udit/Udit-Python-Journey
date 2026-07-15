class Vector:
    n=3
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def __add__(self,other):
        new_l=self.l+other.l
        new_b=self.b+other.b
        new_h=self.h+other.h
        return Vector(new_l,new_b,new_h)
    def __mul__(self,other):
        return self.l * other.l + self.b * other.b + self.h * other.h #We want to return a single value not 3
    def __str__(self):
        return f"{self.l}i+{self.b}j+{self.h}k"
c=Vector(1,2,3)
d=Vector(4,5,6)
result_sum=c+d
result_product=c*d
print(f"Sum:{result_sum}")
print(f"Dot product:{result_product}")