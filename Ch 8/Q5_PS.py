n=int(input("Enter a number:"))
i=1
def stars(n):
    while i<=n:
        print("*"*n)
        n-=1
stars(n)