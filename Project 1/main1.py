import random


'''

1 for rock
-1 for scissor
0 for paper

'''

computer = random.choice([-1 , 1 , 0])
youstr = input("Enter your choice between s , p and r : ")
youDict = {"s" : -1 , "p" : 0 , "r" : 1}
reverseDict = {1 : "Rock" , -1 : "Scissor" , 0 : "Paper"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("draw")

else:
    if(computer == -1 and you == 1):
        print("You win!") 

    elif(computer == -1 and you == 0):
        print("you lose!")
        
    elif(computer == 1 and you == -1):
        print("you lose!")
        
    elif(computer == 1 and you == 0):
        print("you win!")
        
    elif(computer == 0 and you == -1):
        print("you win!")
        
    elif(computer == 0 and you == 1):
        print("you lose!")
        
    else:
        print("Semthing went wrong!")


