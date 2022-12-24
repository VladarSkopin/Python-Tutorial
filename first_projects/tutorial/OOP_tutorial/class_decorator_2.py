# CLASS DECORATOR

class ErrorCheck:
    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !")
        else:
            return self.function(*params)


@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)


print(add_numbers(20, 30, 40))  # 90
print(add_numbers(20, '30', 40))  # TypeError: parameter cannot be a string !
