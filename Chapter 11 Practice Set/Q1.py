class two_d_vector:
    def __init__(self,length,breadth):
        self._length=length
        self._breadth=breadth
        return self._length , self._breadth
class three_d_vector(two_d_vector):
    def __init__(self,length,breadth,height):
        super().__init__(length,breadth)
        self._height=height
        print(f"Length:{self._length},Breadth:{self._breadth},Height:{self._height}")
something=three_d_vector(2,3,4) #Hi