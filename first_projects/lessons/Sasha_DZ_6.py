# 1
input_numbers = []
number = int(input())
while number != 0:
    input_numbers.append(number)
    number = int(input())
print(len(input_numbers))


# 3
input_strings = []
string = input()
while string != 'СТОП':
    input_strings.append(string)
    string = input()
print(len(input_strings))


# 4
input_numbers = []
number = int(input())
sum_of_numbers = 0
while number >= 0:
    input_numbers.append(number)
    sum_of_numbers += number
    number = int(input())
print(sum_of_numbers)


# 6
bank_deposit = 10_000
percent = 0.25
months_count = 0
while bank_deposit <= 15_000:
    months_count += 1
    bank_deposit += bank_deposit * percent
print(months_count)


# Творческое задание 5

# 1
temperature_sum = 0
temperature_count = 0
current_temperature = int(input())
while current_temperature > -300:
    temperature_sum += current_temperature
    temperature_count += 1
    current_temperature = int(input())
if temperature_count == 0:
    print(0)
else:
    print(temperature_sum / temperature_count)


# 2
bank_deposit = 100_000
percent = int(input())
years = 0
while bank_deposit < 500_000:
    bank_deposit += bank_deposit * percent / 100
    years += 1
print(years)
print(bank_deposit)
