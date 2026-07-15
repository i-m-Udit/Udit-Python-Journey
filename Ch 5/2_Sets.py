# Sets are unordered, unindexed
#Items written in sets are immutable but we can any item in sets
# No repetition is allowed in sets 
#Sets are written using {}
# For example :
s={5,1,1,1,1,2,3,4}
#OUPUT: 5,1,2,3,4
s2={7,5,4,6,85,9}
# Operations on Sets:
# s.add(9) #Adds 9 in the set
print(len(s)) #Prints the length of set
s.remove(1) #Removes 1 from set
print(s.pop()) #Removes a random element from set and returns the value of that element
s.clear #Empties the set
s.union(s2) #Returns a new set with all the values of both sets
s.intersection(s2) #Returns a new set which contains the common values from both sets
