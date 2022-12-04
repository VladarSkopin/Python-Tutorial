numbers = [1, 4, 5, 7, 4, 3.14, 10, 4, 1]  # list[int | float]

print(min(numbers))
print(max(numbers))
numbers.sort()
print(numbers)
numbers.insert(2, 100)
print(numbers)
print(numbers.count(4))
