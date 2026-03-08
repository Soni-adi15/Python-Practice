class Employee:
    language = "Py"   # This is class attribute
    salary = "1500000"
    
harry = Employee()
harry.language = "javascript"    #This is object/instance attribute
print(harry.salary , harry.language)

