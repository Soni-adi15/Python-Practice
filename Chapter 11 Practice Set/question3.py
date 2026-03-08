class Employee():
    salary = 25000
    increment = 10

    @property
    def salaryAfterincrement(self):
        return (self.salary + self.salary * (self.increment/100)) 

    @salaryAfterincrement.setter
    def salaryAfterincrement(self , salary):
        self.increment = ((salary / self.salary) - 1) * 100
        
        
    
e = Employee()
# print(e.salaryAfterincrement)
e.salaryAfterincrement = 27500
print(e.increment)