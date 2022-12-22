class User:
    def __init__(self):
        self.array = [1, 2, 3]

    def __enter__(self):
        print('__enter__()')
        return self.array

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')
        del self.array


a = User()

with a as arr:
    print(arr[0])

a = User()

with a as arr:
    print(arr[0])
