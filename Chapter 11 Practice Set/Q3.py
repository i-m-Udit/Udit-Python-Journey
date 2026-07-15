class Employee:
    def __init__(self,salary):
        self._salary=salary
        self._increment=0
    @property
    def SalaryAfterIncrement(self):
        return self._salary + self._increment
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,info):
        salary=info
        if salary<100000:
                    increment=1000
        elif salary<200000:
                    increment=2000
        elif salary<300000:
                    increment=3000
        elif salary<400000:
                    increment=4000
        elif salary<500000:
                    increment=5000
        else:
            increment=7000
        newSalary=salary+increment
        self._salary=salary
        self._increment=increment
        print(f"The salary after increment is {newSalary}")
salary=int(input("Enter your salary:"))
Rohit=Employee(salary)
Rohit.SalaryAfterIncrement=(salary)