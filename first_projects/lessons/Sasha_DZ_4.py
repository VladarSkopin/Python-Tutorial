# 1
temperature = float(input())
if temperature > 36.6:
    print('Температура повышена')
else:
    print('Температура нормальная')


# 3
x = int(input())
y = int(input())
if x > y:
    print(x)
else:
    print(y)


# 5
A = int(input())
B = int(input())
C = int(input())
if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
else:
    print(C)


# 6
a = int(input())
b = int(input())
if a != b:
    a = a + b
    b = a + b
else:
    a = 0
    b = 0
print(a, b)


# 7
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('I четверть')
elif x > 0 and y < 0:
    print('IV четверть')
elif x < 0 and y < 0:
    print('III четверть')
else:
    print('II четверть')


# ТВОРЧЕСКОЕ ЗАДАНИЕ 3

# 1
a = int(input())
b = int(input())
if a < b:
    print(a)
elif b < a:
    print(b)
else:
    print('It\'s a tie!')


# 2
num1 = int(input())
num2 = int(input())
if num1 < num2:
    print('Первое число меньше второго')
elif num2 < num1:
    print('Второе число меньше первого')
else:
    print('Числа равны')


# 3
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
if number1 < number2 and number1 < number3 and number1 < number4:
    print(number1)
elif number2 < number1 and number2 < number3 and number2 < number4:
    print(number2)
elif number3 < number1 and number3 < number2 and number3 < number4:
    print(number3)
else:
    print(number4)


# 4
num_to_check = float(input())
if num_to_check > 0:
    print('+')
elif num_to_check < 0:
    print('-')
else:
    print('0')


# 5
A = float(input())
B = float(input())
num_list = []

if A < B:
    num_list.append(A)
    num_list.append(B)
else:
    num_list.append(B)
    num_list.append(A)
for i in num_list:
    print(i)
