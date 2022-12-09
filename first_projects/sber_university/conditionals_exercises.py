print('Which word to break?')
word_to_break = input()

for word in ['My', 'dear', 'kitty', 'cat', 'is', 'Alicia']:
    if word == word_to_break:
        break
    print(word, end=' ')
else:  # if "break" was not executed
    print('\nThe word', word_to_break, 'was not found')


print('\n-----')

n = int(input())
step = 0
while step <= n:
    j = 1
    while j <= step:
        print(j, end='')
        j += 1
    print()
    step += 1
