def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature : "))

m = celsius_to_fahrenheit(c)
print(f"The temperature at fahreheit is : {round(m , 2)} °F")
