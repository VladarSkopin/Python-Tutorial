from collections import *

Person = namedtuple('Person', ['name', 'age', 'weight'])

bob = Person('Bob', 45, 223.5)
maria = Person('Maria', 28, 567.45)

print(bob)
print(maria)

print(bob.name, 'is in love with', maria.name)
print(bob[0], 'is in love with', maria[0], 'although she\'s just', maria.age)

