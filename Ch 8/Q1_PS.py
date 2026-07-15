n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("Enter a number:"))
def greatest(n1,n2,n3):
    if (n1>n2 and n1>n3):
        print("The largest number is",n1)
    elif (n2>n1 and n2>n3):
        print("The largest number is",n2)
    else:
        print("The largest number is",n3)
greatest(n1,n2,n3)