marks = {
    "Garry" : 80,
    "Soni" : 100,
    "Rohan" : 55,
}

# print(marks, type(marks))

# print(marks ["Garry"])

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Garry" : 99 , "Menka" : 70})

print(marks)

print(marks.get("Garry"))  # prints none

print(marks["Garry"])      # prints error  due to presence of square brackets




