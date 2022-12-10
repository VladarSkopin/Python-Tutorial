array = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']

map_to_count_duplicates = {}
for x in array:
    if map_to_count_duplicates.get(x) is None:
        map_to_count_duplicates[x] = 1
    else:
        map_to_count_duplicates[x] += 1

print(map_to_count_duplicates)  # {'abc': 3, 'bcd': 1, 'abd': 2, 'dcd': 1}

for value in map_to_count_duplicates.values():
    print(value, end=' ')  # 3 1 2 1
