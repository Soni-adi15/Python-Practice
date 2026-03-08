class Employee:
    language = "Python"   # This is class attribute
    salary = "1500000"
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():     # function which will not take self 
        print("Good morning")
        
Soni = Employee()
Soni.language = "javascript"  # This is object/instance attribute
Soni.salary = 1200000 
# Soni.getInfo()
Soni.greet()
Employee.getInfo(Soni)
