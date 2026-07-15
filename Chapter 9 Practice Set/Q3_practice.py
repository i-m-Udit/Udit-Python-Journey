#Generetaing squares from 2 to 30
def Squares(n):
    square=""
    square+=f"{n} X {n} = {n*n}"
    with open(f"Squares/Square_{n}.txt","w") as s:
        s.write(square)
for n in range (2,41):
    Squares(n)