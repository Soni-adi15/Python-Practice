# f = open("poems.txt")
# c = f.read()
# if "twinkle" in c:
#     print("The word twinkle is present in the poem")
    
# else:
#     print("The word twinkle is not present in the poem")
    
# f.close()

with open("poems.txt" , "r") as f:
    c = f.read()
    if("twinkle" in c):
        print("Yes , the word twinkle is present in poem")
        
    else:
        print("No , the word twinkle is not present in poem") 