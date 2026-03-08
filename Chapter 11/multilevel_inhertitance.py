class Employee():
    a = 3
    
class Programmer(Employee):
    b = 2
    
class Manager(Programmer):
    c = 4
    
o = Employee()
print(o.a)      # Prints the a attribute
# print(o.b)

o = Programmer()
print(o.a , o.b)

o = Manager()
print(o.a , o.b , o.c)
