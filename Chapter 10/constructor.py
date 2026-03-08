class Employee:
    language = "Python"   # This is class attribute
    salary = "1500000"
    
    def __init__(self , name , salary , language):   #dunder method gets automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an object")
        
    # def getInfo(self):
    #     print(f"The language is {self.language}. The salary is {self.salary}")
        
    # @staticmethod
    # def greet():     # function which will not take self 
    #     print("Good morning")
        
harry = Employee("Soni" , 1300000 , "Javascripts")
# harry.name = "Soni"
print(harry.name , harry.salary , harry.language)

# rohan = Employee()