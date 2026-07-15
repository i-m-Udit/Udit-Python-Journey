class Vector:
    def __init__(self,l):
        self._l=l
    def __len__ (self):
        return(len(self._l))
c=Vector([1,2,3])
print(len(c))