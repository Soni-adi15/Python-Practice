# factorial(n) = n x n-1 x ........ 3 2 1

# factorial(n) = n * factorial(n-1)

def fact(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact(n - 1)

n = int(input("Enter any number : "))
print(f"The factorial of the number {n} is {fact(n)}")
