n=input("Enter:")
if ("  ") in n:
    print("The double spaces are replaced\nHere is the result:",end="")
    print(n.replace("  "," "))
else:
    print("There are no double spaces in the entered sentence")