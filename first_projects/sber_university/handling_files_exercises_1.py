# 'r' -> read
# 'w' -> write, file contents are deleted and rewritten, if doesn't exist -> new is created
# 'x' -> write only if file doesn't exist
# 'a' -> append to the file
# 'b' -> open a binary file mode
# 't' -> open a text file mode (by default)
# '+' -> read and write

f = open('love.txt', 'w')
f.write('Kitty loves her doggy, and doggy loves his kitty')
f.write('\nI love my dear kitten')
f.write('\nI love my dear doggy')
f.close()

f = open('love.txt')
text = f.read()
print(text)
f.close()

f = open('love.txt')
for line in f:
    print('Line: ' + line, end='')
f.close()
