try:
    with open ("file1.txt") as file:
        pass
except FileNotFoundError:
    print("File 1 is not present")
try:
    with open ("file2.txt") as file:
        pass
except FileNotFoundError:
    print("File 2 is not present")
try:
    with open ("file3.txt") as file:
        pass
except FileNotFoundError:
    print("File 3 is not present")