print('This program will check whether Twinkle word is in a poem or not')
f=open("1_poems.txt")
text=f.read()
if "Twinkle" in text:
    print("True")
else:
    print("False")
f.close