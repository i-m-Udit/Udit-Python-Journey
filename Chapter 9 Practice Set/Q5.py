word="Donkey"
with open("4_and_5_file.txt") as c:
    content=c.read()
    if "Donkey" in content:
         print('You have used a censored word now you will not be abe to use it ')
    content=content.replace(word,"#"*len(word))
    with open("4_and_5_file.txt","w") as e:
        e.write(content)