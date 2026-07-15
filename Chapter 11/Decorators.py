def greet(main_code): #Making a funcion for DECORATOR
    def greeting_func(): #Main code for the decorator
        print("Good Morning!")
        main_code() #Running the main code of the programme
        print("Thank you for using this code!")
    return greeting_func#Returning the whole decorator code with the main code 

@greet #Using the decorator
def hello(): #The main code
    print("Hello world!") 

hello() #Running the main code with the decorator
# OR
def hello():
    print("Hello World!")
greet(hello)() #Empty backets are used here to run the function ,if we will not use the empty brackets the code will not be execued 

