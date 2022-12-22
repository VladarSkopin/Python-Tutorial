# Можно создать свой декоратор, не прибегая к сахару Python:

def self_decorator(function_to_decorate):
    def wrap_original_function():  # вложенная ф.
        print('Before')
        function_to_decorate()  # оригинальная ф.
        print("After")
    return wrap_original_function  # возвращаемая ф.


def easy_function():
    print("I am just printing")


decorated_function = self_decorator(easy_function)  # perform decoration

decorated_function()
