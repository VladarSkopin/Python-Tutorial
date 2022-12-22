x = "global"


def foo():
    x = x * 2  # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    print(x)


foo()

