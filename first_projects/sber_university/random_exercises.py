import random
from random import randint

print(randint(0, 200))  # 107
print(random.choice('Python is awesome!'))  # y
print(random.choice(['Kitty', 'Doggy', 'kitten', 'rabbit']))  # kitten
print(random.choice([21, 22, 23, 24]))  # 24

array = [1, 2, 3, 4, 5]
random.shuffle(array)
print(array)  # [5, 3, 2, 1, 4]
