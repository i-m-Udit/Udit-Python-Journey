try:
    a=int(input("Enter a number:"))
    print(a)

except ValueError:
    print("Enter a valid number")

except Exception as e :
    print(e)
    
print("Thank You")