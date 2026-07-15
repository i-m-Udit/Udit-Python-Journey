class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,other):
        new_r=self.r+other.r
        new_i=self.i+other.i
        return Complex(new_r,new_i)
    def __mul__(self,other):
        new_r=(self.r*other.r)-(self.i*other.i)
        new_i= self.r * other.i + self.i * other.r 
        return Complex(new_r,new_i)
    def __str__(self):
        return f"{self.r}+{self.i}i"
c1=Complex(1,2)
c2=Complex(3,4)
sum_result=c1+c2 #Automatically calls __add__
mult_result=c1*c2 #Automatically calls __mul__
print("Sum:",sum_result)
print("Multiplication:",mult_result)