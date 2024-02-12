# scope = The region that a variable is recognized
#         A variable in only available from inside the region it is created
#         A global and locally scoped versions of variable can be created.

# The LEGB rule in Python dictates the order in which the language searches for
# variable names in different scopes:

# L: Local scope
# E: Enclosing scope
# G: Global scope
# B: Built-in scope

# Global scope
x = 10


def my_function():
    # Enclosing scope
    y = 20

    def inner_function():
        # Local scope
        z = 30
        # Using a built-in function
        print("Inside inner_function:")
        print("z (local):", z)
        print("y (enclosing):", y)
        print("x (global):", x)
        # Using the len() built-in function
        my_list = [1, 2, 3, 4, 5]
        print("Length of my_list:", len(my_list))

    inner_function()

my_function()
print("Outside any function:")
print("x (global):", x)




