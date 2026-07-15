print('This is a password generator!')
length=int(input("Enter the length of password you want:"))                     
def Password(length):
    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    special_chars = list('!@#$%^&*()')
    password=""
    for i in range (1,length+1):
        import random
        password+=random.choice(letters+numbers+special_chars)
    print('Do you want to save this password to Passwords.txt?\nGive your response in Yes or No')
    response=input("Your response:")
    if response.lower== "yes" :
        with open ("Passwords.txt",'r') as r:
            content=r.read()
        with open ('Passwords.txt','w') as w:
            w.write(f"\nYour password is:{(password)}")
            print('Your password has been successfully saved!')
    else:
         pass
    print('Here is your password:')
    print( password )
Password(length)
