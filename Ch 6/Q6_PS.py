m=int(input("Enter your marks:"))
if m>90 and m==100:
    print("Excellent")
elif m>80 and m==90:
    print("A")
elif m>70 and m==80:
    print("B")
elif m>60 and m==70:
    print("C")
elif m>50 and m==60:
    print("D")
elif m<50:
    print("F")
else:
    print("Wrong marks entered")