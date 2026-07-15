word="Donkey"

with open("4_and_5_file.txt","r") as f: #Opening file in read mode
    content=f.read()
replacing = content.replace(word,"#"*len(word)) #Giving how to replace the word donkey
with open("4_and_5_file.txt","w") as f: #Opening the file in read mode
    f.write(replacing) #Writing the given steps
    print('Replacing Donkey with # is done in your file.txt')