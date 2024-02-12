# **kwargs = parameter that will pack all keyword arguments into a dictionary (object of key and value pairs)
#            useful so that a function can accept a varying amount of keyword(not positioned) arguments.
#            we can use any names instead of kwargs, but kwargs is convention
#            Asterisk (**) is very important

def hello(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Tauhid", middle="", last="Hasan")

