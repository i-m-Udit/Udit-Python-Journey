try:
    a=int(input("Enter a number:"))
    print(a)

except ValueError:
    print("Enter a valid number")

except Exception as e :
    print(e)

finally:  
    print("Thank You") #this gets executed every time and this is mainly used in functions