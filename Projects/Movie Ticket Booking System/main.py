try:
    import time
    import json
    import random
    import os

    print("Welcome to the Movie World! \nA movie theatre where you can watch movies ! \nWe have the cheapest price for the tickets!\n\n")
    time.sleep(1)

    movies = ["The Lion Queen" , "Ms Dhobi : The Untold Story" , "Bhool Guliyaa 99" , "The CineCraft Movie"]

    movie_prices = {movies[0]:200 , 
                    movies[1] : 150 , 
                    movies[2] : 175 , 
                    movies[3] : 250}

    def movies_display():
        print("Here are the movies available in our theatres !")
        for i in range (0 , len(movies)):
            print(f"{i+1}. {movies[i]}")
            time.sleep(0.5)


    class Viewer():
        def __init__(self,name,movie,movie_price,movie_theatre_num):
            self.name = name 
            self.movie = movie
            self.movie_price = movie_price
            self.movie_theatre_num = movie_theatre_num

    def movie_0():
            price_movie = movie_prices[movies[0]]
            print(f"Here is the price for your ticket : ₹{price_movie}")
            time.sleep(1)
            name_viewer = input("Please enter your name: ")
            

            viewer_money = int(input("Give the amount for the ticket : "))

            if viewer_money > price_movie:
                print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                viewer_money = viewer_money - price_movie
                time.sleep(1)

            elif viewer_money < price_movie:
                print("Insufficient amount!")
                print(f"You need to give ₹{price_movie - viewer_money} more to watch the movie!")
                choice = int(input("Your choice? \n(1.Watch  2.Leave) \n(1 / 2) > "))
                price_movie = price_movie - viewer_money
                if choice == 1:
                    more_money = int(input("Submit the remaining money properly : "))
                    if more_money == price_movie:
                        print("Thank you , now you can enjoy your movie : ")
                        time.sleep(1)

                    elif more_money > price_movie:
                        print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                        viewer_money = viewer_money - price_movie
                        time.sleep(1)
                    else:
                        print("You have been asked to leave the theatre because you are not submitting the money properly!")
                        time.sleep(1)
            elif viewer_money == price_movie:
                print("Thank you , now you can enjoy your movie : ")
                time.sleep(1)
            
            movie_theatre = "A1"

            viewer = Viewer(name_viewer , movies[0] , price_movie ,movie_theatre)
            print(f"Here is your ticket : \nName : {viewer.name} \nMovie : {viewer.movie} \nPrice : {viewer.movie_price} \nTheatre : {viewer.movie_theatre_num}")
            time.sleep(1)

            ticket_dict = {}
            
            ticket_dict["Name"] = viewer.name
            ticket_dict["Movie"] = viewer.movie
            ticket_dict["Ticket price"] = viewer.movie_price
            ticket_dict["Theatre"] = viewer.movie_theatre_num

            with open (f"{name_viewer}.json" , "w") as user_file:
                 json.dump(ticket_dict , user_file , indent=4)

    def movie_1():
            price_movie = movie_prices[movies[1]]
            print(f"Here is the price for your ticket : ₹{price_movie}")
            time.sleep(1)
            name_viewer = input("Please enter your name: ")

            viewer_money = int(input("Give the amount for the ticket : "))

            if viewer_money > price_movie:
                print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                viewer_money = viewer_money - price_movie
                time.sleep(1)

            elif viewer_money < price_movie:
                print("Insufficient amount!")
                print(f"You need to give ₹{price_movie - viewer_money} more to watch the movie!")
                choice = int(input("Your choice? \n(1.Watch  2.Leave) \n(1 / 2) > "))
                price_movie =price_movie - viewer_money
                time.sleep(1)
                if choice == 1:
                    more_money = int(input("Submit the remaining money properly : "))
                    if more_money == price_movie:
                        print("Thank you , now you can enjoy your movie : ")
                        time.sleep(1)

                    elif more_money > price_movie:
                        print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                        viewer_money = viewer_money - price_movie
                        time.sleep(1)

                    else:
                        print("You have been asked to leave the theatre because you are not submitting the money properly!")
                        time.sleep(1)
            
            elif viewer_money == price_movie:
                print("Thank you , now you can enjoy your movie : ")
                time.sleep(1)

            movie_theatre = "A2"

            viewer = Viewer(name_viewer , movies[1] , price_movie ,movie_theatre)
            print(f"Here is your ticket : \nName : {viewer.name} \nMovie : {viewer.movie} \nPrice : {viewer.movie_price} \nTheatre : {viewer.movie_theatre_num}")
            time.sleep(1)

            try:
                with open (f"{name_viewer}.json" , "r") as user_file:
                     ticket_dict = json.load(user_file)

            except FileNotFoundError :
                 with open (f"{name_viewer}.json" , "w") as user_file:
                      ticket_dict = {}
            
            ticket_dict["Name"] = viewer.name
            ticket_dict["Movie"] = viewer.movie
            ticket_dict["Ticket price"] = viewer.movie_price
            ticket_dict["Theatre"] = viewer.movie_theatre_num

            with open (f"{name_viewer}.json" , "w") as user_file:
                 json.dump(ticket_dict , user_file , indent=4)

    def movie_2():
            price_movie = movie_prices[movies[2]]
            print(f"Here is the price for your ticket : ₹{price_movie}")
            time.sleep(1)

            name_viewer = input("Please enter your name: ")
            viewer_money = int(input("Give the amount for the ticket : "))

            if viewer_money > price_movie:
                print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                viewer_money = viewer_money - price_movie
                time.sleep(1)

            elif viewer_money < price_movie:
                print("Insufficient amount!")
                print(f"You need to give ₹{price_movie - viewer_money} more to watch the movie!")
                choice = int(input("Your choice? \n(1.Watch  2.Leave) \n(1 / 2) > "))
                price_movie =price_movie - viewer_money
                if choice == 1:
                    more_money = int(input("Submit the remaining money properly : "))
                    if more_money == price_movie:
                        print("Thank you , now you can enjoy your movie : ")
                        time.sleep(1)

                    elif more_money > price_movie:
                        print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                        viewer_money = viewer_money - price_movie
                        time.sleep(1)

                    else:
                        print("You have been asked to leave the theatre because you are not submitting the money properly!")
                        time.sleep(1)
            elif viewer_money == price_movie:
                print("Thank you , now you can enjoy your movie : ")
                time.sleep(1)
            
            movie_theatre = "A3"

            viewer = Viewer(name_viewer , movies[2] , price_movie ,movie_theatre)
            print(f"Here is your ticket : \nName : {viewer.name} \nMovie : {viewer.movie} \nPrice : {viewer.movie_price} \nTheatre : {viewer.movie_theatre_num}")
            time.sleep(1)

            try:
                with open (f"{name_viewer}.json" , "r") as user_file:
                     ticket_dict = json.load(user_file)

            except FileNotFoundError :
                 with open (f"{name_viewer}.json" , "w") as user_file:
                      ticket_dict = {}
            
            ticket_dict["Name"] = viewer.name
            ticket_dict["Movie"] = viewer.movie
            ticket_dict["Ticket price"] = viewer.movie_price
            ticket_dict["Theatre"] = viewer.movie_theatre_num

            with open (f"{name_viewer}.json" , "w") as user_file:
                 json.dump(ticket_dict , user_file , indent=4)

    def movie_3():
            price_movie = movie_prices[movies[3]]
            print(f"Here is the price for your ticket : ₹{price_movie}")
            time.sleep(1)

            name_viewer = input("Please enter your name: ")
            viewer_money = int(input("Give the amount for the ticket : "))
            if viewer_money > price_movie:
                print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                viewer_money = viewer_money - price_movie
                time.sleep(1)

            elif viewer_money < price_movie:
                print("Insufficient amount!")
                print(f"You need to give ₹{price_movie - viewer_money} more to watch the movie!")
                choice = int(input("Your choice? \n(1.Watch  2.Leave) \n(1 / 2) > "))
                price_movie = price_movie - viewer_money
                if choice == 1:
                    more_money = int(input("Submit the remaining money properly you have only one chance : "))
                    if more_money == price_movie:
                        print("Thank you , now you can enjoy your movie : ")
                        time.sleep(1)

                    elif more_money > price_movie:
                        print(f"Here is your change : \nMoney given :- {viewer_money} \nMovie price : {price_movie} \nChange : {viewer_money - price_movie}")
                        viewer_money = viewer_money - price_movie
                        time.sleep(1)

                    else:
                        print("You have been asked to leave the theatre because you are not submitting the money properly!")
                        time.sleep(1)

                elif choice == 2:
                     print("Thank you for visiting the theatre !")

                else:
                     print("Error")

            elif viewer_money == price_movie:
                print("Thank you , now you can enjoy your movie : ")
                time.sleep(1)

            
            movie_theatre = "A4"

            viewer = Viewer(name_viewer , movies[3] , price_movie ,movie_theatre)
            print(f"Here is your ticket : \nName : {viewer.name} \nMovie : {viewer.movie} \nPrice : {viewer.movie_price} \nTheatre : {viewer.movie_theatre_num}")
            time.sleep(1)

            try:
                with open (f"{name_viewer}.json" , "r") as user_file:
                     ticket_dict = json.load(user_file)

            except FileNotFoundError :
                 with open (f"{name_viewer}.json" , "w") as user_file:
                      ticket_dict = {}
            
            ticket_dict["Name"] = viewer.name
            ticket_dict["Movie"] = viewer.movie
            ticket_dict["Ticket price"] = viewer.movie_price
            ticket_dict["Theatre"] = viewer.movie_theatre_num

            with open (f"{name_viewer}.json" , "w") as user_file:
                 json.dump(ticket_dict , user_file , indent=4)
            


    movies_display()
    print(f"Which movie do you want to watch? \n\nConfused ?\nHere is our reccommendation :-\n{random.choice(movies)}")

    print("\n\n[DEBUG]  NOTE : You can only buy one ticket for the name of one person if 2 or more tickets will be bought for the same name it will throw an error ")

    print("What do you want to do ? \n1. Buy a ticket \n2. Cancel your ticket")
    choice = int(input("(1 / 2)  > "))

    if choice == 1:
        movie_ = input("Enter the movie name you want to watch :- ")

        if movie_.lower() == movies[0].lower():
                movie_0()

        elif movie_.lower() == movies[1].lower():
                movie_1()

        elif movie_.lower() == movies[2].lower():
                movie_2()

        elif movie_.lower() == movies[3].lower():
                movie_3()

        else:
            print("Error")

    elif choice == 2:
        name = input("Enter your name so that we can check your ticket info : ") #asking the name from the user
        try:
            with open (f"{name}.json" , "r") as user_data: #in try except opening the file
                try :
                    data = json.load(user_data) #trying to load using json

                except json.JSONDecodeError:
                    print(f"We do not have any data for the viewer {name}!")
                    data = None  #if error

            if not data :
                    pass #checking if data is present or not using not(data)

            else:
                print("Found the viewer's ticket and removed it successfully")
                os.remove(f"{name}.json")
                print(f"Here is your money back after the cancellation : 100 (This is our own compenstation , the price is not calculated with respective to the price of movie)")
                        
        except FileNotFoundError:
                print(f"We do not have any data for the viewer {name}!")
                   
except Exception as e:
    print(e)
