def hello():
    a = 5  # local variable -> shadows a global variable with the same name
    b = 6
    c = 7
    print('Hello')
    print(locals())  # to understand what all the local variables are
    print(globals())


hello()
a = 10
print('global variable = ', a)
print(locals())
print(globals())
