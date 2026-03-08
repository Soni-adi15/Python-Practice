n = int(input("Enter a number : "))

for i in range(2 , n):
    if(n % i == 0):
        print("Not a prime nummber.")
        break
else:
    print("number is prime.") 
     
