import random
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
                      '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']

def new_P():
    print("Do you want a new password? (Yes/No)")
    choice=input("What is your choice?:")
    if choice.lower()=="yes":
        length=int(input("Enter the length of password you want: (Minimum 8 length is recomendded:)"))                     
        def Password(length):
                uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

                lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

                special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
                                    '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']
                password=""
                for i in range (1,length+1):
                        password+=random.choice(lowercase_letters+uppercase_letters+digits+special_characters)
                print('Here is your password:')
                print( password )
        Password(length)
    else:
        print("Thank you for using this app!")
password=input("Enter your password:")
points=0
if len(password) >= 8:
    points+=1
else:
    pass
for char in uppercase_letters:
    if char in password:
        points+=1
        break
    else:
        pass
for char in lowercase_letters:
    if char in password:
        points+=1
        break
    else:
        pass
for char in digits:
    if char in password:
        points+=1
        break
    else:
        pass
for char in special_characters:
    if char in password:
        points+=1
        break
    else:
        pass
if points==5:
    print("Good job! Your password is STRONG!")
elif points==4:
    print("Password strength : MEDIUM")
    new_P()
else:
    print("Password strength : WEAK")
    new_P()
