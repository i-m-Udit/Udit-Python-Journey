class Student:
    def __init__(self,marks):
            self._marks=marks
    @property
    def marks(self):
          return self._marks
    @marks.setter
    def marks(self,new_marks):
          if new_marks<101 :
                self._marks=new_marks
          else:
                print("Wrong marks entered") 
Rohan=Student(100)
Rohan.marks=101
print(Rohan.marks)