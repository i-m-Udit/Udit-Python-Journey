#importing
import json 
import time

a = True

#welcome the user
print("Welcome! This is a contact book.\n")

#taking the user input
user = input("Enter your name : ")

# reading the file if file is not present then  creating a new file 
try:
    with open(f"{user}.json", "r") as f:
        data = f.read()
        if data == "":
            user_dict = {}
        else:  #if file is present and there is some thing moving the cursor from top
            f.seek(0)
            user_dict = json.load(f)

except FileNotFoundError:
    with open (f"{user}.json" , "w") as g:
        user_dict = {}

while a == True:
    print("\nWhat do you want to do?")

    print("\n1. Add a contact \n2. View all contacts  \n3. Search by name  \n4. Update a contact  \n5. Delete a contact  \n6. Exit \n")

    try:
        choice = int(input("( 1 / 2 / 3 / 4 / 5 / 6)  > ")) #taking the choice from user

        if choice == 1:
            print("\nHow many contact do you want to add?\n")
            contacts_num = int(input("> "))

            for i in range(1, contacts_num + 1):
                name = input("\nEnter the name for the contact : ")
                contact = int(input("\nEnter the contact number : "))
                email = input("\nEnter the gmail : ")
                user_dict[name] = {"contact": contact, "email": email}

            with open(f"{user}.json", "w") as user_file:
                json.dump(user_dict, user_file, indent=4) #dumping the user_file bcz it is a part of syntax
                print("\nContacts saved!")

        if choice == 2:

            print("\nHere are all of your contacts -")
            time.sleep(1)

            if user_dict != "":
                for name, info in user_dict.items():
                    print(f"\nName: {name}, Contact: {info['contact']}, Email: {info['email']}") # giving the valurs through the keys (for eg contact and email)

            else :
                print("\nThere are no contacts")

        if choice ==3 :

            try :
                name = input("\nEnter the name of the contact: ")
                print("\nSearching by name......")
               
                if name in user_dict:
                        print("\nSuccessfully found the contact!\n")
                        print(name , user_dict[name])
                else:
                        print("\nFailed to find contact from the given name!")

            except Exception as e :
                print("\nError : " , e)

        if choice == 4:

            try:
                with open (f"{user}.json" , "w") as user_file:
                    name = input("\nEnter the name of the contact which you want to update : ")

                    print("\nSearching by name......")
                    time.sleep(1)

                
                    if name in user_dict:
                            info = user_dict[name]
                            print("Successfully found the contact!")
                            print(f"Name: {name}, Contact: {info['contact']}, Email: {info['email']}")
                            new_contact_num = input("Enter the contact number for updated contact : ")
                            new_gmail = input("Enter the gmail for updated contact : ")

                            user_dict[name] = {"contact": new_contact_num, "email": new_gmail}
                            json.dump(user_dict , user_file , indent=4)
                            print("\nContact changed successfully!!")

                    else:
                            print("Failed to find contact from the given name!")

            except Exception as e:
                print("Error : " , e)

        if choice==5:
            try:    
                name = input("\nEnter the name of the contact which you want to delete : ")

                print("\nSearching by name......")
                
                if name in user_dict:
                        print("\nSuccessfully found the contact!")
                        info = user_dict[name]
                        print(f"\nName: {name}, Contact: {info['contact']}, Email: {info['email']}")
                        del user_dict[name] #del is used to delete any key value pair of dict from key
                        with open (f"{user}.json" , "w") as user_file:
                            json.dump(user_dict , user_file , indent=4)
                            print("\nContact successfully deleted!")
                else:
                        print("\nFailed to find the contact!!")

            except Exception as e:
                print("Error : " , e)
        if choice == 6:
            print("\nThank you for using this app!")
            a = False
    except Exception as e:
        print("[DEBUG] Error :" , e)
