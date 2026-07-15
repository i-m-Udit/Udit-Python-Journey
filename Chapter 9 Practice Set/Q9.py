with open("8_Q.txt") as r:
    content1=r.read()
with open("9_Creating.txt") as f:
    content2=f.read()
if content1==content2:
    print('Yes the contents of both files are the same')
else:
    print("No they are not same")