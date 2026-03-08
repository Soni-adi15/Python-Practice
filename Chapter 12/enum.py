list = [1 , 3 , 5 , 7]

# index = 0
# for item in list :
#     print(f"The item number at index {index} is {item}")
#     index += 1
    
# This can be simplified using enumerate function

for index , item in enumerate(list):
    print(f"The item number at index {index} is {item}")
    