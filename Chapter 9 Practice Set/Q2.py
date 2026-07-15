import random #Importing random module
def game():  #Making a function
    print('You are playing a luck game...')
    score=random.randint(1,100) #Taking the score as random
    with open("2_hiscore.txt") as f: #Opening the hiscore file in read mode
        hiscore=f.read()  #Reading the contents of the file
    if (hiscore!=""):  #If hiscore is not as blank
        hiscore=int(hiscore)  #Converting the hiscore into integers
    else: #hiscore==""
        hiscore=0 #If hiscore is blank it will be taken as 0
    print(f"The score you get based on your luck is {score}")
    if (score>hiscore or hiscore==""): #If hi score is smaller than score or hiscore is 0
        with open("2_hiscore.txt","w") as f: #Opening the hiscore.txt file in write mode
            f.write(str(score))  #Writing the new score as a string because write mode only takes the value in it as a string and not a integer or other variable type
    return score #Taking the value of score
game() #Running the function