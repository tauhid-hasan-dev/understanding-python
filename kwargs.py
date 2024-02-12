# **kwargs = parameter that will pack all keyword arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword(not positioned) arguments.

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first="Tauhid", middle="", last="Hasan")

