# list = used to store multiple items in a single variable

food = ["pizza", "doner", 'adana', 'urfa']
# food[1] = "pilav"


# few useful functions of list
# food.append("ice cream")  # add item to the list
# food.remove("urfa")  # remove any item
# food.pop()  # remove last item
# food.insert(0, "sdf")  # it does not delete the item at the index, it add a item in that index
# food.sort()  # It actually sorts in alphabetical order.

# ---> to see all the food item we can iterate and see the each item
for x in food:
    print(x)
