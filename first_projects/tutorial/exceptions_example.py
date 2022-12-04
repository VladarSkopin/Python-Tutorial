
x = 5

x = 5 + 'str'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(x)

# -----

print('How old are you?')

age = int(input())
print('You are', age, 'years old')   # ValueError: invalid literal for int() with base 10: 'five'

a = 10
b = 0
print(a / b)  # ZeroDivisionError: division by zero


#if age >= 16:
#print('You are odl enough to drive')  # IndentationError: expected an indented block after 'if' statement on line 20



