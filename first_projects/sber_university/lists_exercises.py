# lists generators:

a = ['k', 'i', 't', 't', 'y']
b = [i * 3 for i in a]
print(b)

a.append(' ')
a.append('c')
a.extend(['a', 't'])
print(a)

a.insert(0, 'M')
a.insert(1, 'y')
a.insert(2, ' ')
print(a)

b = a.copy()
b.sort()
b.reverse()
print(b)
print(b.index('M'))
print(b.count('t'))
b.pop()
b.reverse()
print(b)
