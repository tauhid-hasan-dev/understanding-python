# -----------> SOME OF THE IMPORTANT STRING METHODS <--------------

name = "Tauhid"

# ---> length of the string
print(len(name))

# ---> Find Method: we can find a index of a character in a string
print(name.find("T"))

# ---> Capitalize: convert word started with small letter to capital letter (only first letter)
first_name = 'mehedi'
print(first_name.capitalize())

# ---> Capital
last_name = 'hasan'
print(last_name.upper())

# ---> Smaller
capital_name = 'AHMAD'
print(capital_name.lower())

# ---> Is a number
age = '123'
print(age.isdigit())
# ---> Is an alphabet (value will be true or false)
print(age.isalpha())

# ---> We can count how many characters in a string
my_last_name = 'hasan'
print(my_last_name.count("a"))  # how many a in 'hasan'

# ---> We can replace a character with another in python
print(my_last_name.replace('a', 'o'))

# ---> We can print a string multiple time
print(name*3)




