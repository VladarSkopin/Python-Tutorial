# Аргументы функции:
# - обязательные required parameters (в строгом порядке)
# - ключевые named parameters (при вызове функции указаны = любой порядок)
# - по умолячанию default parameters
# - изменяемое число аргументов variable arguments (*args, **kwargs)

# если сразу *args + **kwargs -> обязательно в порядке: *args, **kwargs

def append(my_list):
    # внутри функции создаётся новый список,
    # my_list указывает на [0, 1],
    # а x указывает на [0]
    my_list = [0, 1]


x = [0]
append(x)
print(x)  # [0]
