# Prints positional arguments


def f(*args, **kwargs):
    print("Positional:", args)


f(100, 50, 25)
f(100, 50, 25, 1)
f(100) # trailing comma is tuple syntax
