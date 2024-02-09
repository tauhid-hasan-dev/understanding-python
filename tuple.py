# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Tauhid", 28, "male")

print(student.count("Tauhid"))
print(student.index("male"))

for x in student:
    print(x)

if 22 in student:
    print('there is 28 in student')
else:
    print("Not found")
