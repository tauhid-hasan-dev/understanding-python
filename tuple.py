# tuple = collection which is ordered and unchangeable used to group together related data
# tuples are immutable, their contents cannot be altered after creation,
# which means you cannot add, remove, or change elements in a tuple once it is created.
# They are faster than lists due to their immutability,
# making them slightly more performance efficient for fixed data sets.

student = ("Tauhid", 28, "male")

print(student.count("Tauhid"))
print(student.index("male"))

for x in student:
    print(x)
if 22 in student:
    print('there is 28 in student')
else:
    print("Not found")

# A real life Example

# Defining a few locations as tuples (latitude, longitude)
headquarters = (40.712776, -74.005974)  # New York, NY
warehouse = (34.052235, -118.243683)    # Los Angeles, CA
customer_location = (41.878113, -87.629799)  # Chicago, IL

# Function to calculate distance between two locations (simplified example)
def calculate_distance(location1, location2):
    # This function would contain the logic to calculate distance between two GPS points
    # For demonstration purposes, let's just pretend it calculates and returns a distance
    return 123.45  # Placeholder value for distance

# Calculating distance from warehouse to customer location
distance_to_customer = calculate_distance(warehouse, customer_location)

print(f"Distance from warehouse to customer location: {distance_to_customer} miles")

