def sum_of_numbers(x, y):
    return x + y


def fun(surname):
    if len(surname) >= 6:
        print('Hello, ' + surname + '!')
    else:
        print('G\'day mate!')


print(sum_of_numbers(10, 20))
fun(input())
