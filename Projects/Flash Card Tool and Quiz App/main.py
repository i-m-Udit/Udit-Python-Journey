import json
def lines():
    print("------------------------------------------------------")
lines()
print("Welcome to the Quiz and FlashCard tool")
lines()
print("What do you want to do?\n1.Review the flash cards\n2.Take a quiz from the flash cards\n3.Add a new flashcrad\n4.Exit")
choice0=int(input("Enter the number of your choice:"))
if choice0==1:
    lines()
    print('Welcome to the reviewing section of your flashcards.\nWhich types of flash cards do you want to review?\n1.Notes type\n2.QnA type')
    choice1=int(input("Enter the number of your choice :"))
    if choice1==1:
        with open ("Notes.txt") as notes :
            content=notes.read()
            if content=="":
                print("Error! No notes found in the given file")
            else:
                print("Here are your notes!")
                print(content)
    elif choice1==2:
        with open ("QnA.txt") as qna :
            my_dict=json.load(qna)
            for key in my_dict:
                print(f"Question:{key}")
                input("Press ENTER for the answer")
                print(f"Answer:{my_dict[key]}\n")
                input("Press ENTER for the next Question")
    else:
        print("Wrong choice entered!")
    lines()
if choice0==2:
    lines()
    print("You can only take the quiz of the ques and ans type!\nAre you ready?\nHere is the first question-->")
    with open ("QnA.txt") as qna :
            my_dict=json.load(qna)
            for key in my_dict:
                print(f"Question:{key}")
                ans=input("Enter your answer:")
                if ans.lower()==my_dict[key].lower():
                    print("Your answer is correct!")
                    input("Press ENTER for the next question\n")
                else:
                    print(f"Your answer is wrong! Correct answer ;{my_dict[key]}\n")
                    input("Press ENTER for the next question")
            print("Questions are finished!")
    lines()
if choice0==3:
    lines()
    print("Which type of flashcards do you want to add?\n1.Notes\n2.QnA")
    choice2=int(input("Enter your choice:"))
    if choice2==1:
        n=int(input("How many notes do you want to enter?:"))
        with open ("Notes.txt",'a') as notes :
            def adding_notes():
                    Notes=input("Enter your notes:")
                    notes.write(f"{Notes}\n")
            for i in range (1,n+1):
                adding_notes()
            print("Notes have been successfully added!")
    if choice2==2:
        n=int(input("How many questions do you want to enter?:"))
        with open ("QnA.txt","r") as qna :
             content=qna.read().strip()
             if content:
                  m_dict=json.load(qna)
             else:
                  m_dict={}
        for i in range (n):
            Question=input("Enter your question:")
            Answer=input("Enter your answer:")
            m_dict[Question]=Answer
        with open ("QnA.txt","w") as adding_qna:
            json.dump(m_dict,adding_qna,indent=4)
        print("Your flashcards have been successfully saved!")
    lines()
if choice0==4:
    lines()
    print("Thank you for using our application")
    lines()
