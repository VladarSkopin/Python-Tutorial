d = {'a': 1, 'b': 3}
print(d.values())  # dict_values([1, 3])

d1 = dict(short='dict', long='dictionary')
print(d1)  # {'short': 'dict', 'long': 'dictionary'}

d2 = dict([(1, 2), (2, 4)])
print(d2)  # {1: 2, 2: 4}

d3 = dict.fromkeys(['a', 'b'])
print(d3)  # {'a': None, 'b': None}

d4 = dict.fromkeys(['a', 'b'], 100)
print(d4)  # {'a': 100, 'b': 100}


# dictionary generators:
d5 = {a: a ** 2 for a in range(7)}
print(d5)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

d = {1: 2, 2: 4, 3: 9}
# print(d[0])  KeyError
d[0] = 0
d[4] = 4 ** 2
print(d)  # {1: 2, 2: 4, 3: 9, 0: 0, 4: 16}

# d.clear()
# print(d)  # {}
a = d.copy()
print(d.get(2))  # 4
print(d.get(5))  # None
print(d.get(5, 25))  # 25 (default)

