class Random:  #Making a class
    def __init__(self,value):
        self._value=value   
    @property #This is a getter
    def value(self):
        return self._value
    @value.setter #This is a setter
    def value (self,new_value):
        self._value=new_value
g=Random(7)
g.value=10
print(g._value)