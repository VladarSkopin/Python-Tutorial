def solve(s):
    c = []
    for i in range(len(s)):
        if i % 2 == 0:
            c.append(s[i])
    return c


func = lambda x, y: x + y


print(solve([1, 2, 3, 4, 5, 6, 7, 8]))  # [1, 3, 5, 7]
print(solve('Brisbane'))  # ['B', 'i', 'b', 'n']
print(func(1, 2))  # 3
print(func('Kitty', 'Doggy'))  # KittyDoggy
