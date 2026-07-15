m1=int(input("Enter your marks:"))
m2=int(input("Enter your marks:"))
m3=int(input("Enter your marks:"))
if m1>33:
    print("You are passed in subject 1")
else:
    print("You failed in subject 1")

if m2>33:
    print("You are passed in subject 2")
else:
    print("You failed in subject 2")

if m3>33:
    print("You are passed in subject 3")
else:
    print("You failed in subject 3")

if (m1+m2+m3)/3==40 or (m1+m2+m3)/3>40 :
    print("You are passed in the test")
else:
    print("You are failed in the test")