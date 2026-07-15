import random
print("This is a number guessing game!")
print("Which difficulty do you want to play?\n1.Easy\n2.Medium\n3.Hard\n4.Godly")
diff=int(input("Enter the number of difficulty:"))
if diff==1:
    print("I am thinking of a number between 1 to 50.......\nCan you guess it?")
    num=random.randrange(1,50)
    print("Difficulty:Easy")
    def game():
        tries=0
        while tries<10:
            guess=int(input("Enter your guess:"))
            tries+=1
            if guess==num:
                print('You guessed the number correcty')
                print(f"Tries:{tries}")
                break
            elif guess>num:
                print("Your number is too high")
                print(f"Tries:{tries}")
            elif guess<num:
                print("Your number is too low")
                print(f"Tries:{tries}")
        else:
                print("GAME OVER , You used all your tries")
        with open ("Tries.txt","a") as gg:
                gg.write(f"\nEasy difficulty\nTries:{tries}")
    game()
if diff==2:
    print("Difficuty:Normal")
    print("I am thinking of a number between 1 to 100.......\nCan you guess it?")
    num=random.randrange(1,100)
    def game():
        tries=0
        while tries<11:
            guess=int(input("Enter your guess:"))
            tries+=1
            if guess==num:
                print('You guessed the number correcty')
                print(f"Tries:{tries}")
                break
            elif guess>num:
                print("Your number is too high")
                print(f"Tries:{tries}")
            elif guess<num:
                print("Your number is too low")
                print(f"Tries:{tries}")
        else:
                print("GAME OVER , You used all your tries")
        with open ("Tries.txt","a") as gg:
                gg.write(f"\nNormal difficulty\nTries:{tries}")
    game()
if diff==3:
    print("Difficulty:Hard")
    print("I am thinking of a number between 1 to 500.......\nCan you guess it?")
    num=random.randrange(1,500)
    def game():
        tries=0
        while tries<11:
            guess=int(input("Enter your guess:"))
            tries+=1
            if guess==num:
                print('You guessed the number correcty')
                print(f"Tries:{tries}")
                break
            elif guess>num:
                print("Your number is too high")
                print(f"Tries:{tries}")
            elif guess<num:
                print("Your number is too low")
                print(f"Tries:{tries}")
        else:
                print("GAME OVER , You used all your tries")
        with open ("Tries.txt","a") as gg:
                gg.write(f"\nHard difficulty\nTries:{tries}")
    game()
if diff==4:
    print("Difficulty:Godly")
    print("I am thinking of a number between 1 to 1000.......\nCan you guess it?")
    num=random.randrange(1,1000)
    def game():
        tries=0
        while tries<11:
            guess=int(input("Enter your guess:"))
            tries+=1
            if guess==num:
                print('You guessed the number correcty')
                print(f"Tries:{tries}")
                break
            elif guess>num:
                print("Your number is too high")
                print(f"Tries:{tries}")
            elif guess<num:
                print("Your number is too low")
                print(f"Tries:{tries}")
        else:
                print("GAME OVER , You used all your tries")
        with open ("Tries.txt","a") as gg:
                gg.write(f"\nGodly difficulty\nTries:{tries}")
    game()
