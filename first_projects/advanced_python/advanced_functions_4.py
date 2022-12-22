# 3) FUNCTION CAN RETURN A FUNCTION !

def example_function():
    def under_function(param1):
        print(param1)
    return under_function


variable = example_function()
print(variable("test"))
