d = {1: 2, 2: 4, 3: 9, 0: 0, 4: 4 ** 2}
print(d.items())  # dict_items([(1, 2), (2, 4), (3, 9), (0, 0), (4, 16)])
print(d.keys())  # dict_keys([1, 2, 3, 0, 4])

print(d.pop(1))  # 2
# print(d.pop(10))  # KeyError
print(d.pop(10, 100))  # 100 default
print(d)  # {2: 4, 3: 9, 0: 0, 4: 16}

# popitem() -> удаляет и возвращает пару с конца

print(d.popitem())  # (4, 16)
print(d)  # {2: 4, 3: 9, 0: 0}

d.update({'alex': 'Vance'})
print(d)  # {2: 4, 3: 9, 0: 0, 'alex': 'Vance'}


# setdefault(key[,default]) -> возвращает значение ключа, но если его нет, то созд ключ со значением default
print(d.setdefault(2, 200))  # 4
print(d.setdefault('j', 'Jolly'))  # Jolly
print(d)  # {2: 4, 3: 9, 0: 0, 'alex': 'Vance', 'j': 'Jolly'}
