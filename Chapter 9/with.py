f = open("file1.txt")

# print(f.read())
# f.close()

# The same can be written using with statement

with open("file1.txt") as f:
    print(f.read())
    
# we needn't have to use f.close() here
