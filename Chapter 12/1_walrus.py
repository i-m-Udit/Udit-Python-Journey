i=0
list1=[]
while i==0:
    if (user := input("Enter your name:")).lower() != "stop": #Used to assign values in a condition or something similar
        list1.append(user)
        print(user)
    else:
        print(list1)
        break