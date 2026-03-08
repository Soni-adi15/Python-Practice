from functools import reduce

a = [111 , 25 , 58 , 75 , 888 , 9999]

def greater(a , b):
    if(a > b):
        return a
    return b

print(reduce(greater , a))
