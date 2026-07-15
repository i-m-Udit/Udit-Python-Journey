class Random:
    a=45
    @staticmethod #It means this function does not require any object
    def greet():
        return "Good morning"
object=Random()
object.a=0
print(object.greet(),object.a)
#Yes it does change the class attribute 