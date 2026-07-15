def div(a:int,b:int) -> int:
    try :
        print(a/b)
    except ZeroDivisionError:
        print("Python doesnt support division by 0 but ans is infinite")
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    div(a,b)
except ValueError:
    print('Enter valid numbers!')