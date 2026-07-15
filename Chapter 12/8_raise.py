a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if b==0:
    raise ZeroDivisionError("Python doesnt support division by 0")
else:
    print(a/b)