print('Welcome to the python library!')
booklist=["Harry Potter","The 48 Laws of power","Jungle Book"]
print("Please choose an option:\n1.Display Available Books\n2.Borrow a book \n3.Return a book\n4.Add a new book\n5.Exit")
choice=int(input("Enter the number based on your choice:"))
if choice==1:
    print(f"The available books are:{booklist}")
    print("Do you want to borrow a book?\nRun the program again and choose option 2!")
if choice==2:
    print(f"The available books are:{booklist}")
    name=input("Enter your name:")
    book=input("Enter the exact NAME of the book:")
    print("You have borrowed the book and you have to return this in under a week\nYour purchase has been saved successfully")
    with open ('Book_List.txt','w') as info:
        info.write(f"Name:{name}\nBook borrowed:{book}\n")
if choice==3:
    print("It looks like you have came back to return the book!")
    returnbook=input("Enter the exact name of the book you have borowed:")
    with open ("Book_List.txt","r") as reading:
        data=reading.read()
    if returnbook in data:
        print("Your book has been successfully returned!")
        with open ("Book_List.txt","w") as writing :
            updated_data=data.replace(returnbook,"NONE")
            writing.write(updated_data)
    elif data=="":
        print("You have not borrowed any book")
    else:
        print(f"You have not borrowed any book named {returnbook}\nIf you have borrowed then retry and enter the correct name of the book carefully")
if choice==4:
    print("Oh! it looks like you are a author!")
    newbook=input("Enter the name of your book:")
    booklist.append(newbook)
    print("Your book has been successfully added")
    print(f"Here is the updated list:{booklist}")
if choice==5:
    print('You have exited the library')
