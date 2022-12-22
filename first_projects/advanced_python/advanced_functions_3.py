# 2) FUNCTIONS CAN BE NESTED !

def example_function():
    def under_function(param1):
        print(param1)
    print(under_function("test"))


example_function()
