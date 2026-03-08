def add_numbers(a , b):
    return a + b

def subtract_numbers(a , b):
    return a - b

def multiply_numbers(a , b):
    return a * b

def divide_numbers(a , b):
    if(b == 0):
        return "Error : Division by zero is not possible"
    return a / b
    
def square_numbers(a):
    return a * a


while True:
    print("\n____ Basic calculator____\n")
    print("Operations Menu\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Exit")
    
    choice = int(input("Enter you choice : "))
    
    if(choice == 6):
        print("Thank you for using my calculator..")
        break
    
    if choice in [1 , 2 , 3 , 4]:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
    
        if (choice == 1):
            print(f"Addition of the numbers is : {add_numbers(a , b)}")
       
        elif (choice == 2):
            print(f"Subtraction of the numbers is : {subtract_numbers(a , b)}")
            
        elif (choice == 3):
            print(f"Multiplication of the numbers is : {multiply_numbers(a , b)}")
            
        elif (choice == 4):
            print(f"Division of the numbers is : {divide_numbers(a , b):.2f}")
    
    elif (choice == 5):
        a = float(input("Enter the number : "))
        print(f"Square of the number is : {square_numbers(a)}")
        
    else:
        print("Invalid choice") 
    
            
    
    

