class Mathematics:

    @staticmethod  # do not have access to instances
    def add5(x):
        return x + 5

    @staticmethod  # do not have access to instances
    def multiply(x, y):
        return x * y


n1 = Mathematics.add5(10)
print(n1)
n2 = Mathematics.multiply(10, 3)
print(n2)
