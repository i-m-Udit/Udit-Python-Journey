with open("6_and_7_mining.txt") as g:
    content=g.read()
if ("python") in content:
    print('We found the word python in the given file')
else:
    print("There is no word named python in the given file")