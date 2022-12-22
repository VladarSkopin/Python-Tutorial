# LIST COMPREHENSION

squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [x for x in fruits if 'a' in x]
print(new_list)  # ['apple', 'banana', 'mango']

uppercase_list = [x.upper() for x in fruits]
print(uppercase_list)  # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

new_list_2 = [x if x != 'banana' else 'orange' for x in fruits]
print(new_list_2)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

odds = [x for x in range(10) if x % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9]

evens = [x for x in range(100) if x % 2 == 0 and x % 10 == 0]
print(evens)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


