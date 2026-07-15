b=54
def func():
    a=3 #this is the local variable of func()
    global b
    b=4
    #changes the global variable b to 4
    print(a,b)
a=58 #global variable
print(a)
print(b)
func()
print(b) #to change the global variable in a func we have to first run the func