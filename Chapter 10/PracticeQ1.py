class Car:
    Company=input('Enter your car brand:')
    Model=input('Enter your car model:')
    def Car_GetInfo(self):
        print(f"Your car brand is {self.Company} and your car model is {self.Model}")
Udit=Car()
Udit.Car_GetInfo()
