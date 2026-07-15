print("We will help you find the english of Kutta,Billi,Kursi")
d={"Kutta":"Dog",
   "Billi":"Cat",
   "Kursi":"Table"}
n=input("Enter the word which you want the english of:" )
if n in d:
    print("The english of the given word is:",d.get(n))
else:
    print("Your word is not in the given Dictionary")