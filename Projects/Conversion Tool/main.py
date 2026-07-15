print("---Conversion Tool---")
print('What do you want to convert?\n1.Length (cm to inches OR inches to cm)\n2.Weight (kg to lb OR lb to kg)\n3.Temperature (C to F)\n4.Currency (INR to USD , USD to INR , INR to YEN , YEN to INR , INR to Dhirams , Dhirams to INR , INR to EURO , EURO to INR)')
user=float(input("Enter the number of your choice:"))
if user==1:
    print("What do you want to convert?\n1.cm to inches\n2.inches to cm")
    conv1=float(input('Enter the number of your choice:'))
    if conv1==1:
        cm=float(input("Enter the length in cms:"))
        inch=(f"{cm}cm in inches is {cm/2.54}inches or {cm/30.48}feet")
        print(inch)
        print("The values have been successfully converted!")
    if conv1==2:
        inches=float(input("Enter the length in inches:"))
        cms=(f"{inches}inch in cm is {inches*2.54}inches")
        print(cms)
        print("The values have been successfully converted!")
if user==2:
    print("What do you want to convert?\n1.kg to lb\n2.lb to kg")
    conv2=float(input('Enter the number of your choice:'))
    if conv2==1:
        kg=float(input("Enter the weight in kgs:"))
        lb=(f"{kg}kgs in lbs are {kg*2.20462}lbs")
        print(lb)
        print("The values have been successfully converted!")
    if conv2==2:
        lbs=float(input("Enter the weight in lbs:"))
        kgs=(f"{lbs}lbs in kgs are {lbs/2.20462}kgs")
        print(kgs)
        print("The values have been successfully converted!")
if user==3:
    print("What do you want to convert?\n1.C to F\n2.F to C")
    conv3=float(input("Enter the number of your choice:"))
    if conv3==1:
        cel=float(input("Enter the emperature in celcius:"))
        print(f"The temperature in °F is {(cel*(9/5))+32} °")
        print("The values have been successfully converted!")
    if conv3==2:
        fah=float(input("Enter he temperature in fahrenheits:"))
        print(f"The tempertaure in celcius is {(fah - 32) * 5 / 9}")
        print("The values have been successfully converted!")
if user==4:
    print("What do you want to do?")
    print("1.INR to USD\n2.USD to INR\n3.INR to YEN\n4.YEN to INR\n5.INR to UAE Dhirams\n6.UAE Dhirams to INR\n7.INR to EURO\n8.EURO to INR")
    conv4=float(input("Enter the number of you choice:"))
    if conv4==1:
        inr=float(input('Enter the amount in INR:'))
        print(f"{inr}Rs. in USD is {inr/83}$")
    if conv4==2:
        usd=float(input("Enter the amount in USD:"))
        print(f"{usd}$ in INR is {usd*83}Rs")
    if conv4==3:
        inr=float(input('Enter the amount in INR:'))
        print(f"{inr}Rs in YEN is {inr*1.65}Yen")
    if conv4==4:
        yen=float(input("Enter he amount in YEN:"))
        print(f"{yen}Yen in INR is {yen*0.606}Rs")
    if conv4==5:
        inr=float(input('Enter the amount in INR:'))
        print(f"{inr}Rs in UAE Dhirams is {inr*0.044}Dhirams")
    if conv4==6:
        Dhirams=float(input("Enter the amount in Dhirams:"))
        print(f"{Dhirams}UAE Dhirams in INR is {Dhirams*22.73}Rs")
    if conv4==7:
         inr=float(input('Enter the amount in INR:'))
         print(f"{inr}Rs in EURO is {inr*0.011}EURO")
    if conv4==8:
        Euor=(float(input("Enter the amount in EURO:")))
        print(f"{Euor}EURO in INR is {Euor*90.91}Rs")