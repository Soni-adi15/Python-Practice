a = 15  # here it is global variable
def fun():
    global a  
    a = 3
    
    print(a)
    

fun()
print(a)
