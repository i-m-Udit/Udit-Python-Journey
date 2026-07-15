with open("6_and_7_mining.txt") as g: #Opening the file in read mode
    lines=g.readlines() #Reading ALL the lines
lineno=1  #Giving that start reading from line 1
for line in lines: #Makaing a variable line and starting a loop for all the read lines
    if ("python") in line: #If found python in line variable which is a part of all the lines 
        print(f'We found the word python in the given file at line {lineno}') #Printing the lline number
        break #Once we got the line number we will end the looop
    lineno+=1 #Adding 1 in lineno to read eachline 
else:
    print("There is no word named python in the given file") #Else the loop is exhausted when no python is found in all of the line
#Line and line no work parralel to each other    