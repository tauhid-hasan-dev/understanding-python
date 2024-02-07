# Slicing: create a substring by extracting elements from another string
# There are two ways to slice: indexing[] or slice()

# indexing[] --> [start: stop : step]

name = "Tauhid Hasan"

first_name = name[:6]       # [start:6]
last_name = name[7:]        # [7:end]
funky_name = name[::2]      # [start:end:2] (it will start o index and step up by 2)
reversed_name = name[::-1]  # [start:end:-1]


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


# slice(start, end)

website1 = "https://google.com"
website2 = "https://wikipedia.com"


slice = slice(8, -4)

print(website1[slice])




print(website2[slice])
