planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']  # list[str]

print(planets)

planet_third = planets[2]
print(planet_third)
print('There are', len(planets), 'planets in the list')

rivers = ['The Nile', True, 'The Mississippi', 20, False, 'The Thames', 100]  # list[str | bool | int]
print(rivers)

mixture = rivers + planets + [3.14]  # Any
print(mixture)
print('The first element in the mixture is', mixture[0])
print('The last element in the mixture is', mixture[len(mixture) - 1])

planets.pop()
planets.reverse()
print(planets)
planets.append('The Sun')
print(planets)
