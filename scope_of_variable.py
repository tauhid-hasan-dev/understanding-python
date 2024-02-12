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
x = "This is global scope"


def my_function():
    # Enclosing scope
    y = "This is enclosing scope"
    print(y)
    def inner_function():
        # Local scope
        z = "This is local scope"

        print(z)

        # Using the len() built-in function
        my_list = [1, 2, 3, 4, 5]
        print("Built in function, Length of my_list:", len(my_list))

    inner_function()


print("Outside any function:")
print("x (global):", x)
my_function()


