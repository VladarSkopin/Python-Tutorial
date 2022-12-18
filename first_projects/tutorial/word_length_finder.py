print('How many words: ')
x = int(input())

words = []
while x > 0:
    words.append(input())
    x -= 1

shortest_word = words[0]
for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print(f'The shortest word is {shortest_word}')
