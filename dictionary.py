# dictionary : a changeable unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly
#              it is quite similar to set

capitals = {
    "Bangladesh": "Dhaka",
    "USA": "New Delhi",
    "India": "New Delhi",
    "Russia": "Mocow"
}

# if the key existed it will update the value of that key,
# if not it will add that key and value to the dictionary
capitals.update({"Germany": "Berlin"})
capitals.update({"Inddia": "Chennai"})

# to remove a key value pair (pop())
capitals.pop("Inddia")
capitals.clear()


# This method raises a KeyError if the key doesn't exist, stopping the program.
print(capitals["Bangladesh"])

#  The second method, .get(), returns None (or a specified default value) if the key is absent, avoiding an error.
#  Essentially, .get() is safer for accessing dictionary values when you're unsure if the key exists.
print(capitals.get('Bangladesh'))

# get only "keys" of from the dictionary
print(capitals.keys())

# get only "values"
print(capitals.values())

# get both "keys and values"
print(capitals.items())

# this will print both key and value
for key, value in capitals.items():
    print(key, value)




