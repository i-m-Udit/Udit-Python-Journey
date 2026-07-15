n=int(input("Enter a number:"))
for i in range (1,n+1): #Running a loop
    spaces=n-i   #Spaces are given number - i and it will work infinitely because of the loop
    stars=(2*i)-1 #This is the formula of stars printing because we need to print odd number of stars
    print(" "*spaces,stars*"*")#Now this is used to print the sapces and stars