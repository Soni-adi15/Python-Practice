class Employee:
    language = "Py"   # This is class attribute
    salary = "1500000"
    
harry = Employee()
harry.name = "Soni"    #This is object/instance attribute
print(harry.salary , harry.language , harry.name)

rohan = Employee()
rohan.name = "Rishab Rohan"
print(rohan.language , rohan.salary , rohan.name)


# Here name is object attribute and salary and language 
# are object attribute as they directly belong to the class



















