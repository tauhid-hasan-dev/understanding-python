# str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + "jumped over the " + item)

# ---> we can write this in a better way using python.

print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  # positional arguments
print("The {animal} jumped over the {item}".format(animal="Horse", item="bridge"))  # keyword arguments
# we can use the keyword multiple time
print("The {animal} jumped over the {animal}".format(animal="Horse", item="bridge"))
# we can reuse the same index for positional arguments
print("The {1} jumped over the {1}".format(animal, item))

# we can do by declaring the variable
text = "The {0} jumped over the {1}"
print(text.format(animal, item))


# Padding in string
name = "Tauhid"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}.Nice to meet you".format(name))
print("Hello, my name is {:>10}.Nice to meet you.(right align)".format(name))  # left align
print("Hello, my name is {:<10}.Nice to meet you.(left align)".format(name))  # right align
print("Hello, my name is {:^10}.Nice to meet you.(middle align)".format(name))  # middle align

# for example I want to show only the two digits of a number

number = 3.14159
thousand = 100

print("The number pi is {:.2f}".format(number))  # f is for floating point number
print("The number pi is {:,}".format(thousand))  # we can apply commas for a huge number with format method
print("The binary of {0} is {1:b}".format(thousand, thousand))  # binary
print("The binary of {0} is {1:o}".format(thousand, thousand))  # octal
print("The binary of {0} is {1:x}".format(thousand, thousand))  # hexadecimal
print("The binary of {0} is {1:E}".format(thousand, thousand))  # scientific notation











