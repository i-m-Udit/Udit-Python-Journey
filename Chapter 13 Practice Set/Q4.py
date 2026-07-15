l1=[1,2,3,4,5,10]
def finding(n):
    if n%5==0:
        return True
    return False
new = filter(finding,l1)
print(list(new))