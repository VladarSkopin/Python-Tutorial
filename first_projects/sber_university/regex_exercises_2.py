import re

print(re.match(r'Hey', 'Hey Hey'))  # <re.Match object; span=(0, 3), match='Hey'>
print(re.match(r'Hey', 'hey Hey'))  # None

print(re.search(r'Hey', 'hey Hey'))  # <re.Match object; span=(4, 7), match='Hey'>
print(re.search(r'Hey', 'hey Hey').group(0))  # Hey

print(re.findall(r'Hey', 'hey Hey Hey Hey'))  # ['Hey', 'Hey', 'Hey']

print('-----')

# re.split(pattern, string) -> to divide the string with template
print(re.split(r'y', 'hey Hey Hey Hey'))  # ['he', ' He', ' He', ' He', '']

print('-----')

# re.sub(pattern, replacement, string) -> to replace part of a string
print(re.sub(r'Hey', '?', 'hey Hey Hey Hey'))  # hey ? ? ?

print('-----')

# re.compile(pattern) -> for reusing
ex_str = re.compile('Hey')
result = ex_str.findall('hey Hey Hey Hey')
print(result)  # ['Hey', 'Hey', 'Hey']
result2 = ex_str.findall('Hey')
print(result2)  # ['Hey']

