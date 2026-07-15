n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("Enter a number:"))
n4=int(input("Enter a number:"))
if (n1>n2 and n1>n3 and n1>n4):
    print("The largest number is",n1)

elif (n2>n1 and n2>n3 and n2>n4):
    print("The largest number is",n2)

elif (n3>n2 and n3>n1 and n3>n4):
    print("The largest number is",n3)

else:
    print("The largest number is",n4)