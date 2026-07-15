def Generate_Tables(n): #Making a function to generate tables
    table="" #Giving that there are no tables
    for i in range(1,11): #Running a loop from 1 to 10
        table +=f"{n} X {i} = {n*i}" #Adding the tables to n
    
    with open(f"Tables/Table_{n}.txt","w") as f: #Making a new file in the folder named"Tables"
        f.write(table) #Writing the table 
for n in range (2,21): #N is considered as a loop from 2 to 20
    Generate_Tables(n) #Running the function
print("Your tables have been successfully generated")