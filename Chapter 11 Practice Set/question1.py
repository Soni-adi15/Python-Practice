class twoDvector():
    def __init__(self , i , j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
        
        
class threeDvector(twoDvector):
    def __init__(self , i , j , k):
        super().__init__(i , j)
        self.k = k
         
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
         
a = twoDvector(1 , 5)
b = threeDvector(2 , 4 , 6)

a.show()
b.show()
