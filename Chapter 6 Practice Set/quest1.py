a = int(input("Enter marks : "))
b = int(input("Enter marks : "))
c = int(input("Enter marks : "))
d = int(input("Enter marks : "))

if(a > b and a > c and a > d):
        print(a, "is greater")

elif(b > a and b > c and b > d):
        print(b, "is greater")

elif(c > b and c > a and c > d):
        print(c, "is greater")

elif(d > b and d > c and d > a):
        print(d, "is greater")

