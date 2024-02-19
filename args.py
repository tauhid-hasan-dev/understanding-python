# *args = parameter that will pack all "positioned" arguments into a "tuple"
#         useful so that a function can accept a varying amount of positioned arguments.

# asterisk (*) is very important (convert the args to tuple)
# we can not change the element of tuple, so we need to type cast

def add(*args):
    sum = 0
    args = list(args)  # type casting to list type--> because list is mutable
    args[1] = 50
    for i in args:
        sum += i
    return sum

print(add(1,3,5,6))


