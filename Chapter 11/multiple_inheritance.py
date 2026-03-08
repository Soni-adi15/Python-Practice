class Employee:
    company ="ITC"
    name = "Soni"
    salary = 1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
        
class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all languages here is your language : {self.language}")
        
class Programmer(Employee , Coder):
    company ="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and the language is {self.language} language")   

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()

print(a.company , b.company)
