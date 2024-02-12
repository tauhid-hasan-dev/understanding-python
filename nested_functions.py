# nested function calls = function calls inside other function calls
#                         innermost functions calls are resolved first
#                         return value is used as argument for the next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# We can do same thing with nested functions
print(round(abs(float(input("Enter a whole positive number: ")))))
