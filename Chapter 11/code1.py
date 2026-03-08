class Employee:
    company ="ITC"
    name = "XYZ"
    salary = 1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
        
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")  
         
#     def showLanguage(self):
#         print("The name is {self.name} and he is good with {self.language} language")
        
class Programmer(Employee):
    company ="ITC Infotech"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language} language")   
a = Employee()
a.show()
b = Programmer()
b.showLanguage()
print(a.company , b.company)