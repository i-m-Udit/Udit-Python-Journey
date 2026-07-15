import math
n=int(input("Enter a no.:"))
class Calculator:
    def __init__(self):
        self.n=n
    def Sq(self):
            print(f"The sq of n is {self.n*self.n}")
    def SqRoot(self):
            print(f"The sqRoot of n is {math.sqrt(self.n)}")
    def Cube(self):
            print(f"The cube of n is {self.n*self.n*self.n}")
    def All(self):
          print(f'Sq of n:{self.n*self.n}\nSqRoot of n:{math.sqrt(self.n)}\nCube of n:{self.n*self.n*self.n}')
A=Calculator()
A.All()