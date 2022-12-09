s = 'Python'

print(s[1:2])
print(s[0:])
print(s[:3])
print(s[:])
print(s[3:])

print('-----')

print(s.find('t'))  # index or -1
print(s.rfind('t'))  # index or -1
print(s.index('t'))  # index or ValueError
print(s.rindex('t'))  # index or ValueError
print(s.replace('P', 'J'))
print(s.split('t'))
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())  # digits and letters

print('-----')

print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.upper())
print(s.lower())
print(s.startswith('p'))
print(s.endswith('p'))
print(s.join(['a', 'b', 'c']))
