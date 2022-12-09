some_string = input()
new_string = ""
split_string = some_string.split(' ')

for word in split_string:
    if word != '':
        new_string += word[0].upper() + word[1:] + ' '

print(new_string)
