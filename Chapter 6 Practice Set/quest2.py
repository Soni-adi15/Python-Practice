a1 = int(input("Enter marks : "))
a2 = int(input("Enter marks : "))
a3 = int(input("Enter marks : "))

total_percentage = (100 * (a1 + a2 + a3) / 300)

if(total_percentage >= 40 and a1 >= 33 and a2 >= 33 and a3 >= 33):
    print("You are passed", total_percentage)
    
else:
    print("You failed to score 40 percentage of marks in all the subjects", total_percentage)

