def func_a(*args):  # * -> many arguments
    return args


def func_b(**kwargs):  # ** -> dictionary type arguments
    return kwargs


def solve_math_equation(a, operation, b):
    operation = operation.strip()
    if operation == '-':
        print(a - b)
    elif operation == '+':
        print(a + b)
    elif operation == '*':
        print(a * b)
    elif operation == '/' or operation == '\\':
        print(a / b)
    elif operation == '**' and b == '':
        print(a ** 2)
    elif operation == '**':
        print(a ** b)
    elif operation == '%':
        print(a % b)
    else:
        print('Such operation is not supported!')


print(func_b(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
