# 4) FUNCTION CAN RECEIVE ANOTHER FUNCTION AS A PARAMETER !

def print_func():
    print("I am just printing")


def example_function(func):
    print("Print before func")
    func()
    print("Print after func")


example_function(print_func)
