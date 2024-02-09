# index operator [] = gives access to a sequence's element (str, list, tuples)
# that means we can modify any element of "STRING, LIST AND TUPLES"

name = "tauhid Hasan!"

if name[0].islower():
    name = name.capitalize()

first_name = name[:6].upper()
last_name = name[7:].lower()
last_character = name[-1]
second_last_character = name[-2]

print(first_name)
print(last_name)
print(last_character)
print(second_last_character)



