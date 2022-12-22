# 1) FUNCTION IS AN OBJECT !

def example_function(param1='test'):
    return param1


print(example_function())  # test

variable = example_function
print(variable)  # <function example_function at 0x0000024FEC678860>
