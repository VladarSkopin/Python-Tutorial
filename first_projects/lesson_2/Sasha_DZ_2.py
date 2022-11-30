#  task 1

print('Task 1: enter a number of dwarfs:')
diamonds = int(input())
print(diamonds * 10)

# task 3

print('Task 3: enter two numbers:')
x = float(input())
y = float(input())
z = (x + y) / 2.0
print(z)

# task 4

print('Task4: enter a coordinate:')
coordinate = int(input())
print('How many seconds?:')
seconds = int(input())
new_coordinate = coordinate + seconds * 3
print(new_coordinate)

# ТВОРЧЕСКИЕ ЗАДАНИЯ:

# Harry Potter
print("Type the number of Harry's friends:")
friends = int(input())
gifts = friends * 5
print('Harry will receive', gifts, 'presents')

# Rectangle sides
print('Enter side a:')
a = int(input())
print('Enter side b:')
b = int(input())
rectangle_perimeter = (a + b) * 2
rectangle_area = a * b
print('Rectangle perimeter = ', rectangle_perimeter)
print('Rectangle area = ', rectangle_area)

# Fahrenheit
print('Enter degrees Fahrenheit:')
degrees_fahrenheit = float(input())
degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9
print('Degrees Celsius = ', degrees_celsius)
