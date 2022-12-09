# 1 Спортмастер
print('Enter the kicks price:')
kicks_price = int(input())
print('Enter the jacket price:')
jacket_price = int(input())
print('Enter the backpack price:')
backpack_price = int(input())
total_price = kicks_price + jacket_price + backpack_price
total_price_discount = total_price * 0.1  # 10% discount
price_to_pay = total_price - total_price_discount - 1000
print("Total price = ", int(price_to_pay))

# 1 Определите значение переменной b после выполнения алгоритма
a = 4
b = 4
a = 2 * a + 3 * b
b = a / 2 * b
print(b)

# 2 Фаренгейты в градусы Цельсия
print('Enter degrees Fahrenheit:')
degrees_fahrenheit = float(input())
degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9
print('Degrees Celsius = ', degrees_celsius)

# 3 Поменять местами переменные
a = int(input())
b = int(input())
c = a
a = b
b = c
print(a, b)

# 4 Определите значение переменной a после выполнения алгоритма
a = 17
b = 23
b = a + b + 1
a = b + a
print(a)

# 5 Определите значение переменной a после выполнения алгоритма
a = 4
b = 2
b = a / 2 * b
a = 2 * a + 3 * b
print(a)

# 6 Определите значение переменной a после выполнения алгоритма
a = 5
b = 4
b = 100 - a * b
a = b / 16 * a
print(a)
