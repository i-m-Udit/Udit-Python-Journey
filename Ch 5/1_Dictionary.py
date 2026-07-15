# Dictionaries are written using {} 
# Dictionary is a set of key value pairs 
#For example {"key":"value"}
#Dictionaries are mutable,unordered,indexed
# Dictionaries value can be accessed using keys 
# Example 
d={"key":"value",
   "marks":99,
   "name":"Udit"}
print(d("marks")) #This will print 99 because 99 is the value of key (marks)

# Dictionary methods:
d.items() #Returns a list of key value pairs
d.keys()#Returns a list of only keys of a dictionary
d.update({"country":"India"}) #updates the dictionary and adds the given key value pair at last
d.get("name") #Gives the value of the key name