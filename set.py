# set = collection which in unordered, unindexed. No duplicate values.
# sets are mutable like lists and unlike tuple

students = {"tauhid", "mehedi", "muaz", "mohsin"}
dishes = {"bowl","plate", "cup", "muaz"}

#-------> some useful method of set
# students.add("asad")
# students.remove("muaz")
# students.clear()

# --------> UPDATE METHOD:
# NOTE: modifies a set by adding elements from another set or iterable,
#       Change the original set.
# students.update(dishes)

# --------> UNION METHOD
# NOTE: Returns a new set with combined unique elements,
#       Does not modify original set.
student_dorm_kitchen = dishes.union(students)

# --------> COMMONS between sets
print(students.intersection(dishes))

# --------> UNCOMMON in targeted set
print(students.difference(dishes))

for x in student_dorm_kitchen:
    print(x)
