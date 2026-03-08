a = int(input("Enter your age : "))

# if elif ladder

if(a > 18):
    print("You are above the consent age.")
    print("Good enough")
    
elif(a < 0):
    print("You are entering an invalid age.")

elif(a == 0):
    print("You are entering 0.")
    
    
else:
    print("You are below the age of consent.")
    
print("End od program.")

