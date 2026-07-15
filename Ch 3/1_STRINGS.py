# Strings can be written in '' , "" , """ """ 
# String is a data type in python 

# String slicing can be done as 
# U  D  I  T 
# 0  1  2  3 This is the positive slicing
# -4 -3 -2 -1 This is the negative slicing]
# In index slicing [] brackets are used 
# for example 
x="Udit"
sl=x[0:3] #In this the slicing is starting from value 0 to 3 excluding 3
print(sl)

# String functions :
len(x) #prints the length of a string

x.endswith("it") #Searches whether a string ends with it or not BOOLEAN

x.count("i") #Counts how many times a character occurs

x.capitalize() #Capatalizes the first character of a string

x.find("i") #Finds a specific word and return its first occurance index number

x.replace("t","") #Replaces the given character with the next given character in whole string
