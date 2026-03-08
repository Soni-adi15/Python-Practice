class Programmer:
    company = "Microsoft"    # Class attribute
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
     
        
p = Programmer("Adi" , 1500000)
print(p.name , p.company , p.salary)

r = Programmer("Rahul" , 1500000)
print(r.name , r.company , r.salary)

