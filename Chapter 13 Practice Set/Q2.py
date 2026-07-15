try:
    name=str(input("Enter your name:"))
    marks=int(input("Enter your marks:"))
    number=input("Enter your mobile number:")
    if len(number)!=10:
        print("Wrong length of your mobile number!!")
    else:
        pass
    ans="The name of the student is {} , his marks are {} and phone number is {}".format(name,marks,number)
    print(ans)
except ValueError:
    print("Wrong value entered!!")