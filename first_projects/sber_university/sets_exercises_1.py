a = set()
print(a)  # set()
a = set('hello')
print(a)  # {'l', 'e', 'h', 'o'}
a = {'a', 'b', 'c', 'd'}
print(a)  # {'a', 'c', 'b', 'd'}
a = {i ** 2 for i in range(10)}
print(a)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

words = ['hello', 'daddy', 'hello', 'mum']
print(set(words))

print(len(a))
a.pop()
a.remove(64)
a.add('r')
print(a)  # {1, 4, 36, 9, 'r', 16, 49, 81, 25}

b = a.copy()
a.clear()
print(a)  # set()
print(b)
print(b.isdisjoint('a'))  # True -> no mutual elements
print(b.isdisjoint('r'))  # False -> has mutual elements

