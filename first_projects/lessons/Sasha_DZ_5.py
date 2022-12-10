# 2
input_numbers = [int(input('First number: ')), int(input('Second number: ')), int(input('Third number: '))]
positive_numbers = 0
negative_numbers = 0
zeros = 0
for i in input_numbers:
    if i > 0:
        positive_numbers += 1
    elif i < 0:
        negative_numbers += 1
    else:
        zeros += 1
print('Positive numbers: ', positive_numbers)
print('Negative numbers: ', negative_numbers)
print('Zeros: ', zeros)


# 3
a = int(input())
if a > 0:
    print('True')
else:
    print('False')


# 4
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    print('True')
else:
    print('False')


# 5
a = int(input())
b = int(input())
c = int(input())
if a > 0 or b > 0 or c > 0:
    print('True')
else:
    print('False')


# 6 является ли число чётным и двузначным
x = 150
x_string = str(x)
if (len(x_string) == 2) and (x % 2 == 0):
    print('True')
else:
    print('False')


# 7
a = int(input())
b = int(input())
c = int(input())
if (a > 100 and b > 100 and c <= 100) or (a > 100 and c > 100 and b <= 100) or (b > 100 and c > 100 and a <= 100):
    print('True')
else:
    print('False')


# Творческое задание 4

# 1
a = int(input())
b = int(input())
if a != b:
    if a > b:
        b = a
    else:
        a = b
else:
    a = 0
    b = 0
print(a)
print(b)


# 2
input_numbers = [int(input('First number: ')), int(input('Second number: ')), int(input('Third number: '))]
even_numbers = 0
odd_numbers = 0
zeros = 0
for i in input_numbers:
    if i == 0:
        zeros += 1
    elif i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print(even_numbers)
print(odd_numbers)
print(zeros)


# 3
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print('True')
else:
    print('False')


# 4
a = int(input())
b = int(input())
if (a < 0 and b >= 0) or (b < 0 and a >= 0):
    print('True')
else:
    print('False')


# 5
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
