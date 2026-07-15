try:
    n=int(input("Enter a number:")) 
    lis1=[n]
    tableList=[n*i for i in range(1,11)]
    [print (f"{n} X {i} = {n*i}") for i in range (1,11)]
except ValueError:
    print("Please enter a valid number!")