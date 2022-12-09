# issubset(other) -> True, если все элементы set принадлежат other

set_A = {10, 20, 30, 40, 50}
print(set_A.issubset({10, 20, 30, 40}))  # False
print(set_A.issubset({10, 20, 30, 40, 50}))  # True
print(set_A.issubset({10, 20, 30, 40, 50, 60}))  # True
print(set_A.issuperset({10, 20, 30, 40, 50}))  # True
print(set_A.issuperset({10, 20, 30, 40, 50, 60}))  # False

rivers1 = {'The Nile', 'The Mississippi'}
rivers2 = {'St.Lawrence', 'The Nile'}
rivers_union = rivers1.union(rivers2)
print(rivers_union)  # {'St.Lawrence', 'The Nile', 'The Mississippi'}
rivers_intersection = rivers1.intersection(rivers2)
print(rivers_intersection)  # {'The Nile'}
rivers_difference = rivers1.difference(rivers2)
print(rivers_difference)  # {'The Mississippi'}
rivers1.update({'The Thames', 'The Sena'})
print(rivers1)  # {'The Thames', 'The Mississippi', 'The Nile', 'The Sena'}
