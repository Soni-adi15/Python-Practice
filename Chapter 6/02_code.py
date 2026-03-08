a = int(input("Enter your age : "))

# if elif ladder

# if statement number 1

if( a % 2 == 0):            """ independent if statement 
    print("a is even")       no need of else statement  """

# end of if statement 2

# if statement 2
if(a >= 18):
    print("You are above the consent age.")
    print("Good enough")
    
elif(a < 0):
    print("You are entering an invalid age.")

elif(a == 0):
    print("You are entering 0.")
    
    
else:
    print("You are below the age of consent.")
 
# end os if statement 2
    
print("End of program.")

