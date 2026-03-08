# filter

def divisible5(n):
    if (n % 5 == 0):
        return True
    return False

a = [1 , 20 , 56 , 75 , 88 , 25]

f = list(filter(divisible5 , a))
print(f)
