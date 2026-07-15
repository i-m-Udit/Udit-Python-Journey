l1 = []
def tables(n):
    for i in range (1,11):
        l1.append(n*i)
    print (l1)
tables(7)
print('\n'.join(str(item)) for item in l1)