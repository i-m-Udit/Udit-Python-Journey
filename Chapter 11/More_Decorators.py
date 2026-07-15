def greet(add): #Making the function for greetings
    def greeting(*args,**kwargs): #args and kwargs are used to take arguments if here is any for the decorators
        print('Hello')
        add(*args,**kwargs)
        print('Bye Bye')
    return greeting
def adding(a,b):
    print(a+b)
greet(adding)(1,2) #Giving the arguments which are taken by args and kwargs
#args is used to pass values in the form of tuples
#kwargs is used pass arguments in the form of dictionaries Key:value pairs
#OR]
@greet
def adding(a,b):
    print(a+b)
adding()