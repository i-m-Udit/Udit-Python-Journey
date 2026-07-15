class Random:
    a=45
object=Random()
object.a=0
print(object.a) #Prints a instance attribute because instance attribute is given
print(Random.a) #Prints a class attribute because we are not saying to print the instance attribute
#Class attribute is not changed , it depends on user what he is using