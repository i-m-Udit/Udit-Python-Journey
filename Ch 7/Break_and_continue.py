#The break statement is used to come out of the loop when it meets the required condition
for i in range(0,81):
    if i==7:
        break
    print(i)
#Continue statement is used to skip the part of code when it meets the required condition
for i in range(0,5):
    if i==3:
        continue
    print(i)
#Pass statement tells the program to do nothing
for i in range(1,6):
    pass
#Pass statement means do not do this now we will do this later 
#Without pass the program will give error
#Pass is a null statement