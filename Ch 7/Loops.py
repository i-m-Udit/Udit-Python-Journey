# 2 types of loops are 1. While loop 2. For loop
#While loop keeps repeating the program until it is true
#It wil stop when the condition is false
#Quick Quiz:
# i=1
# while (i<=50):
#     print(i*1)
#     i+=1
#If the condition never becomes false the loop will never stop
i=0
l=["Hello","Udit","Rohit","Kohli","Rohan"]
while (i<=(len(l))):
    print(l[i-1])
    i+=1
#Important Program:
l=[1,2,3]
for item in l:
    print(item)
else:
    print("Done")
# Range funtion is used in for loops for printing integers 
for i in range(1,7):
    print(i) #It is the same as index slicing which means it will count till the last value given excluding the last value given
