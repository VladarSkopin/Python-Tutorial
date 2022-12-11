import re

# 1
punishment = input()
count = int(input())
if count <= 0:
    print('Must be a positive number!')
else:
    while count > 0:
        print(punishment)
        count -= 1

# 3
for i in range(16):
    print(i)


# 5
print('Type what you wish to buy: ')
purchases = []
current_purchase = input()
while current_purchase.strip().lower() != 'stop':
    purchases.append(current_purchase)
    current_purchase = input()
for i in purchases:
    print(i, end=' ')


# 8
print('\nHow many items are you planning to buy? ')
count = int(input())
purchases = []
if count <= 0:
    print('Number of items should be more than zero!')
else:
    print('Type what you wish to buy: ')
    while count > 0:
        current_purchase = input()
        purchases.append(current_purchase)
        count -= 1
for item in purchases:
    print(item)


# 9
print('\nHow many items are you planning to buy? ')
count = int(input())
purchases = {}
if count <= 0:
    print('Number of items should be more than zero!')
else:
    while count > 0:
        print('Type what you wish to buy (item name): ')
        current_purchase = input()
        print('Amount (whole number): ')
        amount = int(input())
        purchases[current_purchase] = amount
        count -= 1
for key in purchases:
    print(key, purchases[key])


# 10
lines_input = []
lines_found = []
print('Number of lines to search:')
number_of_lines = int(input())
if number_of_lines <= 0:
    print('Number of lines should be more than zero!')
else:
    print('Enter the lines of text:')
    while number_of_lines > 0:
        lines_input.append(input())
        number_of_lines -= 1

    print('Which text to search?: ')
    text_to_search = input()
    for line in lines_input:
        if re.findall(text_to_search, line):
            lines_found.append(line)
    print('Lines, in which the text was found:')
    for line in lines_found:
        print(line)


# Творческое задание 6

# 1
print('How old are you?')
age = int(input())
counter = 1
if age % 2 == 0:
    while counter <= age:
        if counter % 2 == 0:
            print(counter)
        counter += 1
else:
    while counter <= age:
        if counter % 2 != 0:
            print(counter)
        counter += 1


# 2
ingredients = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'хвост змеи']
count = 0
while count < len(ingredients):
    print(count + 1, ingredients[count])
    count += 1

print('-----')

ingredients.append(ingredients[0])
ingredients.remove(ingredients[0])
count = 0
while count < len(ingredients):
    print(count + 1, ingredients[count])
    count += 1


# 3
lines_input = []
lines_found = []
print('Number of lines to search:')
number_of_lines = int(input())
if number_of_lines <= 0:
    print('Number of lines should be more than zero!')
else:
    print('Enter the lines of text:')
    while number_of_lines > 0:
        lines_input.append(input())
        number_of_lines -= 1

    print('Which text to search?: ')
    text_to_search = input()
    for line in lines_input:
        if re.findall(text_to_search, line):
            lines_found.append(line)
    print(text_to_search + ' was found in ' + str(len(lines_found)) + ' lines.')


