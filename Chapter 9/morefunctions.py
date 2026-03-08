f = open("file1.txt")

# lines = f.readlines()
# print(lines , type(lines))

# line1 = f.readline()
# print(line1 , type(line1))

# line2 = f.readline()
# print(line2 , type(line2))

# line3 = f.readline()
# print(line3 == "")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

with open("file1.txt") as f:
    for line in f:
        print(line , end = "")