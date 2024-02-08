# while loop = a statement that will execute its block of code,
#              as long as its condition remains true

name = ""
while len(name) == 0:
    name = input("Enter your name: ")

# we can write same thing in a different way
# In Python, empty strings, None, and False are considered as "falsy" values
# while loop that will continue executing until the fullname variable is not empty or None

fullname = None
while not fullname:
    fullname = input("Enter your full name ")

print("The full name is " + fullname)
print("The name is " + name)

