# logical operator (and , or, not ) = used to check if two or more logical statement is true
# not operator works like "!" in javascript.

temp = int(input("What is the temperature outside?: "))

if not (temp >= 0 and temp <= 30):
    print("The weather is not good today")
    print("do not go outside today")
elif not (temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside")


