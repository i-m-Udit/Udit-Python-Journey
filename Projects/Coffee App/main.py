# coffee app

import json

dict_sandwich_name = {1 : "Grilled Sandwiches" , 2 : "Grilled Cheese Sandwiches" , 3 : "Veg Sandwiches" , 4 : "Veg cheese sandwiches" }

dict_sandwich_price = {"Grilled Sandwiches" : 100 , "Grilled Cheese Sandwiches" : 150 , "Veg Sandwiches" : 50 , "Veg cheese sandwiches" : 100 }

# Pastries
dict_pastries_name = {
    1: "Chocolate Pastry",
    2: "Strawberry Pastry",
    3: "Vanilla Pastry",
    4: "Red Velvet Pastry"
}

dict_pastries_price = {
    "Chocolate Pastry": 120,
    "Strawberry Pastry": 100,
    "Vanilla Pastry": 90,
    "Red Velvet Pastry": 150
}

# Croissant
dict_croissant_name = {
    1: "Butter Croissant",
    2: "Chocolate Croissant",
    3: "Cheese Croissant"
}

dict_croissant_price = {
    "Butter Croissant": 80,
    "Chocolate Croissant": 110,
    "Cheese Croissant": 120
}

# Pizzas
dict_pizza_name = {
    1: "Margherita Pizza",
    2: "Veggie Pizza",
    3: "Cheese Burst Pizza",
    4: "Pepperoni Pizza"
}

dict_pizza_price = {
    "Margherita Pizza": 200,
    "Veggie Pizza": 250,
    "Cheese Burst Pizza": 300,
    "Pepperoni Pizza": 350
}

# Burgers
dict_burger_name = {
    1: "Veggie Burger",
    2: "Cheese Burger",
    3: "Double Patty Burger",
    4: "Chicken Burger"
}

dict_burger_price = {
    "Veggie Burger": 120,
    "Cheese Burger": 150,
    "Double Patty Burger": 200,
    "Chicken Burger": 220
}


order = []
order_amount= []
class Customer:
    def __init__(self,name,order,order_amount):
        self.name = name
        self.ordero = order
        self.order_amounta = order_amount

def welcome():
    print("Here is our menu : ")
    print("1. BEVERAGES \n2. FOOD \n3.Some surprise items!")
    print("What would you like to have ?")

def order1():
    try:
        choice = int(input("Please enter your choice (1 / 2 / 3) : "))

        if choice==2:
            print("Here is our menu of the food items :")
            print("1. Sandwiches\n2. Pastries \n3. Crossoiant \n4. Pizzas \n5. Burgers")
            choice2 = int(input("Please enter your choice (1 / 2 / 3 / 4 / 5) : ")) 

            if choice2==1:
                print("1. Grilled Sandwiches (₹ 100)\n2. Grilled Cheese Sandwiches (₹ 150)\n3. Veg Sandwiches (₹ 50)\n4. Veg cheese sandwiches (₹ 100)")
                choice3 = int(input("Please enter your choice (1 / 2 / 3 / 4) :")) 

                if choice3 > 4:
                    print("Please enter again !!")
                    choice2 = int(input("Please enter your choice (1 / 2 / 3 / 4 ) :")) 

                else : 
                    order_item1 = dict_sandwich_name[choice3]
                    order_price1 = dict_sandwich_price[order_item1]

                    order.append(order_item1)
                    order_amount.append(order_price1)

                    print(f"{order_item1} of price {order_price1} added to your order !")

                    

            elif choice2 == 3:
                print("1. Butter Croissant (₹ 80)\n2. Chocolate Croissant (₹ 110)\n3. Cheese Croissant (₹ 120)")
                choicec = int(input("Please enter your choice (1 / 2 / 3 ) :")) 

                if choicec > 4:
                    print("Please enter again !!")
                    choicec = int(input("Please enter your choice (1 / 2 / 3 ) :")) 

                else :
                    order_item2 = dict_croissant_name[choicec]
                    order_price2 = dict_croissant_price[order_item2]

                    order.append(order_item2)
                    order_amount.append(order_price2)

                    print(f"{order_item2} of price {order_price2} added to your order !")

            elif choice2 == 2:
                print("1. Chocolate Pastry (₹ 120)\n2. Strawberry Pastry (₹ 100)\n3. Vanilla Pastry (₹ 90)\n4. Red Velvet Pastry (₹ 150)")
                choicep = int(input("Please enter your choice (1 / 2 / 3 / 4) :")) 

                if choicep > 4:
                    print("Please enter again !!")
                    choicep = int(input("Please enter your choice (1 / 2 / 3 / 4 ) :")) 

                else :
                    order_item3 = dict_pastries_name[choicep]
                    order_price3 = dict_pastries_price[order_item3]

                    order.append(order_item3)
                    order_amount.append(order_price3)

                    print(f"{order_item3} of price {order_price3} added to your order !")

            elif choice2 == 4:
                print("1. Margherita Pizza (₹ 200)\n2. Veggie Pizza (₹ 250)\n3. Cheese Burst Pizza (₹ 300)\n4. Pepperoni Pizza (₹ 350)")
                choicepi = int(input("Please enter your choice (1 / 2 / 3 / 4) :")) 

                if choicepi > 4:
                    print("Please enter again !!")
                    choicepi = int(input("Please enter your choice (1 / 2 / 3 / 4 ) :")) 

                else :
                    order_item4 = dict_pizza_name[choicepi]
                    order_price4 = dict_pizza_price[order_item4]

                    order.append(order_item4)
                    order_amount.append(order_price4)

                    print(f"{order_item4} of price {order_price4} added to your order !")

            elif choice2 == 5:
                print("1. Veggie Burger (₹ 120)\n2. Cheese Burger (₹ 150)\n3. Double Patty Burger (₹ 200)\n4. Chicken Burger (₹ 220)")
                choiceb = int(input("Please enter your choice (1 / 2 / 3 / 4) :")) 

                if choiceb > 4:
                    print("Please enter again !!")
                    choiceb = int(input("Please enter your choice (1 / 2 / 3 / 4 ) :")) 

                else :
                    order_item5 = dict_burger_name[choiceb]
                    order_price5 = dict_burger_price[order_item5]

                    order.append(order_item5)
                    order_amount.append(order_price5)

                    print(f"{order_item5} of price {order_price5} added to your order !") 

        elif choice == 1:  # Beverages
            print("Here is our Beverages menu :")
            print("1. Cappuccino (₹ 120)\n2. Latte (₹ 150)\n3. Espresso (₹ 100)\n4. Cold Coffee (₹ 130)")
            choice_bev = int(input("Please enter your choice (1 / 2 / 3 / 4) : "))

            if choice_bev > 4:
                print("Please enter again !!")
                choice_bev = int(input("Please enter your choice (1 / 2 / 3 / 4) :"))
            else:
                beverages_name = {
                    1: "Cappuccino",
                    2: "Latte",
                    3: "Espresso",
                    4: "Cold Coffee"
                }
                beverages_price = {
                    "Cappuccino": 120,
                    "Latte": 150,
                    "Espresso": 100,
                    "Cold Coffee": 130
                }
                order_item_bev = beverages_name[choice_bev]
                order_price_bev = beverages_price[order_item_bev]

                order.append(order_item_bev)
                order_amount.append(order_price_bev)

                print(f"{order_item_bev} of price {order_price_bev} added to your order !")


        elif choice == 3:  # Surprise items
            print("Surprise Items Menu :")
            print("1. Brainrot Special Pizza (₹ 420)\n2. NPC Smoothie (₹ 210)\n3. Sigma Sandwich (₹ 180)\n4. Rizzler Pastry (₹ 250)")
            choice_sur = int(input("Please enter your choice (1 / 2 / 3 / 4) : "))

            if choice_sur > 4:
                print("Please enter again !!")
                choice_sur = int(input("Please enter your choice (1 / 2 / 3 / 4) :"))
            else:
                surprise_name = {
                    1: "Brainrot Special Pizza",
                    2: "NPC Smoothie",
                    3: "Sigma Sandwich",
                    4: "Rizzler Pastry"
                }
                surprise_price = {
                    "Brainrot Special Pizza": 420,
                    "NPC Smoothie": 210,
                    "Sigma Sandwich": 180,
                    "Rizzler Pastry": 250
                }
                order_item_sur = surprise_name[choice_sur]
                order_price_sur = surprise_price[order_item_sur]

                order.append(order_item_sur)
                order_amount.append(order_price_sur)

                print(f"{order_item_sur} of price {order_price_sur} added to your order !")



    except ValueError:
        print("Please enter correct values (1 / 2 / 3 ..etc)")
    


print("----------------------------------------------\nWelcome to the BrainRot coffee shop\n----------------------------------------------")
name_of = input("Please enter your name: ")
while True:
    welcome()
    order1()
    stop = input("Type STOP if you want to stop your order else press ENTER: ")  
    if stop.lower() == "stop": 
            print("Here is your reciept :")
            customer = Customer(name_of , order , order_amount )   
            print(f"Name : {customer.name}") 
            print("Your order is :")         
            for o in customer.ordero:
                    print(o)
            print(f"The amount to be paid is {sum(customer.order_amounta)}")
            with open(f"{customer.name}.json" , "w") as info:
                data = {
                        "Name": customer.name,
                        "Order": customer.ordero,
                        "Amount paid": sum(customer.order_amounta) }
                json.dump(data, info, indent=4)
            break
    
            
    else :
        continue
