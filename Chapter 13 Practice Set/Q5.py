from functools import reduce
l1 = [1,2,3,4,5,6,7,8,9,0]
def finding_greatest(a,b):
    if a>b:
        return a
    return b
s= reduce(finding_greatest,l1)
print(f"The greatest number from the given list is {s}")