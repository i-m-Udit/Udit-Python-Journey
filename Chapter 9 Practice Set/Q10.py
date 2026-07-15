with open("10_Deleting.txt") as c:
    content=c.read()
content=content.replace(content,"")
with open("10_Deleting.txt","w") as d:
    d.write(content)